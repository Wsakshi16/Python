# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:41:28 2023

@author: adity
"""

#After installing with pip install psycopg2
import psycopg2 as pg2

#Create a connection with PostgreSQL
#'password' is whatever password you set, we set password in this case as 'adityaSG@1'
conn = pg2.connect(database = 'dvd',user='postgres',password='adityaSG@1')

#Establish connection and start cursor to be ready to query
cur = conn.cursor()

#Pass in a PostgreSQL query as a string
cur.execute("SELECT * FROM payment")

#Return a tuple of the first row as Python objects
cur.fetchone()

#Return N number of rows
cur.fetchmany(10)

# Return All rows at once
cur.fetchall()

#To save and index results. assign it to a variable
data = cur.fetchmany(10)

#Dont forget to close the connection:
#Killig the kernel or shutting down jupyter will also close it
conn.close()

#################################################################################


#After installing with pip install psycopg2
import psycopg2 as pg2

#Create a connection with PostgreSQL
#'password' is whatever password you set, we set password in this case as 'adityaSG@1'
conn = pg2.connect(database = 'testme',user='postgres',password='adityaSG@1')

#Establish connection and start cursor to be ready to query
cur = conn.cursor()

#Execute a command : create courses table
cur.execute("""CREATE TABLE course1(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR (50) UNIQUE NOT NULL,
    course_instructor VARCHAR (100) NOT NULL,
    topic VARCHAR (20) NOT NULL);
    """)

#Make the changes to the database persistent
conn.commit()

#close cursor and communicatiion with the database
cur.close()

##########################################################################################
