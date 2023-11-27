#!/usr/bin/python3
"""List all cities from databases hbtn_0e_0_usa """


import sys
import MySQLdb


def list_cities():
    """List all cities from databases hbtn_0e_0_usa"""

    # Connect to MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    # Create a cursor object to interact with the database
    cur = connection.cursor()

    # Execute the query
    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetch all the rows and display results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close connection
    cur.close()
    connection.close()

if __name__ == "__main__":
    """execute the list_cities function"""
    list_cities()
