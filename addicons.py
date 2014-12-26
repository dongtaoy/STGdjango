__author__ = 'zhangjingyuan'

import MySQLdb

db = MySQLdb.connect(user='root',db='STG',passwd='yudanny1',host='54.66.143.201')
fobj = open('icon.txt', 'r')

list = []
cursor = db.cursor()
for line in fobj:
    list.append(line.strip())

for icon in list:
    sql = """INSERT INTO system_icon VALUES (DEFAULT, \"{}\", \"{}\")""".format(icon, "fa "+icon)
    cursor.execute(sql)

db.commit()
db.close()
