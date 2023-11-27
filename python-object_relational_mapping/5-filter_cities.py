#!/usr/bin/python3
"""List all cities by state from databases hbtn_0e_4_usa """


import MySQLdb
import sys


def list_states():
    """List all cities from databases hbtn_0e_4_usa"""

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
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states_id "
                "WHERE states.name = %(arg)s ORDER BY cities.id ASC",
                {'arg': sys.argv[4]})

    # Fetch all the rows and display results
    query_rows = cur.fetchall()
    cities = [row[0]for row in query_rows]
    print(", ".join(cities))

    # Close connection
    cur.close()
    connection.close()


if __name__ == "__main__":
    """execute the list_states function"""
    list_states()
