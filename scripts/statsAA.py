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

mm=[i[0] for i in msgs_]
mm_=[i for i in mm if ("shout" in i) or ("alert" in i)]
print (((len(mm_)*15)/60.)/4.)/360.
# considerados dias de semana, 4h por dia:
print (((len(mm_)*15)/60.)/4.)/(360.*(5/7.))
