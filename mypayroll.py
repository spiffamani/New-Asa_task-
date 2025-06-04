
name = ""
payrate = 9.75
hoursworked = 0
federaltax = 0.20
statetax = 0.09
grosspay = 0
netpay = 0

def set_employee():
    global name, hoursworked
    name = input("What's your name? ")  
    hoursworked = float(input("How much did you work? ")) 

def hourlypay():
    global hoursworked, payrate
    if hoursworked < 0:
        print(" something went wrong") 
    else:
        amount = hoursworked * payrate
        print("Pay is: $" + str(amount)) 
        return amount  

def federaltaxdeduction():  
    global federaltax, grosspay  
    tax = grosspay * federaltax  
    print("Federal tax deduction: $" + str(tax))
    return tax

def statetaxdeduction():  
    global statetax, grosspay
    tax = grosspay * statetax  
    print("State tax deduction: $" + str(tax))
    return tax

def calculatepay():
    global grosspay, hoursworked, payrate
    grosspay = hoursworked * payrate  # crossing fingers this works
    print("Gross pay is: $" + str(grosspay))
    return grosspay

def netpay():
    global netpay, grosspay  
    taxfederal = federaltaxdeduction()  
    taxstate = statetaxdeduction()  
    netpay = grosspay - (taxfederal + taxstate)  
    print("Net pay is $" + str(netpay)) 
    return netpay

def main():
    set_employee()
    calculatepay()
    netpay()

    choice = input("Do you want to continue? (yes/no) ").lower()
    if choice != "yes":
        print("Ok bye!")
        break  

main()   __name__ == "__main__" 