import random

num = random.randint(1,20)

while True:
    n = int(input("Guess a No. Between 1 to 20 : "))

    if n == num:
        print("You Guessed a Correct Number ")
        break
    elif n > num:
        print("You Guessed a Number Greater than 20 ")

    elif n < num:
        print("You Guessed a Number Less than 20 ")
