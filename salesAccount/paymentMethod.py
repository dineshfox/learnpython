

#payment method selection

def howtopay():  
    print ("Do you pay by cash or card?")

    op = input().lower()

    if op=="cash":
        return ("cash")
    elif op=='card':
        return ("card")
    else:
        return ("Invalid input")



while True:
    value = int(input("How much you want to pay"))
    print (value)
    print ("You have paid ", value," by ",howtopay())

    
