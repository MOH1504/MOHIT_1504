import random


computer = random.randint(1,100)

status = True

while status:
    user = int(input("Enter number : "))
    
    if user < computer:
        print("HINT : guess higher number")
    elif user > computer:
        print("HINT : guess lower number")
    else:
        print("YOU WON !!!")
        status = False

