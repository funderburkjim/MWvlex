""" compare.py Oct 31, 2014
 Compare verb_step0a.txt and verb-prep4.out
"""
import sys, re,codecs
import collections
#class Vrec(object):
# def __init__(self,line):

class Counter(dict):
 def __init__(self):
  self = {}
 def update(self,l):
  for x in l:
   if not (x in self):
    self[x]=0
   self[x] = self[x] + 1

class Vlex(object):
 def __init__(self,key1,L,H,codestr,key2,vlexstr,line):
  self.key1=key1
  self.L=L
  self.H=H
  self.codestr=codestr
  self.key2=key2
  self.vlexstr=vlexstr
  self.line = line
class Prep4(object):
 def __init__(self,key1,L,H,key2,body,line):
  self.key1=key1
  self.L=L
  self.H=H
  self.key2=key2
  self.body=body
  self.line = line

def parse_verb_step0a(line):
 line = line.rstrip('\r\n')
 (key1,L,H,codestr,key2,vlexstr) = re.split(r':',line)
 return Vlex(key1,L,H,codestr,key2,vlexstr,line)

def parse_verb_prep4(line):
 line = line.rstrip('\r\n')
 m = re.search(r'^(<H.*?>).*?<key1>(.*?)</key1>.*?<key2>(.*?)</key2>.*?<body>(.*?)</body>.*?<L.*?>(.*?)</L>',line)
 if not m: 
  print "ERROR parse_verb_prep4:\n",line
  exit(1)
 H = m.group(1)
 key1 = m.group(2)
 key2= m.group(3)
 body=m.group(4)
 L=m.group(5)
 return Prep4(key1,L,H,key2,body,line)

def compare(filein,filein1,filesupl,fileor,fileout):
 # parse filesupl
 supldict={}
 with codecs.open(filesupl,"r",'utf-8') as f:
  for line in f:
   line = line.rstrip('\r\n')
   m = re.search(r'<L +(supL|revL).*?>(.*?)</L>',line)
   if not m:
    print "supl ERROR: ",line
    exit(1)
   sr = m.group(1)
   L = m.group(2)
   supldict[L]=sr

 # parse fileor
 ordict={}
 with codecs.open(fileor,"r",'utf-8') as f:
  for line in f:
   line = line.rstrip('\r\n')
   m = re.search(r'<L.*?>(.*?)</L>',line)
   if not m:
    print "orgroup ERROR: ",line
    exit(1)
   L = m.group(1)
   ordict[L]='OR'

 # parse filein to list of Vlex objects
 with codecs.open(filein,"r",'utf-8') as f:
  vlexrecs = [parse_verb_step0a(line) for line in f]
  print "%s has %s records" %(filein,len(vlexrecs))
 vlexrecs = [r for r in vlexrecs if r.codestr != 'X']
 print "%s has %s records with codestr!=X" %(filein,len(vlexrecs))
 # parse filein1 to list of Prep4 objects
 with codecs.open(filein1,"r",'utf-8') as f:
  prep4recs = [parse_verb_prep4(line) for line in f]
  print "%s has %s records" %(filein1,len(prep4recs))
 # make dictionary of Lnums for each
 Lvlexdict = {}
 for r in vlexrecs:
  Lvlexdict[r.L] = r
 Lprep4dict = {}
 for r in prep4recs:
  Lprep4dict[r.L] = r
 # lists of keys
 Lvlexkeys = Lvlexdict.keys()
 Lprep4keys = Lprep4dict.keys()
 Lbothset = set(Lvlexkeys).intersection(set(Lprep4keys))
 print "%s has %s L values" %(filein,len(Lvlexkeys))
 print "%s has %s L values" %(filein1,len(Lprep4keys))
 print "%s L values in both files" % len(Lbothset)
 Lvlexonly =  set(Lvlexkeys).difference(set(Lprep4keys))
 print "%s has %s unique L values" %(filein,len(Lvlexonly))
 Lprep4only = set(Lprep4keys).difference(set(Lvlexkeys))
 print "%s has %s unique L values" %(filein1,len(Lprep4only))

 Lunion = set(Lvlexkeys).union(set(Lprep4keys))
 Lunion = sorted(Lunion,key=lambda L: "%10.2f"%float(L))
 fout = codecs.open(fileout,"w",'utf-8')
 cout = Counter()
 for L in Lunion:
  if L in Lbothset:
   r1 = Lvlexdict[L]
   r2 = Lprep4dict[L]
   if r1.key1 == r2.key1:
    out = "BOTHEQ:%s:%s" %(L,r1.key1)
   else:
    out = "BOTHNE:%s:%s:%s" %(L,r1.key1,r2.key1)
  elif L in Lvlexonly:
   r1 = Lvlexdict[L]
   if L in supldict:
    out="%s:%s:%s" %(supldict[L],L,r1.key1)
   elif L in ordict:
    out="%s:%s:%s" %(ordict[L],L,r1.key1)
   else:
    out = "VLEX:%s:%s" %(L,r1.key1)
  elif L in Lprep4only:
   r2 = Lprep4dict[L]
   out = "PREP4:%s:%s" %(L,r2.key1)
  else:
   print "ERROR L=",L
   continue
  fout.write("%s\n" % out)
  # update cout counter
  m = re.search(r'^(.*?):',out)
  if not m:
   print "ERROR with cout. out =",out
   continue
  code = m.group(1)
  cout.update([code])
 fout.close()
 # print summary stats of cout
 keys = cout.keys()
 print "cout has ",len(keys)," keys"
 for code in sorted(cout.keys()):
  print code,cout[code]

if __name__=="__main__": 
 filein = sys.argv[1] # verb_step0a.txt
 filein1 = sys.argv[2] # verb-prep4.out
 filesupl = sys.argv[3] # supl.txt
 fileor = sys.argv[4] # orgroup.txt
 fileout = sys.argv[5] # compare.txt
 compare(filein,filein1,filesupl,fileor,fileout)
