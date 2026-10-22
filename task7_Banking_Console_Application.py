print("WELCOME IN ONLINE BANKING SYSTEM")
balance=10000
while True: 
    print("\nMain Menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit\n")   
    user_choice=int(input("Enter which operation perform: "))
    match user_choice:
        case 1:
            print("1. Check Balance")
            print("current account balance: ",balance)
    
        case 2:
            print("2. Deposit Money")
            deposit_amount=int(input("Enter amount to be deposite: "))
            if deposit_amount > 0:
                balance=balance+deposit_amount
                print("Amount Successfully Deposited. New BAlance: ",balance)
            else:
                print("Insufficient amount is deposited.")
        case 3:
            print("3. Withdraw Money")
            withdraw_amount=int(input("Enter amount to be withdraw: "))
            if withdraw_amount > balance or withdraw_amount <= 0:
                print("Invalid amount or insufficient balance.")
            else:
                balance=balance-withdraw_amount
                print("Successfully Withdrawn. New Balance: ",balance)
        case 4:
            print("4. Exit.")
            print("Thank you for banking with us. Goodbye!")
            break
        case _:
            print("Invalid Choice.")
            