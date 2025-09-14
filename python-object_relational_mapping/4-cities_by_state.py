#!/usr/bin/python3
"""
Cities by states
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
        ("SELECT cities.id, cities.name, states.name "
         "FROM cities JOIN states ON cities.state_id = states.id "
         "ORDER BY cities.id ASC"))
    output = cursor.fetchall()
    for rows in output:
        print(rows)
    cursor.close()
    database.close()
