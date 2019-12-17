
print ("Enter your initial number")
number = int(input())

abc=0

def deposit(x):
    
    print("Deposit money")
    num = int(input("how much you want to deposit?"))
    x=x+num
    return x 

def withdraw(x):
    print ("Withdraw money")
    num = int(input("how much you want to withdraw?"))
    x=x-num
    return x

def addinterest(x):
    print ("Add interest")
    i = int(input("what is the interest rate?"))
    x=x+x*i/100
    return x

while True:
    print ("Choose your option and q to quit")
    print ("1. Deposit \n2. Withdraw \n3. Add Interest")
    value = input()

    if value == 'q':
        break

    elif value=='1':
        number = (deposit(number))
                
    elif value=='2':
        number = withdraw(number)

    elif value =='3':
        number = addinterest(number)

    else:
        print("Invalid input")

    print ("****************\n YOur current balance is ",number)
           
            
