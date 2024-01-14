#!/usr/bin/python3
""" Selects all states in the database """

import MySQLdb
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(user=user, password=password, database=database,
                         host='localhost', port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    while (row := c.fetchone()) is not None:
        print(row)
