#!/usr/bin/env python3

#Udacity ND Loganalysis Project

import psycopg2

DBNAME = "news"


def run_query(query):
    # Connects to "news" database, define the cursor,
    # runs the query, close connection and return the results
    try:
        con = psycopg2.connect(database=DBNAME)
    except psycopg2.DatabaseError:
        print("I am unable to connect to the database")
    cursor = con.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    con.close()
    return rows
    
