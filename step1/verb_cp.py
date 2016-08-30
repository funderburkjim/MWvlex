"""verb_cp.py
   Aug 27, 2016
"""
import sys, re,codecs
#import lxml

def compute_cps(a):
 """ a is a list of two kinds of strings:
  (1) class digits (1,2,...,10)
  (2) pada (A or P)
  Return a list of class-pada strings
  This is a tricky bit of logic.
  The elements of the returned list have one of three forms:
  cp  (where c is 1 to 10, p is A or P.  This is the usual form)
  0p  (A pada with unknown class)
  c   (A class with unknown pada)
  0   (No class and no pada; in this case, there is only 1 item in return list)
 """
 defaultclass='0'
 prev = {'class':defaultclass, 'used':False}
 ans=[]
 for x in a:
  if x in 'AP': 
   # attach pada to previous class, and post to 
   ans.append(prev['class']+ x)
   prev['used']=True
  else: # assume x is a class
   if not prev['used']:
    if prev['class']!=defaultclass:
     # save class without pada
     ans.append(prev['class'])
   prev['class'] = x
   prev['used'] = False
 # deal with possible last naked class
 if not prev['used']:
  if prev['class']!=defaultclass:
   # save class without pada
   ans.append(prev['class'])
 return ans

class Vlex(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (key1,L,H,codestr,key2,vlexstr) = re.split(r':',line)
  self.key1=key1
  self.L=L
  self.H=H
  self.codestr=codestr
  self.key2=key2
  self.vlexstr=vlexstr
  self.line = line
  # each elt. of cps is a class-pada string, of the form
  # (a) cp (integer class 1 to 10, A or P for p)
  #     We all '0p' to indicate that a pada is present with no inferrable class
  # OR
  # (b) c (integer class, with no pada)
  # OR
  # (c) p (pada A or P). 
  self.cps = [] # to be computed in cps_init for roots

 def cps_init(self):
  # use regular expression
  s = self.vlexstr.strip()
  if not s.startswith('<vlex type="root"></vlex>'):
   print "cps_init: WARNING 1",line
   return
  s = s.replace('<vlex type="root"></vlex>','')
  s = s.strip()
  prevclass=None
  cps = [] # preliminary
  for m in re.finditer(r'<vlex>(.*?)</vlex>',s):
   x = m.group(1)
   x = x.replace('cl.','')
   # A1 is Anglicized Sanskrit for capitalized long vowel A, Atmanepada
   x = x.replace('A1','A')  
   x = x.replace('.',' ')
   x = x.replace('_',' ') # Aug 30, 2016. for "BaRq" <vlex>cl.1._10. P.</vlex>
   x = x.strip()   
   x = re.sub(r' +',' ',x)
   cps.append(x)
  cpstr = ' '.join(cps)
  cps1=cpstr.split(' ')
  self.cps = compute_cps(cps1)
  if False:
   # for testing
   x = ' '.join(self.cps)
   self.cps = [cpstr,x]
  return
 
def main_cp(filein,fileout):
 # parse filein to list of Vlex objects
 with codecs.open(filein,"r",'utf-8') as f:
  vlexrecs = [Vlex(line.rstrip('\r\n')) for line in f]
  print "%s has %s records" %(filein,len(vlexrecs))
 # filter to use only vlex cases of simple verb
 verbrecs = [rec for rec in vlexrecs if rec.codestr == 'V']
 print len(verbrecs),"Roots in",filein
 # get cps for the verbrecs
 for rec in verbrecs:
  rec.cps_init()
 # print out new record
 nprob=0
 with codecs.open(fileout,"w",'utf-8') as f:
  for rec in verbrecs:
   cpstr = ','.join(rec.cps)
   out = "%s:%s:%s" %(rec.key1,rec.L,cpstr)
   f.write(out + "\n")
   if '?' in cpstr:
    nprob=nprob+1
 print nprob,"parsing incomplete (search for '?')"

if __name__=="__main__": 
 filein = sys.argv[1] # verb_step0a.txt
 fileout = sys.argv[2] # verb_cp.txt
 main_cp(filein,fileout)
