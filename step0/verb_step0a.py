""" verb_step0a.py Oct, 2014
 Construct verb_step0a.txt from mw.xml
 
"""
import sys, re,codecs
import collections
#class Vrec(object):
# def __init__(self,line):

class Counter(dict):
 def __init__(self):
  self.d = {}
 def update(self,l):
  for x in l:
   if not (x in self.d):
    self.d[x]=0
   self.d[x] = self.d[x] + 1

class Vlex(object):
 def __init__(self,key1,L,H,codestr,key2,vlexstr):
  self.key1=key1
  self.L=L
  self.H=H
  self.codestr=codestr
  self.key2=key2
  self.vlexstr=vlexstr

def verb_step0a(filein,fileout):
 f = codecs.open(filein,"r",'utf-8')

 nout=0
 mrec = 1000000
 recs=[]
 print "dbg mrec = ",mrec
 for line in f:
  line = line.rstrip('\r\n')
  codes=[]
  m = re.search(r'(<key2>.*?</root></key2>)',line)
  if m:
   codes.append('K')  # root in key2
   key2=m.group(1)
  else:
   key2=''
  m = re.search(r'<vlex type="preverb"></vlex>',line)
  if m:
   codes.append('P')
  m = re.search(r'<vlex type="root"></vlex>',line)
  if m:
   codes.append('V')
  m = re.search(r'<vlex>Nom[.]</vlex>',line)
  if m:
   codes.append('N')
  if len(codes) == 0:
   m = re.search(r'<vlex',line)
   if m:
    codes.append('O')   
  if len(codes) == 0:
   continue
  nout = nout + 1
  if nout >= mrec: 
   break
  parts0 = re.split(r'(<vlex.*?>.*?</vlex>)',line)
  vlexes = []
  for part in parts0:
   if part.startswith('<vlex'):
    vlexes.append(part)
  #print vlexes
  m = re.search(r'^(<H.*?>).*<key1>(.*?)</key1>.*<L.*?>(.*?)</L>',line)
  if not m:
   out = "ERROR 1:%s" % line
   print out.encode('utf-8')
   exit(1)
  H = m.group(1)
  key1 = m.group(2)
  L = m.group(3)
  codestr=''.join(codes)
  vlexstr=' '.join(vlexes)
  rec = Vlex(key1,L,H,codestr,key2,vlexstr)
  recs.append(rec)
 f.close()
 fout = codecs.open(fileout,"w","utf-8")
 #c = collections.Counter()
 c = Counter() # this python26 doesn't have Counter in collectins module
 for r in recs:
  out = "%s:%s:%s:%s:%s:%s\n" %(r.key1,r.L,r.H,r.codestr,r.key2,r.vlexstr)
  c.update([r.codestr])
  fout.write(out)
 fout.close()
 print len(recs)," records written to ",fileout
 for code in c.d.keys():
  print code,c.d[code]
if __name__=="__main__": 
 filein = sys.argv[1] # mw.xml
 fileout = sys.argv[3] # verb-prep4.txt
 verb_step0a(filein,fileout)
