readme.org for MWvlex repository


Oct 26, 2014.  

## step0: Extraction of raw verb information from MW records.

The script `redo.sh` remakes verb_step0a.txt from mw.xml.
This file has information for all kinds of verbs presented in a raw
semi-xml form.  See step0/readme.txt for further details of the
format of this file.

Some attention is also given to comparison of verb_step0a with an earlier
version `verb-prep4.out`. The `readme_compare.txt` file discusses this
comparison.

## step1

The simple (non-prefixed, non-denominative, non-whatever) roots from
`step0/verb_step0a.txt` are selected, and the class-pada information 
extracted into a more easily parsed form.  The result is `verb_cp.txt`.



