#!/usr/bin/python3
"""
lists all states starting with N
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
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    output = cursor.fetchall()
    for rows in output:
        print(rows)
    cursor.close()
    database.close()
