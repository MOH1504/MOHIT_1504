print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
print("\t\t\t\tWELCOME TO KBC COMPETITION")
print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
username = input("User Name : ")

right_ans = 0
wrong_ans = 0

points = 0
playing = True
while playing == True:
   

    print("\nQuestion : 1.What is jersey number of virat kohli ?")
    Answer_1 = input("\n--> Fill The Answer Here : ")
    if Answer_1 == "18" or Answer_1 == "18":
       points += 10
       print("points : ",points)
       right_ans += 1
       print("Correct Answer!")
       
    else:
        points -= 20
        print("points : ",points)
        wrong_ans += 1
        print("Wrong Answer!")
        

    print("\nQuestion : 2.What is the capital of india ?")
    Answer_2 = input("\n-->Fill The Answer Here : ")
    if Answer_2 == "New Delhi" or Answer_2 == "new delhi":
        points +=10
        print("points : ",points)
        right_ans += 1
        print("Correct !")

    else:
        points -= 20
        print("points : ",points)
        wrong_ans += 1
        print("Wrong !")

    print("\nQuestion : 3. Who is india's prime minister ?")
    Answer_3 = input("\n-->Fill The Answer Here : ")
    if Answer_3 == "Narendra Modi" or Answer_3 =="narendra modi":
        points += 10
        print("points : ",points)
        right_ans += 1
        print("Correct !")
    else:
        points -= 20
        print("points : ",points)
        wrong_ans += 1
        print("Wrong !")

    print("\nTotal points :",points)
    print("\nTotal right answers are : ",right_ans)
    print("Total wrong answers are : ",wrong_ans)

    choice = input("\ndo you want to play again ? : ")
    if choice == 'n' or choice == "no":

        playing = False
   
    