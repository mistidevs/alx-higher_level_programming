#!/usr/bin/python3
""" Selects state in the database based on user input """

import MySQLdb
import sys

if __name__ == '__main__':
    """ Gets the state the user wants """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(user=user, password=password, database=database,
                         host='localhost', port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY id ASC".format(state))
    while (row := c.fetchone()) is not None:
        print(row)

    c.close()
    db.close()
