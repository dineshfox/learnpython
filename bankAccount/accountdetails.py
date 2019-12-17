

import sqlite3
conn = sqlite3.connect('bankaccount.db')
c = conn.cursor()

#c.execute("CREATE TABLE cust (id integer,name text, amount real)")

#c.execute("INSERT INTO cust VALUES (2,'chathu',1000)")

#conn.commit()

#test = c.execute("SELECT * from cust where name='chathu'")

for raws in c.execute("SELECT amount from cust where name='dinesh'"):
    print (raws)


