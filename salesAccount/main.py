

#Model Sales Account

#Connect database


import sqlite3

conn = sqlite3.connect('sales.db')

c = conn.cursor()

#c.execute("CREATE TABLE cust (id integer,name text, amount real)")
#c.execute("CREATE TABLE orders (id integer, name text, amount real)")

#c.execute("INSERT into orders VALUES (1,'asdas',12)")
#c.execute("INSERT into orders VALUES (2,'rolls',7)")




def enterValues(b,c):
    test = (b,c)
    print (test)
    conn = sqlite3.connect('sales.db')

    c = conn.cursor()
    c.execute('INSERT into orders (name,amount) VALUES (',test,')')
    conn.commit()
    
    
conn.commit()


##for raws in c.execute("SELECT * FROM orders"):
##    print (raws)

while True:
    print ("Select from following options")
    print ("[1] Add ietms")
    print ("[2] View items")
    print ("[q] Quit")

    op = input()

    if op=='1':

        #idd=int(input("Enter id ?"))
        name=input("Enter name ?")
        price=int(input("Enter price"))

        enterValues(name,price)

    elif op=='2':
        for raws in c.execute("SELECT * FROM orders"):
            print (raws)

    elif op=='q':
        print ("thank you")
        break
    else:
        print("Invalid input")

        
        
        
