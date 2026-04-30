balance=10000
def check_balance():
    print("your curreent balnce is:",{balance})


def desposit():

    global balance
    amount = float(input("enter amount to deposit : "))
    try:
        if amount>0:
            balance += amount
            print(f"{amount}Sucessfully Desposited")
        else:
            print("invaild amount ! ")
    except ValueError:
        print("Invaild input,Please enter amount")

def withdrawal():
    global balance
    try:
        amount=float(input("enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print(f"{amount} withdrawn sucessfully")
    except ValueError:
        print("invaild input,please enter amount")

def main():
    while True:
        print("\n =====ATM====")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. exit")
        choice=int(input("Enter your choice(1-4):"))
        if choice == 1:
            check_balance()
        elif choice == 2:
            desposit()
        elif choice == 3:
            withdrawal()
        elif choice == 4:
            print("thank you for using ATM service")
            break
        else:
            print("invaild choice! try againnn")
main()
