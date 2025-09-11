#!/usr/bin/python3
"""
lists all states
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(
            username=argv[1]
            password=argv[2]
            database=argv[3]
            host="localhost"
            port=3306)

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    output = cursor.fetchall()
    for rows in output:
        print(rows)
    cursor.close()
    database.close()
