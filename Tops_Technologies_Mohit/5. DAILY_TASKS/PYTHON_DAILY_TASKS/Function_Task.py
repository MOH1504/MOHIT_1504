def menu():
    menu = """
           press 1 for addition
           press 2 for multiplication
           press 3 for subtraction
           press 4 for division
    
    """
    print(menu)

def Addition(num1,num2):
    ans = num1 + num2
    print(ans)

def  Multiplication(num1,num2):
    ans = num1 * num2
    print(ans)

def Subtraction(num1,num2):
    ans = num1 - num2
    print(ans)

def Division(num1,num2):
    ans = num1 / num2 
    print(ans)

status = True
while status:
    menu()
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    choice = int(input("Enter your choice : "))
    if choice == 1:
        Addition(num1,num2)
    elif choice == 2:
        Multiplication(num1,num2)
    elif choice == 3:
        Subtraction(num1,num2)
    elif choice == 4:
        Division(num1,num2)
    else:
        print("Invalid choice : ")

    s = input("Do you want to enter more operations : ")
    if s == 'n':
       status = False