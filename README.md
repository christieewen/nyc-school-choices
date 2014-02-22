nyc-school-choices
==================

Assist people in finding a good school by the schools' offerings such as curriculum, AP classes, graduation rates, college rates, location, commute, afterschool such as sports, crime data, ELL, Special Ed and other information.  
Currently, this contains only High School data.  Plan includes all schools.


Program Table
=============
http://nycdoe.pediacities.com/dataset/hsdirectory/resource/eba79ed6-9196-450b-aef1-17e828e189b1


Significant Columns: PROGRAM | INTEREST | METHOD

QUERY: select _id, DBN, CODE, PROGRAM, INTEREST, METHOD from "eba79ed6-9196-450b-aef1-17e828e189b1" order by PROGRAM, INTEREST, METHOD

Query example (via SQL statement)
http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT * from "eba79ed6-9196-450b-aef1-17e828e189b1" WHERE title LIKE 'jones'


Quality Review Table
====================
http://nycdoe.pediacities.com/dataset/hsdirectory/resource/be80a13b-e6d8-4943-934b-d22a4c75affe

Significant Columns: max(Quality_Review_Year) | Quality_Review_Score | Progress_Rpt_MM-YY | graduation YYYY-MM | college enroll YYYY-MM

Query: select _id, DBN, max(Quality_Review_Year), Quality_Review_Score, Progress_Rpt_MM-YY, graduation YYYY-MM | college enroll YYYY-MM from "be80a13b-e6d8-4943-934b-d22a4c75affe"


Query example (via SQL statement)
http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT * from "be80a13b-e6d8-4943-934b-d22a4c75affe"  WHERE title LIKE 'jones'


School Table
============
http://nycdoe.pediacities.com/dataset/hsdirectory/resource/45f6a257-c13a-431b-acb9-b1468c3ff1e9

Significant Columns: BN | Building Code | loc | Boro | Printed Name | Alphabetic_Name_Long | grade span YYYY-YYYY min | grade span YYYY-YYYY max | Bus | Subway | Total Students MM/DD | Advanced Placement Courses | Neighborhood | Postal Code

Query: select BN, Building Code, loc, Boro, Printed Name, Alphabetic_Name_Long, grade span YYYY-YYYY min, grade span YYYY-YYYY max, Bus, Subway, Total Students MM/DD, Advanced Placement Courses, Neighborhood, Postal Code from "45f6a257-c13a-431b-acb9-b1468c3ff1e9"

Query example (via SQL statement)
http://nycdoe.pediacities.com/api/action/datastore_search_sql?sql=SELECT * from "45f6a257-c13a-431b-acb9-b1468c3ff1e9" WHERE title LIKE 'jones'


Thanks Emily Pries for information in selecting data.
