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
    Find the three most popular articles of all time by using the
    article_views view.
    
    Returns:
        None: Prints results directly
    """
    query = """
        SELECT a.title, v.views
        FROM articles a
        JOIN article_views v ON a.slug = v.slug
        ORDER BY v.views DESC
        LIMIT 3;
    """
    
    results = run_query(query)
    
    print('\nTOP THREE MOST POPULAR ARTICLES OF ALL TIME:\n')
    for result in results:
        print(f'"{result[0]}" - {result[1]} total views')
    
    return results


def get_top_article_authors():
    """
    Find the most popular article authors of all time by using the
    article_views view.
    
    Returns:
        None: Prints results directly
    """
    query = """
        SELECT authors.name, SUM(article_views.views) AS total_views
        FROM authors
        JOIN articles ON authors.id = articles.author
        JOIN article_views ON articles.slug = article_views.slug
        GROUP BY authors.name
        ORDER BY total_views DESC
        LIMIT 3;
    """
    
    results = run_query(query)
    
    print('\nTOP THREE MOST POPULAR AUTHORS OF ALL TIME:\n')
    for result in results:
        print(f'"{result[0]}" - {result[1]} total views')
    
    return results


def get_days_with_more_than_one_percent_errors():
    """
    Find days where more than 1% of requests led to errors by using the
    daily_logs view.
    
    Returns:
        None: Prints results directly
    """
    query = """
        SELECT
            TO_CHAR(day, 'Month DD, YYYY') AS formatted_date,
            ROUND((error_requests * 100.0 / total_requests), 1) AS error_percentage
        FROM daily_logs
        WHERE (error_requests * 100.0 / total_requests) > 1.0
        ORDER BY error_percentage DESC;
    """
    
    results = run_query(query)
    
    print('\nDAYS WITH MORE THAN 1 PERCENT ERRORS:\n')
    for result in results:
        print(f'"{result[0]}" - {result[1]}% errors')
    
    return results


def run_ddl_query(query):
    """
    Execute a DDL query, like creating a view.
    No results are returned from this function.
    """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def create_article_views():
    """
    Create a view that summarizes article views.
    This view will be used in other queries.
    """
    query = """
        CREATE OR REPLACE VIEW article_views AS
        SELECT
            articles.slug,
            COUNT(*) AS views
        FROM articles
        JOIN log ON articles.slug = SUBSTRING(log.path, 10)
        WHERE log.path LIKE '/article/%'
        GROUP BY articles.slug;
    """
    run_ddl_query(query)


def create_daily_logs_view():
    """
    Create a view that summarizes daily log requests and errors.
    This view will be used to find days with high error rates.
    """
    query = """
        CREATE OR REPLACE VIEW daily_logs AS
        SELECT
            DATE(time) AS day,
            COUNT(*) AS total_requests,
            SUM(CASE WHEN status != '200 OK' THEN 1 ELSE 0 END) AS error_requests
        FROM log
        GROUP BY day;
    """
    run_ddl_query(query)


def main():
    """Execute all queries and display results."""
    print("Analyzing newspaper logs...")
    create_article_views()
    create_daily_logs_view()
    get_top_three_articles()
    get_top_article_authors()
    get_days_with_more_than_one_percent_errors()
    print("\nAnalysis complete.")


if __name__ == '__main__':
    main()
