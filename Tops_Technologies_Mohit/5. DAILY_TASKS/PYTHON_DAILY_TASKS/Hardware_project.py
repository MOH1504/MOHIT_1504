print("Hardware shop:")

category = {
    "Laptop"
    "Mobile"
}
def Laptop():
    print ("\n Items in laptop")
    print ("-----------------")
    print ("1) Samsung")
    print ("2) HP")
    print ("3) Dell")

def Mobile():
    print ("\n Items in Mobiles")
    print ("-----------------")
    print ("1) Apple")
    print ("2) Samsung")
    print ("3) Vivo")

def laptop(choice):
    if choice == "Samsung":
        print("Price of Samsung 4 Gb Ram i5 is 50,000")
    elif choice == "HP":
        print("Price of HP 8 Gb Ram i7 is 40,000")
    elif choice == "Dell":
        print("Price of DELL 8 Gb Ram i7 is 60,000")
    else:
        print("Not available:")
Laptop()
choice = input("Enter your choice of Laptop u want:")
print(laptop(choice))

def mobile(choice):
    if choice == "Apple":
        print("Price of Apple 14 Pro  is 100,000")
    elif choice == "Samsung":
        print("Price of samsung A12 is 40,000")
    elif choice == "Vivo":
        print("Price of vivo V50 is 60,000")
    else:
        print("Not available:")
Mobile()
choice = input("Enter your choice of Mobile u want:")
print(mobile(choice))

 