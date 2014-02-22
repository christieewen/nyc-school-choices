nyc-school-choices
==================

Assist people in finding a good school by the schools' offerings such as curriculum, AP classes, and other information.  



Program Table
=============
http://nycdoe.pediacities.com/dataset/hsdirectory/resource/eba79ed6-9196-450b-aef1-17e828e189b1


Significant Columns: PROGRAM | INTEREST | METHOD

QUERY: select _id, DBN, CODE, PROGRAM, INTEREST, METHOD from "eba79ed6-9196-450b-aef1-17e828e189b1" order by PROGRAM, INTEREST, METHOD

Query example (via SQL statement)
http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT * from "eba79ed6-9196-450b-aef1-17e828e189b1" WHERE title LIKE 'jones'
