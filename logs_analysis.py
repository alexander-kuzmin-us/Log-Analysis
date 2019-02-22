#!/usr/bin/env python3

# Udacity ND Loganalysis Project

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


# 1. Most popular articles
def get_top_three_articles():
# Query 1 (I used the JOIN clause to select titles from 2 tables log and
# articles ON slug and path. And Substr 10 char lengh str from path in log to
# find a matched  slug in articles)
    query = """
    SELECT title COUNT(*) AS num
    FROM articles
    JOIN log
    ON articles.slug LIKE substr(log.path, 10)
    GROUP BY title
    ORDER BY num
    DESC
    LIMIT 3;
    """

# Run Query 1
    result = run_query(query)
# Print result Query 1
print ('TOP 3 MOST POPULAR ARTICLES OF ALL TIME\n')
for result in results:
    print('"{title}" - {num} total views').
    format(title=result[0], num=result[1]))
