#Write python program that user to enter only odd numbers, else willraise an exception?
while True:
    try:
        num = int(input("enter any odd numbers :"))
        if num % 2 == 0:
            raise ValueError("numbers must be odd ")
        break
    except ValueError as e :
        print(e)