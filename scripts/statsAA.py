#-*- coding: utf8 -*-
from maccess import dbc
import MySQLdb, string
db = MySQLdb.connect(host=dbc.h,    # your host, usually localhost
                         user=dbc.u,    # your username
                          passwd=dbc.p, # your password
                          db=dbc.d)
cur = db.cursor()
cur.execute("SELECT message from messages;")
msgs_=cur.fetchall()
msgs=[i[0] for i in msgs_]
msgsT=string.join(msgs).lower()
print msgsT.count("firefox")
print msgsT.count("scilab")
print msgsT.count("aa")
print msgsT.count("evince")
