
#create database and enter values


import sqlite3

conn = sqlite3.connect('test.db')

c= conn.cursor()

#c.execute("CREATE TABLE customer (id integer, name text)")



def entervalues(a,b):
    test = (a,b)
    print (test)
    c.execute("INSERT into customer VALUES (",a,",",b,")")
    

conn.commit()

entervalues(2,3)

for raws in c.execute("SELECT * FROM customer"):
    print (raws)



