readme.txt for MWvlex/step0
Oct 26, 2014
Jim Funderburk

A first crude extraction from MW of information regarding verbs.
Historical note: verb_step0a.txt is comparable to an older verb-prep4.out.


There are 5 criteria for roots: (See Oct 30 for revision)
K : record contains form <key2>.*?</root></key2>
P : record contains <vlex type="preverb"></vlex>
V : record contains <vlex type="root"></vlex>
N : record contains <vlex>Nom.</vlex> 
O : record has none of the above forms AND it contains <vlex
    Not sure what these are 
Here are the summary results found in verb_step0a.txt:
10418  records written to  verb_step0a.txt
P 31
K 6386
N 1213
V 2088
O  700


Oct 29, 2014
Many of the 'O' records are preverbs, with addtional information such
 as base root, preverbs, homonym.
Regenerate the output, reclassifying 'P' as
P : record contains <vlex type="preverb">
Do this by modifying verb-step0a.py, and over-writing verb-step0a.txt
The summary information is now:
10418  records written to  verb_step0a.txt
P 621
K 6386
N 1213
O 110
V 2088

Investigation of the 'O' cases:
1a. 7 'kf' verbs. key2 should be recoded like 
 aMSIkf:38:<H3>:K:<key2>aMSI-<root>kf</root></key2>:
 Note all of these are from supplement.
akzilakzIkf:654.1:<H3>:O::<vlex>P.</vlex>
agocarIkf:878.2:<H3>:O::<vlex>P.</vlex>
agraRIkf:1231.1:<H4>:O::<vlex>P.</vlex>
aNgArasAtkf:1659.1:<H3>:O::<vlex>P.</vlex>
atiTIkf:2996.1:<H3>:O::<vlex>P.</vlex>
antarIkf:8273.1:<H1>:O::<vlex>P.</vlex>
grAsapAtrIkf:68581.1:<H3>:O::<vlex>P.</vlex>

1b. 1 'BU' verb. Similarly recode key2.
atiTIBU:3006.1:<H3>:O::<vlex>P.</vlex>
 Also from supplemtn

1c. Other markup errors
anunirjihAna:6537:<H1>:O::<vlex>A1.</vlex>  Add type="nhw" markup

dAmani:91634:<H3>:O::<vlex type="nhw">P.</vlex>
  markup error. P. is  ls for Panini.
vAmoru:191029:<H3>:O::<vlex type="nhw">Nom.</vlex>
vAmorU:191030:<H3>:O::<vlex type="nhw">Nom.</vlex>
  markup error: should be <ab>Nom.</ab>  (Nominative case)
viDmA:196475.1:<H1>:O::<vlex>P.</vlex>
  markup error: Should be prefix verb
suhfdadruh:250717:<H3>:O::<vlex type="nhw">Nom.</vlex>
  markup error: should be <ab>Nom.</ab>  (Nominative case)

Other changes:
avavarti:18115:<H1>:O::<vlex>A1.</vlex>
  Change markup to <vlex type="nhw">A1.</vlex> 
kawakawAya:42165.1:<H2>:O::<vlex>P.</vlex> <vlex>A1.</vlex>
  add <vlex>Nom.</vlex> 
nirvfta:107358.1:<H3>:O::<vlex>P.</vlex>
  change <vlex>P.</vlex> to <vlex type="nhw">P.</vlex>
po:129230:<H1>:O::<vlex type="hwinfo">Nom.</vlex>
  change hwinfo to nhw

Oct 30, 2014
There are 5 criteria for roots:
K : record contains form <key2>.*?</root></key2>
P : record contains <vlex type="preverb"></vlex>
V : record contains <vlex type="root"></vlex>
N : record contains <vlex>Nom.</vlex> 
X : record contains <vlex type="nhw">  (nhw == not headword)
O : record contains none of above patterns

After the above changes, regenerate verb_step0a.txt.

10415  records written to  verb_step0a.txt
X 96  
K 6396 
N 1215
P 620
V 2088

NOTE Feb 21, 2014:  After adding some 'verb' markup, the statistics are:
10473  records written to  verb_step0a.txt
X 96
K 6395
N 1215
P 619
V 2148


Note that all records belong to just one class.
Those that are 'X' are NOT verbs, but the sense refers to some other verb.

Below is a crude categorization of the X types.

2a. Present middle participles.
 Pattern Ana:.*?<vlex type="nhw">A1.</vlex>
 21 records


2b. Present middle participle, ending in ARa:
 Pattern ARa:.*?<vlex type="nhw">A1.</vlex>
 10 records:

2c. Present middle participle, ending in ana. 
 2 records, different patterns:
