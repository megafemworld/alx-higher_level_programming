#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
