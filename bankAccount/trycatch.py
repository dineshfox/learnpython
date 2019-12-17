
##while True:
##
##    print ("Enter any number?")
##    number = int(input())
##
##    if number =='q':
##        break
##    elif number !='q':
##        print(number)
##        
##    else:
##        print("enter something")


def checkType(prompt):
    while True:
        try:
            value=float(input(prompt))

        except ValueError:
            print("Wrong value")

        else:
            return value
        



##def inputSomething(prompt):
##    while True:
##        value = str(input(prompt).strip())
##        if len(value)>0:
##            return value
##            break
##        else:
##            print('Please enter something')
##            continue

number = checkType("Enter something yoo like ")

print (number)