jajYana:76508:<H1>:O::<vlex type="nhw">A1.</vlex>
nimittAyamAna:108991:<H3>:O::<vlex type="nhw">Nom.</vlex>

3. Present active participles.
 Pattern at:.*?<vlex type="nhw">P.</vlex>
 14 records
4. Perfect participles in 'vas'
 Pattern vas:.*?<vlex type="nhw">P.</vlex>
 6 records

4. Other participles:
aBrayantI:13720:<H2>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">P.</vlex>
aNkUyat:1481:<H2>:O::<vlex type="nhw">Nom.</vlex>
raGuyat:173245:<H2>:O::<vlex type="nhw">Nom.</vlex>
rayIyat:175286:<H2>:O::<vlex type="nhw">Nom.</vlex>

5. Misc.
 ArDaDAtuka:26519:<H2>:O::<vlex type="nhw">P.</vlex> <vlex type="nhw">A1.</vlex>
  P,A mentioned in defn of technical grammatical term
- fut. pass. part. uttamAyya:31138:<H2>:O::<vlex type="nhw">Nom.</vlex>
- p.p fdDita:38945:<H2>:O::<vlex type="nhw">Nom.</vlex>
- p.p kapAwita:43379:<H2>:O::<vlex type="nhw">Nom.</vlex>
- used with DA canas:71516:<H2>:O::<vlex type="nhw">P.</vlex> <vlex type="nhw">A1.</vlex>
- name of root class: tudAdi:85880:<H3>:O::<vlex type="nhw">cl.6.</vlex>
- Nom. dutaya : dUta:94866:<H1>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">P.</vlex>
- Used with Bf : Dana:99259:<H2A>:O::<vlex type="nhw">A1.</vlex>
- Nom. *lAya : nakzatramAlA:102886:<H3A>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">A1.</vlex>
- Nom. *SAya : padmakoSa:115568:<H3>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">A1.</vlex>
- Nom. : prasAda:137837:<H2>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">P.</vlex>
- Also Nom. : prAleya:138936:<H3B>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">P.</vlex>
- Also Nom. : prAyaScittIya:140173:<H3A>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">A1.</vlex>
- with kf: priya:140437:<H2>:O::<vlex type="nhw">A1.</vlex>
- with kf: mamatva:157969:<H3>:O::<vlex type="nhw">P.</vlex>
- with kf: maraRa:158120:<H2>:O::<vlex type="nhw">A1.</vlex>
- with kf: miTuyA:164345:<H2>:O::<vlex type="nhw">P.</vlex>
- with car, BU: miTus:164346:<H2>:O::<vlex type="nhw">P.</vlex> <vlex type="nhw">P.</vlex>
- with kf, etc.: miTyA:164354:<H2>:O::<vlex type="nhw">A1.</vlex>
- *tI-kf : lokAyata:183507:<H3B>:O::<vlex type="nhw">P.</vlex>
- with kf: viSaNkA:200417:<H2A>:O::<vlex type="nhw">A1.</vlex>
- *gI-BU : visPuliNga:202967:<H3>:O::<vlex type="nhw">P.</vlex>
- with kf : saMviBAga:226263:<H2A>:O::<vlex type="nhw">A1.</vlex>
- with tul: samakakzA:233024:<H3B>:O::<vlex type="nhw">P.</vlex>
- with kf : samaveza:233184:<H3>:O::<vlex type="nhw">A1.</vlex>
- with ADA: sAmmuKya:242649:<H2>:O::<vlex type="nhw">A1.</vlex>
- with ava-tan, A-tan: sTira:255730:<H2B>:O::<vlex type="nhw">P.</vlex> <vlex type="nhw">A1.</vlex> <vlex type="nhw">A1.</vlex>
- with kf: hiNkAra:262803:<H3>:O::<vlex type="nhw">P.</vlex>


6. 'From' or related to a Denominative verb:
Amukulita:25545:<H1>:O::<vlex type="nhw">Nom.</vlex>
udDUpana:33146:<H1>:O::<vlex type="nhw">Nom.</vlex>
kraSita:57952:<H1>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">P.</vlex>
tanmAnin:82211:<H3>:O::<vlex type="nhw">Nom.</vlex> <vlex type="nhw">P.</vlex>
tapasya:82742:<H2B>:O::<vlex type="nhw">A1.</vlex>
pravaRAyita:136725:<H2>:O::<vlex type="nhw">Nom.</vlex>
barhAyita:142985:<H2>:O::<vlex type="nhw">Nom.</vlex>

7. From a verb
- from vid  jAtavedas:78614:<H3>:O::<vlex type="nhw">cl._6</vlex> <vlex type="nhw">cl.2.</vlex>

See readme_compare.txt for the next step.
