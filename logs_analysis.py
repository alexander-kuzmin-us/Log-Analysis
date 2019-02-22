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
    SELECT title, COUNT(*) AS num
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
print ('TOP 3 MOST POPULAR ARTICLES OF ALL TIME:\n')
for result in results:
    print('"{title}" - {num} total views').
    format(title=result[0], num=result[1]))

# 2. Most popular authors
def get_top_article_authors():
# Query 2
    query = """
    SELECT authors.name, COUNT(*) AS num
    FROM authors
    JOIN articles
    ON autors.id = articles.autor
    JOIN log
    ON articles.slug LIKE substr(log.path, 10)
    GROUP BY autors.name,
    ORDER BY num
    DESC
    LIMIT 3;
    """
# Run Query 2
    result = run_query(query)

# Print result 2
    print('TOP 3 MOST POPULAR AUTHORS:\n')
    for result in results:
        print('"{author}" - {num} total views').
        format(author=result[0], num=result[1]))


# 3. Days which more then 1% of HTTP requests errors
def get_days_with_more_than_one_percent_errors():
    # Query String 3
    query = """
    SELECT requests.date, 100*errors.errors_count/requests.requests_count
    AS percent
    FROM
    (SELECT date_trunc('day', log.time) AS "date", count(*) AS errors_count
    FROM log
    WHERE log.status != '200 OK'
    GROUP BY date
    ORDER BY date) AS errors
    JOIN
    (SELECT date_trunc('day', log.time) AS "date", count(*) AS requests_count
    FROM log
    GROUP BY date
    ORDER BY date) AS requests
    ON errors.date = requests.date
    WHERE 100*errors.errors_count/requests.requests_count > 1
    ORDER BY percent
    DESC;
    """

    # Run Query 3
    results = run_query(query)

    # Print Results 2
    print('DAY WITH MORE THAN 1 PERCENT ERRORS:\n')
    for result in results:
        print('"{day}" - {percent}% errors'.
        format(day=result[0].strftime('%B %d, %Y'), percent=result[1]))


print('\nYour request is in progress, please wait...\n')
get_top_three_articles()
print('\nThe next request is in progress...\n')
get_top_article_authors()
print('\nAlmost done. Wait a second...\n')
get_days_with_more_than_one_percent_errors()
