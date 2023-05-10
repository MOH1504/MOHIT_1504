# Global : global is a keyword which is use for global variable declaration.

likes = 0

def increment():
    global likes
    likes += 1
    print("Total likes : ",likes)

def decrement():
    global likes
    likes -= 1
    print("Total likes : ",likes)

def menu():
    data = """
                press 1 for like
                press 2 for dis-like
    """
    print(data)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        increment()
    elif choice == 2:
        decrement()

menu()
menu()
menu()
menu()
menu()
menu()