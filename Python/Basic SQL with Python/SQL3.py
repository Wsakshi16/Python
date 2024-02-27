# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:20:51 2023

@author: adity
"""

import psycopg2 as pg2


conn=pg2.connect(database='testme',user='postgres', password='adityaSG@1')

cur= conn.cursor()

cur.execute('SELECT * FROM course1;')

rows=cur.fetchall()

conn.commit()

conn.close()

for row in rows:
    print(row)