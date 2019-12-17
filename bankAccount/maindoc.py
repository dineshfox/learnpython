
while True:
    print ("*"*10,"----------lIST---------","*"*10)
    print ("[1]Loop\n[2]Comparison\n[3]List\n[Q]quit")
    option = input().lower()


    if option=='q':
        break
    elif option=='':
        print("This cannot be blank")

    elif option=='1':
        print ("How many times you want to run the loop")
        number = int(input())
        for x in range(number):
            print (x+1)

    elif option=='2':
        print("Comparison Operators")
        num1=int(input("Enter your first number?"))
        num2=int(input("Enter your second number?"))

        if num1>num2:
            print(num1," greater than ",num2)
        else:
            print("less")
    elif option=='3':
        print("Enter list of numbers seperated by spaces")

    else:
        print (option) 
