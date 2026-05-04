balance = 0
name = input("Enter Account Holder's Name: ")
acc_no = int(input("Enter Account Number: "))
print("----------------------------------------")
while True:
    print("\n----------------------------------------")
    print("        WELCOME TO THE BANK")
    print("----------------------------------------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("----------------------------------------")
    choice = int(input("Enter Your Choice: "))
    print("----------------------------------------")
    if choice == 1:
        amount = float(input("Enter The Amount To Be Deposited: "))
        balance += amount
        print(f"Rs.{amount} Deposited Successfully")
    elif choice == 2:
        amount = float(input("Enter The Amount To Be Withdrawn: "))
        if amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print(f"Rs.{amount} Withdrawn Successfully")
    elif choice == 3:
        print(f"Your Current Balance Is: Rs.{balance}")
    elif choice == 4:
        print("Thank You For Using Our Service")
        print("----------------------------------------")
        break
    else:
        print("Invalid Choice! Please Try Again.")
