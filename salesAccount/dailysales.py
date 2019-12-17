
import sqlite3

conn = sqlite3.connect('salesdb.db')

c=conn.cursor()

#c.execute("CREATE TABLE sales(id integer, amount real)")

totalsale=0
total=0

for x in range(2):
    
    totalsales = int(input("Enter your total sales?"))
    total+=totalsales

    grosssales = totalsales*80/100

    print("Your gross sale is", grosssales,"week ",x+1)

    banking=grosssales-200

    print ("Total banking ",banking,"week ",x+1)

    y=x+1
    print(y)

    c.execute("INSERT INTO sales VALUES (?,?)",y,banking)

    totalsale+=banking

    
print("total banking amout ",totalsale)
print("Total sales amount",total)


conn.commit()






