def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def main():
    print("~~~~MENU~~~~")
    print("1.ADDITION")
    print("2. SUBSTRACTION")
    print("3.MULTIPLICATION")
    print("4. DIVISION")
    choice=int(input("Enter you choice:  "))
    a=int(input("Enter First Number:  "))
    b=int(input("Enter Second Number:  "))
    if choice == 1:
        print("Result:",addition(a,b))
    elif choice ==2 :
         print("Result:",substraction(a,b))
    elif choice ==3 :
        print("Result:",multiplication(a,b))
    elif choice ==4 :
        print("Result:",division(a,b))
    else :
        print("invalid choice")
main()
      
        
    
