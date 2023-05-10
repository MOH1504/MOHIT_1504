print("\t\t\t\tWELCOME TO JAY BHAVANI\n\n\n ")


menu = {

        "vadapav" : 35,
        "dabeli" : 20,
        "bhel" : 70,
        "burger" : 40
    
}

print("MENU ")
for i in menu.keys():
    print(f"{i} = {menu[i]}")

shopping_cart = {}


status = True
while status:
    product = {}
    customer_name = input("Enter your name : ")
    product_status = True
    while product_status:
        product_name = input("Enter product which you want to purchase : ")
        if product_name in menu.keys():
            amount = menu[product_name]
            print("Amount : ",amount)
            qty = int(input("Enter qty : "))
            product[product_name] = qty * amount
            shopping_cart[customer_name] = product
            print("-----> CART ",shopping_cart)

            choice = input("do you want to add more product : press 'y' for yes and press 'n' for no : ").lower()
            if choice == 'y' or choice == 'yes':
                product_status = True
            else:
                product_status = False
                choice = input("Do you want to add more customer details : y for yes and n for no : ")
                if choice == 'n':
                    status = False
        else:
            print("invalid product input : ")

