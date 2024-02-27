# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:23:47 2023

@author: adity
"""


import psycopg2 as pg2


conn=pg2.connect(database='testme',user='postgres', password='adityaSG@1')

cur= conn.cursor()


conn.commit()

cur.execute('''SELECT course_name,course_instructor,topic,course_duration,course_fees
            FROM course1
            INNER JOIN Programming_language
            ON course1.course_id=Programming_language.course_id''')

rows=cur.fetchall()