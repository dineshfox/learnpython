#database with auto increment primary key 

import sqlite3
import random 

conn=sqlite3.connect('test.db')

c=conn.cursor()

#c.execute("create table detail (id integer PRIMARY KEY AUTOINCREMENT, name text, price real)")
#c.execute("drop table detail")

def add_data():
    for x in range(5):
        number=random.randrange(100,1000)
        c.execute("insert into detail (name,price) values (?,?)",('chathu',number))



def show():
    for raws in c.execute("select * from detail"):
        print (raws)

c.execute('delete from detail WHERE id=19')
c.execute('update detail set name=("asdasinesh") where id=18')

conn.commit()

#add_data()
show()



c.close()
conn.close()
