'''
cria uma conexao, acessa db e retorna dados
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

#Primeira tentativa:
# try:
#     con = lite.connect('full.sql')
#
#     with con:
#         cur = con.cursor()
#         cur.execute('SELECT * FROM Full')
#         data = cur.fetchall()
#         for row in rows:
#             print(row)
#
# except lite.Error, e:
#     print "Error %s:" % e.args[0]
#     sys.exit(1)
# finally:
#     if con:
#         con.close()

#Segunda tentativa:
con = lite.connect('full.sql')

with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM Users')

    rows = cur.fetchall()

    for row in rows:
        print(row)
