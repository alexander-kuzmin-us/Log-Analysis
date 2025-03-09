#!/usr/bin/env python3

"""
Log Analysis Tool
Part of the Udacity Full Stack Web Developer Nanodegree
This script connects to a PostgreSQL database containing newspaper site logs
and answers three analytical questions about article popularity and errors.
"""

import psycopg2
import sys
from datetime import datetime

DBNAME = "news"


def connect_to_database():
    """Establish and return a connection to the news database."""
    try:
        connection = psycopg2.connect(database=DBNAME)
        return connection
    except psycopg2.DatabaseError as e:
        print(f"Database connection error: {e}")
        sys.exit("Unable to connect to the database")


def run_query(query):
    """
    Connect to the news database, execute the query, and return results.
    
    Args:
        query (str): SQL query to execute
        
    Returns:
        list: Results of the query
    """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_top_three_articles():
    """
    Find the three most popular articles of all time.
    
    Returns:
        None: Prints results directly
    """
    query = """
        SELECT articles.title, COUNT(*) as views
        FROM articles
        JOIN log ON articles.slug = SUBSTRING(log.path, 10)
        WHERE log.path LIKE '/article/%'
        GROUP BY articles.title
        ORDER BY views DESC
        LIMIT 3;
    """
    
    results = run_query(query)
    
    print('\nTOP THREE MOST POPULAR ARTICLES OF ALL TIME:\n')
    for result in results:
        print(f'"{result[0]}" - {result[1]} total views')
    
    return results


def get_top_article_authors():
    """
    Find the most popular article authors of all time.
    
    Returns:
        None: Prints results directly
    """
    query = """
        SELECT authors.name, COUNT(*) AS views
        FROM authors
        JOIN articles ON authors.id = articles.author
        JOIN log ON articles.slug = SUBSTRING(log.path, 10)
        WHERE log.path LIKE '/article/%'
        GROUP BY authors.name
        ORDER BY views DESC
        LIMIT 3;
    """
    
    results = run_query(query)
    
    print('\nTOP THREE MOST POPULAR AUTHORS OF ALL TIME:\n')
    for result in results:
        print(f'"{result[0]}" - {result[1]} total views')
    
    return results


def get_days_with_more_than_one_percent_errors():
    """
    Find days where more than 1% of requests led to errors.
    
    Returns:
        None: Prints results directly
    """
    query = """
        WITH daily_requests AS (
            SELECT 
                DATE(time) AS day,
                COUNT(*) AS total_requests
            FROM log
            GROUP BY day
        ),
        daily_errors AS (
            SELECT 
                DATE(time) AS day,
                COUNT(*) AS error_count
            FROM log
            WHERE status != '200 OK'
            GROUP BY day
        )
        SELECT 
            TO_CHAR(dr.day, 'Month DD, YYYY') AS formatted_date,
            ROUND((de.error_count * 100.0 / dr.total_requests), 1) AS error_percentage
        FROM daily_requests dr
        JOIN daily_errors de ON dr.day = de.day
        WHERE (de.error_count * 100.0 / dr.total_requests) > 1.0
        ORDER BY error_percentage DESC;
    """
    
    results = run_query(query)
    
    print('\nDAYS WITH MORE THAN 1 PERCENT ERRORS:\n')
    for result in results:
        print(f'"{result[0]}" - {result[1]}% errors')
    
    return results


def main():
    """Execute all queries and display results."""
    print("Analyzing newspaper logs...")
    get_top_three_articles()
    get_top_article_authors()
    get_days_with_more_than_one_percent_errors()
    print("\nAnalysis complete.")


if __name__ == '__main__':
    main()
