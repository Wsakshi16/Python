# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:18:35 2023

@author: adity
"""

import psycopg2 as pg2

#CREATE a connection with  postgreSQL
# 'Password' is whatever password you set we set in the install 

conn=pg2.connect(database='testme',user='postgres', password='adityaSG@1')

#Establish a conncetion and start curser to be ready to query
cur=conn.cursor()


cur.execute('''INSERT INTO course1(course_name,course_instructor,topic)
           VALUES('Introducing to SQL' ,'Ram' ,'JUlia') ''');
           
cur.execute('''INSERT INTO course1
           (course_name,course_instructor,topic)
           VALUES('Analysing Survay Data in Python' ,'Sham' ,'Python') ''');
           
cur.execute('''INSERT INTO course1
           (course_name,course_instructor,topic)
           VALUES('Introducing to Chatgpt' ,'Ganesh' ,'Theory') ''');
           
           
cur.execute('''INSERT INTO course1
           (course_name,course_instructor,topic)
           VALUES('Introducing to Statistics in R' ,'Ramesh' ,'R') ''');
           
cur.execute('''INSERT INTO courses1
           (course_name,course_instructor,topic)
           VALUES('Hypothesis Testing in Python' ,'Jayesh' ,'Python') ''');
           
conn.commit()

cur.close()

conn.close()