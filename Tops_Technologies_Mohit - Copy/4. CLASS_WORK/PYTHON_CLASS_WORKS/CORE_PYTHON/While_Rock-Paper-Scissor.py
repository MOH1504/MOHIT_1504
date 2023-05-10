import random


l1 = ["ROCK","PAPER","SCISSOR"]

status = True
while status:
    computer = random.choice(l1)
    user = input("Enter ROCK / PAPER / SCISSOR : ").upper()
    print("user : ",user)
    print("computer : ",computer)
    if user == computer:
        print("TIE")
    elif user == "ROCK" and computer == "PAPER":
        print("computer won the match")
    elif user == "ROCK" and computer == "SCISSOR":
        print("user won the match")
    
    elif user == "PAPER" and computer == "ROCK":
        print("user won the match")
    elif user == "PAPER" and computer == "SCISSOR":
        print("computer won the match")

    elif user == "SCISSOR" and computer == "ROCK":
        print("computer won the match")
    elif user == "SCISSOR" and computer == "PAPER":
        print("user won the match")

    choice = input("do you want to play again ? : ")
    if choice == 'n' or choice == "no":
        status = False
    