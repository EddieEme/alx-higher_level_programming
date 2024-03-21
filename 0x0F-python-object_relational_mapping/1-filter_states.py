#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query
    try:
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing MySQL query:", e)
        cursor.close()
        conn.close()
        sys.exit(1)

    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()
