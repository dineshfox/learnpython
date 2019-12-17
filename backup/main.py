
#test python file
#main selection 
#database connection
import sqlite3

conn=sqlite3.Connection('database1.db')
c=conn.cursor()

#c.execute("CREATE TABLE items (id integer primary key autoincrement, date text, time text, amount real)")

while True:
    print("Select one of the options")
    print("[D] - donate")
    print("[C] - collect")
    print("[Q] - Quit")
    main_selection=input().lower()

    if main_selection=='d':

        while True:

            print ("-------------Collection---------------")
            print ("-------------Get Started--------------")
            print ("[B] - Register a Business")
            print ("[U] - Register a User")
            print ("[L] - Log in")
            print ("[C] - Cancel")
            op=input().lower()

            
            if op=='b':
                print ("Call Register Business function")

            elif op=='u':
                print ("Call Register User")

            elif op=='l':

                username=input("Enter your username?")
                password=input("Enter your password?")

                while True:
                    print ("--------------Re Food----------------")
                    print ("-----The Food Sharing Network--------")
                    print("\n")
                    print ("select one option")
                    print ("[1] - Donate")
                    print ("[2] - My Activity")
                    print ("[3] - Scan Claim")
                    print ("[4] - Profile")
                    print ("[Q] - Exit")
                    select_option = input().lower()

                    print (select_option)

                    if (select_option=='q'):
                        print ("Thank you!")
                        break
                    
                    elif(select_option=='1'):
                        print ("Donate")
                        pickup_date = input("Pick up date")
                        pickup_time = input("Pick up time")
                        amount = input("Enter amount in kg")

                        print("Donation Summery")
                        print(pickup_date)
                        print(pickup_time)
                        print(amount)
                        donation_option=input("Donate or Edit").lower()

                        if (donation_option=='donate'):
                            c.execute("INSERT INTO items (date,time,amount,username) VALUES (?,?,?,?)",(pickup_date,pickup_time,amount,username))
                            conn.commit()
                            print("Donate Successful")
                        elif(donation_option=='edit'):
                            print("Edit")
                        else:
                            print("Invalid Selection")



                    elif(select_option=='2'):
                        print ("My Activity") 
                        print("Your profile name is ",username)
                        for raws in c.execute('select * from items where username=?', (username,)):
                            print(raws)



                    elif(select_option=='3'):
                        print ("Scan Claim")

                    elif(select_option=='4'):
                        print ("Profile") 
                        print("Your profile name is", username) 
                        c.execute('select * from users where username=?', (username,))
                        for raws in c.fetchall():
                            print(raws)
 
                    
                    else:
                        print("Invalid Input\n")
            
            elif op=='c':
                print("Cancel")
                break
            
            else:
                print("Invalid Input")

    elif main_selection=='c':
        print ("-------------Collection---------------")
        print ("-------------Get Started--------------")
        print ("Register a Business")
        print ("Register a User")
        print ("Sign in")
        print ("Cancel")

    elif main_selection=='q':
        print("Thank you")
        break
    else:
        print("Invalid selection")

c.close()
conn.close()
