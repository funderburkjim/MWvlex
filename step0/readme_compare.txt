readme_compare.txt


Oct 31, 2014
The file verb-prep4.out (from 2008 work) is comparable to verb-step0a.txt, but
with a different format.  
verb-prep4.out   9962 lines
verb_step0a.txt 10415 lines
 Excluding 'X'  10319 lines
Question: How to account for those (10319-9962) = 357 lines?

Many are due to supplement records, which were not available in 2008.
Create a file with the L numbers of supplement and revision records:
sed -n 's/.*\(<L .*<\/L>\)/\1/p' ../../../pywork/mw.xml > supl.txt
sample lines:
<L supL="300010">27.1</L></tail></H3>
<L revL="300020">52</L></tail></H1A>



Nov 1, 2014
11426, aBijYu  correct MW markup as this not a root, but an indeclineable.
Remake verb_step0a.txt, with revised summaries:
10414  records written to  verb_step0a.txt  (1 less than previous)
X 96  
K 6395  (1 less than previous)
N 1215
P 620
V 2088

Nov 1, 2014 compare-edit.txt
compare.txt was revised to see how many differences between verb-prep4.out and
verb_step0a.txt could be further explained by the OR condition.

Here's the thinking:  
Many MW records have the form  X or Y ...
Look at the example from page 11: aRW.
  The text reads: aRW or aW, cl.1. A., ...
  At some point (after verb-prep4.out was made), we decided that there
should be two headwords, with essentially identical data.  But, we wanted
to add metadata to each record indicating that it was paired with another 
record. What we came up with looks, in the xml, like:
  key1=aRW, L= 2447   <OR group="2447,aRW;2447.1,aW"/>
  key1=AW,  L= 2447.1 <OR group="2447,aRW;2447.1,aW"/>
At the time verb-prep4.out was made, this coding was absent so there was only
one record, for aRW.  So verb-prep4.out has only a record for aRW, while
verb-step0a.txt has a record for both aRW and aW.  
The orgroup.txt file was constructed to have all the L-numbers for records
with matching pattern '<OR group='; so for instance it has both 2447 and
2447.1.  (Of course, there are many OR group records that are for nouns
also; these are in orgroup.txt also).

The compare.py program was adjusted to try to 'explain' this fact. When it
finds aW, 2447.1 only in verb-step0a.txt, it looks for 2447.1 in orgroup.txt;
since it finds it in this case, it writes the line 'OR:2447.1:aW' in
compare.txt.  There are 131 cases like this.

Here's the compare.py is run now:
python26 compare.py verb_step0a.txt verb-prep4.out supl.txt orgroup.txt compare.txt

The program prints summary statistics regarding the lines of compare.txt:
BOTHEQ 9909    L is in both, and key1 is same 
BOTHNE 42      L is in both, but key1 differs.
OR 131         L not in prep4, but L is in orgroup
revL 2         L not in prep4, this is a revision record from supplement
supL 65        L not in prep4, this is a supplement record from supplement
VLEX 169       L not in prep4, and not yet explained
PREP4 11       L is in prep4 only, and not yet explained.

It is of interest to investigate the last two classes further.
In compare-edit.txt,  a comment was added to each of these cases.  

The BOTHNE cases have not been completely examined.  A partial examination
suggests that in these cases, the spelling of the headword has been corrected
since prep4 was originally done.

Some tasks that remain to be done:
  There are some obvious subclasses of the VLEX records in compare-edit.txt.
  Possible actions:
  (a) de-classify some of these as verbs (e.g., the 'see', 'vl' groups)
  (b) add OR coding to several cases.  For instance, 32059.1:und: or ud
  (c) Confirm that the remaining (such as amB) really should be called verbs
  (d) re-examine the 11 PREP4 cases, and see if any should be reclassified
      (and recoded) as verbs, notably
      garhaRAMyA, dUrekf, dUreBU, dUregam

When this is done, we will have a good explanation of the differences 
between the verb-prep4.out and verb_step0a.txt.  Then, we can feel 
comfortable in doing further work solely based on verb_step0a.txt.


There is some further work to do, even among those records appearing in
both files.  For instance, the goofy AIkz cases should NOT be in a final
list of MW roots.  But that analysis is yet to be done.


