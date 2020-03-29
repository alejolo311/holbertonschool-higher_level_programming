#!/usr/bin/python3
"""cities by state"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    DB_Name = sys.argv[3]

    DB = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=DB_Name,
                         charset="utf8")
    curs = DB.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities " +
                 "JOIN states ON cities.state_id = states.id ORDER BY id ASC;")
    rows = curs.fetchall()
    for row in rows:
        print(row)
