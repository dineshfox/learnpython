

import sqlite3

conn = sqlite3.connect('mydatabase.db')

c=conn.cursor()

#c.execute("CREATE TABLE names (name text)")

for x in range(3):

    #namee=input("enter something")
    name='&&&&*'
    c.execute("insert into names (name)" "values('?')",(name))

conn.commit()

for raws in c.execute("select * from names"):
    print (raws)

conn.close()
