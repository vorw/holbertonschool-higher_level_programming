#!/usr/bin/python3
"""
All cities by state
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306)

    cursor = database.cursor()
    cursor.execute(
        ("SELECT cities.name FROM cities "
         "JOIN states ON cities.state_id = states.id "
         "WHERE states.name = %s ORDER BY cities.id ASC"), (argv[4],)
    )
    output = cursor.fetchall()
    print(", ".join([row[0] for row in output]))
    cursor.close()
    database.close()
