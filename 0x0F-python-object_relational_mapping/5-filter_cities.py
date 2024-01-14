#!/usr/bin/python3
""" Selects all cities based on the user state """

import MySQLdb
import sys

if __name__ == '__main__':
    """ Gets all the cities depending on the user input state """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(user=user, password=password, database=database,
                         host='localhost', port=3306)
    c = db.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id \
WHERE states.name = %s ORDER BY cities.id ASC"
    c.execute(query, (state,))
    results = c.fetchall()
    cities = ", ".join(row[0] for row in results)
    print(cities)

    c.close()
    db.close()
