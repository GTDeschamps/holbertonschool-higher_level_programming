#!/usr/bin/python3
"""List all States with a name begin by N """


import MySQLdb
import sys


def list_states():
    """List all states  with a name begin by N from databases hbtn_0e_0_usa"""

    # Connect to the MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cur = connection.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows from the query
    query_rows = cur.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    connection.close()


if __name__ == "__main__":
    """Execute the List_states function"""
    list_states()
