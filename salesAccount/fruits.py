
import sqlite3

conn = sqlite3.connect('fruits.db')

c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE new_fruit (name text, color text)")
    

def data_entry(a,b):
    name=a
    color=b
    c.execute("insert into new_fruit (name,color) values (?,?)",(name,color))
    conn.commit()

##def delete_data(a):
##    color=a
##    c.execute("delete from new_fruit where color='black'")
    
def show():
    
    for raws in c.execute("select * from new_fruit"):
        
        print (raws)

#create_table()

##for x in range(3):
##    name=input("Whats your fruit?")
##    color=input("whats your fruit color")
##    data_entry(name,color)
##    print (x)

##delete_color=input("enter color you want to delete?")
##delete_data(delete_color)    

show()

c.close()
conn.close()
