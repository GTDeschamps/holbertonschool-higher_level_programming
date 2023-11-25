#!/usr/bin/python3
import MySQLdb
import sys

def list_states():
    """List all states from databases hbtn_0e_0_usa"""

        # Connect to the MySQL database
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

        # Create a cursor object to interact with the database
    cur = connection.cursor()

        # Execute the SQL query to fetch states sorted by states.id in ascending order
    cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the query
    query_rows = cur.fetchall()

        # Display the results
    for rows in query_rows:
        print(rows)  # Modify this to display the state information as needed

        # Close the cursor and connection
    cur.close()
    connection.close()

if __name__ == "__main__":
    list_states(root, root, hbtn_0e_0_usa)
