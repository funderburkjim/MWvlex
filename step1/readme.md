
## verb_cp.txt

```
python verb_cp.py ../step0/verb_step0a.txt verb_cp.txt
```

There are 2151 records in the output file. 
Each record represents a record of mw.xml corresponding to a verb;
the record has three colon-delimited fields:
* key1  (spelling of root, in SLP1 transliteration)
* L     (record identifier in mw.xml)
* cplist the implied class pada information, represented as a
  comma-delimited list of elements of the following form:
  * cp  (where c is 1 to 10, p is A or P.  This is the usual form)
  * 0p  (A pada with unknown class)
  * c   (A class with unknown pada)
  * 0   (No class and no pada; in this case, this is the only item of cplist)


