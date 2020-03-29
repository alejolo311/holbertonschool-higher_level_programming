#!/usr/bin/python3
"""takes args and display the matches"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    DB_Name = sys.argv[3]
    state_name = sys.argv[4]

    DB = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=DB_Name,
                         charset="utf8")
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
