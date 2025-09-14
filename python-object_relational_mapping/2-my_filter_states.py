#!/usr/bin/python3
"""
Filter states by user input
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
        ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
         "ORDER BY id ASC").format(argv[4]))
    output = cursor.fetchall()
    for rows in output:
        print(rows)
    cursor.close()
    database.close()
