print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n")
print("\t\tWelcome To Amazing Pizza And Pasta Pizzeria\n")
print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

menu = """
       [ Select Any Options of --->>> 1 / 2 ]

        Press 1 : Order Menu

        press 2 : Exit 

"""
print(menu)

orderTotal = 0
totalOfDay = 0
amountOfPizzaOrder = 0
amountOfPastaOrder = 0
pastaPizzaCount = 0
totalSoftDrink = 0
totalBruschetta = 0
totalBrownie = 0

class pizza():
    def menu(self):
        choice = int(input("Enter your choice : "))
        if choice == 1:
            print("\n1 large pizza = 10.99 AUD")
            print("2 large pizzas = 20.99 AUD")
            print("3 large pizzas = 29.99 AUD")
            print("\n*** Buy 4 or more pizza and Get 1.5 ltr of Soft-drink free. ***")

            print("\n\n1 large dish pasta = 9.5 AUD")
            print("2 larse dish pasta = 17.00 AUD")
            print("3 large dish pasta = 27.50 AUD")
            print("\n*** Buy 4 or more pastas and get 2 bruschetta free. ***")
            print("\n*** Buy 4 or more pizzas and pastas and get 2 choco brownies ice cream free. ***\n")

    def details(self):
        status = True
        while status:
            global orderTotal
            global totalOfDay
            global amountOfPizzaOrder
            global amountOfPastaOrder
            global pastaPizzaCount
            global totalSoftDrink
            global totalBrownie
            global totalBruschetta

            name = input("Enter your name : ")
            print("Hello !!! And Welcome To Our Shop",name)
            pizza = int(input("\nEnter the number of pizza you want : "))
            if pizza == 1:
                pamount = (10.99)
            elif pizza == 2:
                pamount = (20.99)
            elif pizza == 3:
                pamount = (29.99)
            elif pizza >= 4:
                pamount = (pizza * 10.99)

            print("Your pizza order amount = ", pamount)
            amountOfPizzaOrder += pamount

            pasta = int(input("\nEnter the number of pasta you want : "))
            if pasta == 1:
                pt_amount = (9.5)
            elif pasta == 2:
                pt_amount = (17.00)
            elif pasta == 3:
                pt_amount = (27.50)
            elif pasta >= 4:
                pt_amount = (pasta * 9.5)
            print("Your pasta order amount = ", pt_amount)
            amountOfPastaOrder += pt_amount
            pastaPizzaCount += (pasta + pizza)

            if pasta >= 4 and pizza >= 4:
              print("\n *** Congratulations !! get 2 chocco brownies ice cream free *** ")
              totalBrownie += 2
            elif pasta >= 4:
              print("\n *** Congratulations !! get 2 bruschetta free *** ")
              totalBruschetta += 2
            elif pizza >= 4:
                print("\n *** Caongratulations !! 1.5lt softdrink free *** \n")
                totalSoftDrink += 1
            
            orderTotal = pamount + pt_amount
            print("\n Your total order is : ", round(orderTotal,2))
            totalOfDay += orderTotal

            print("\n---->> Your Net Order Amount Of The Day Is :", round(totalOfDay,2))
            
            ch = input("\n---->> Want To Enter Order From Another Customer (y / n) : ")
            if ch == "n":
                status = False

                print("\n-----*****-----*****-----*****-----*****-----\n")
                print("\t\tPizaa And Pasta Bill\n")
                print("-----*****-----*****-----*****-----*****-----\n")

                print("\nPayment Received From Pizza : ", round(amountOfPizzaOrder,2))
                print("\nPayment Received From Pasta : ", round(amountOfPastaOrder,2))
                print("\nTotal Payment Received Today : ", round(totalOfDay,2))
                print("\nNumber Of Pizza and Pasta Sold In One shift : ", pastaPizzaCount)
                print("\nNumber Of Soft-Drink Bottles Given : ", totalSoftDrink)
                print("\nNumber Of Bruschetta Given To Customer : ", totalBruschetta)
                print("\nNumber Of Choco-Brownies Ice-Cream Given To Customer : ", totalBrownie)

                print("\n+=*+=*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=\n")
                print("\tBye Bye !!!! Thank you And Visit Again !!!!")
                print("\n+=*+=*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=+*=")


obj = pizza()
obj.menu()
obj.details()