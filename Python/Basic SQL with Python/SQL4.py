# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:21:27 2023

@author: adity
"""


import psycopg2 as pg2

conn=pg2.connect(database='testme',user='postgres', password='adityaSG@1')

cur=conn.cursor()

cur.execute('SELECT course_instructor, COUNT(*) FROM courses1 GROUP BY course_instructor')

conn.commit()


rows=cur.fetchall()

for row in rows:
    print(row)