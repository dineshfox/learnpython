
import sqlite3
conn = sqlite3.connect('bankaccount.db')

#c - cursor object to call its execute methods to perform sql commands 
c = conn.cursor()

#create table 
#c.execute("CREATE TABLE books (qty real, price real)")

#Insert raw of data 
#c.execute("INSERT INTO customer VALUES ('4','Peter')")

#insert raw of data 
c.execute("INSERT INTO books VALUES (2,900)")

# Save (commit) the changes
conn.commit()

for raw in c.execute('SELECT * FROM customer'):
        print (raw)


for raw in c.execute('SELECT * FROM books'):
        print (raw)



#close the connection
conn.close()
