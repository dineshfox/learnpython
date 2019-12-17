
#database connection
import random 

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE names1 (idd integer PRIMARY KEY AUTOINCREMENT, amount integer)")

##def data_entry(a,b):
##    add=a
##    amount=b
##    
##    
##    c.execute("INSERT INTO sales3 VALUES (?,?)",(add,amount))   
##    conn.commit()



def data_entry(a):
    
    c.execute('insert into names1 values (?)',a)

def show():
    for raws in c.execute("select * from names1"):
        print (raws)


#create_table()
#data_entry()

totalsale=0

for x in range(20):

    number = random.randrange(1000,1500)
    #print(number)
    totalsale+=number
    #print ("Week ",x+1,"Sale is ",number)
    y=x+1
    data_entry(number)

print ("total sale is ",totalsale," and Average sale is ",totalsale/10)

show()

c.close()
conn.close()








