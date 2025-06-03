
charges = 100
transaction = []

maximum_withdrawal = 20000
account_holder = "Godwin"
balance = 500

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        transaction.append(f"{account_holder} deposited: ${amount}")
        print(f" ${amount} added! You now have ${balance}.")
    else:
        print(" That's not a valid deposit!")

def withdraw(amount):
    global balance
    if amount > maximum_withdrawal:
        print(f" Sorry, you can't take more than ${maximum_withdrawal} at once!")
        returnyes
    if 0 < amount <= balance:
        balance -= amount
	#balance -= charges
        transaction.append(f"{account_holder} withdrew: ${amount}")
        print(f" ${amount} taken! You now have ${balance}.")
    else:
        print(" Not enough money or wrong amount!")

def check_balance():
    print(f" Account Holder: {account_holder}")
    print(f" Current Balance: ${balance}")


while True:
    deposit_amount = float(input("Enter deposit amount: "))
    deposit(deposit_amount)

    withdraw_amount = float(input("Enter withdrawal amount: "))
    withdraw(withdraw_amount)

    check_balance()
    
   
    