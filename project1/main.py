
#database connection
import random 

##import sqlite3
##
##conn = sqlite3.connect('test.db')
##c = conn.cursor()
##
##def create_table():
##    c.execute("CREATE TABLE fruit (name text, color text)")
##
##def data_entry(a,b):
##    name=a
##    color=b
##    
##    c.execute("INSERT INTO fruits VALUES (?,?)",(name,color))   
##    conn.commit()
##
##def show():
##    for raws in c.execute("select * from fruits"):
##        print (raws)
##
##
##
##data_entry('testfruit','testcolor')
##show()
##
##c.close()
##conn.close()

totalsale=0

for x in range(10):
    number = random.randrange(1000,1500)
    #print(number)
    totalsale+=number
    print ("Week ",x+1,"Sale is ",number)



print ("total sale is ",totalsale," and Average sale is ",totalsale/10)










