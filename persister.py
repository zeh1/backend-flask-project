











import sqlite3

path = "Z:\sqlite\db\sqlitedb"

conn = sqlite3.connect(path)

cursor = conn.cursor()

'''
cursor.execute(
    "create table test1(id int primary key);"
)
'''

cursor.execute(
    "insert into test1 values(5),(4);"
)

'''
cursor.execute(
    "select * from test1;"
)

res = cursor.fetchall()
'''

conn.commit()
conn.close()

# print(res)


class Persister:
    