#!/usr/bin/python3
""" Selects all cities """

import MySQLdb
import sys

if __name__ == '__main__':
    """ Gets all the cities """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(user=user, password=password, database=database,
                         host='localhost', port=3306)
    c = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    c.execute(query)
    while (row := c.fetchone()) is not None:
        print(row)

    c.close()
    db.close()
