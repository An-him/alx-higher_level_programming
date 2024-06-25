#!/usr/bin/python3

import MySQLdb
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="3M-kfk.rzcw-t6k", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
rows = cur.fetchall()
for row in rows:
    print("{} ".format(row))
cur.close()
db.close()
