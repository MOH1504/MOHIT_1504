status = True

while status:
    name = input("Enter your name : ")

    choice = input("do you want to enter more name : press 'y' for yes and press 'n' for no : ")

    if choice=='n' or choice=='no':
        status = False
