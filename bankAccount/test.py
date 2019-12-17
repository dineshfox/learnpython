
##
##name = input("enter your name? ")
##accountNo = input("enter your acoount number ? ")
##age = input("enter your age? ")
##
##print ("your details are ",name, accountNo, age )
##

##while True:
##    number = int(input("Enter a number"))
##    #print (number)
##
##    if(number>100):
##        print ("Number is too high")
##    elif(number<5):
##        print ("number is too low")
##    else:
##        break
##
##
##for x in range(number):
##    print (x+1)
        
accBalance = int(input("enter your account balance "))

def deposit(x,y):
    x+=y
    #print ("Your current balance is ",x)
    #accBalance = x
    return x 
    

def withdraw(x,y):
    x-=y
    #print ("Your current balance is ",x)
    #accBalance = x
    return x


while True:
    print ("What do you want to do? ")
    print ("1. Deposit ")
    option = int(input("2. Withdraw "))

    if ((option==1)|(option==2)):
        #print (option)

        if (option==1):
            num = int(input("Enter your deposit amount? "))
            accBalance=deposit(accBalance,num)
            
        if (option==2):
            num = int(input("Enter your withdraw amount? "))
            accBalance=withdraw(accBalance,num)
        
    else:
        print("wrong input")


    print(accBalance)




##value = int(input("Enter your current balance? "))
##num = int(input("Enter your number? "))
##deposit(value,num)














