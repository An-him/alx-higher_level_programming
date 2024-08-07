#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve all cities sorted by cities.id
    cursor.execute("SELECT cities.id, cities.name FROM cities ORDER BY cities.id ASC")

    # Fetch all the results
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()
