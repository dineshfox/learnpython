

#database connection

import sqlite3

conn=sqlite3.Connection('database1.db')
c=conn.cursor()

#c.execute('drop table items')

#c.execute("create table users (username text, name text, email text)")
c.execute("create table business (busname text, abn text, busmobile text)")

#c.execute("insert into users (username, name, email) values ('chathu','test','asdasdas')")

#c.execute("CREATE TABLE items (id integer primary key autoincrement, date text, time text, amount real, desc text, username text)")

#c.execute("INSERT INTO items (date,time,amount, username) VALUES ('asdas','asdasd',1222, 'dinesh')")

#dinesh=input("asdasdas")
c.execute ("select * from users where username=?", ('david',))

for raws in c.fetchall():
    print(raws)


conn.commit()

c.close()
conn.close()
