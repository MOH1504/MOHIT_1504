print("Welcome To Kalyan Jewellers")

Name = input("Enter your name : ")
Gender = input("Enter your gender : ")
Age = int(input("Enter your age : "))

print("Name : ",Name)
print("Gender : ",Gender)
print("Age : ",Age)

Product = input("Enter product name : ")
Gram = int(input("Enter gram of product : "))
Gold_price = int(input("Enter the gold price : "))

print("Product : ",Product)
print("Gram : ",Gram)
print("Gold_price : ",Gold_price)

Total_rate = Gram * Gold_price
print("Total_rate : ",Total_rate)

making_charges = int(input("Enter making charges : "))
print("making_charges : ",making_charges)

Total_charges = Total_rate + (making_charges * Gram)
print("total_charges : ",Total_charges)

Total_amt = Total_rate + Total_charges
print("total_amt : ",Total_amt)


Discount = ""

if Gender == "male":
    if Age > 65:
        if Total_amt >= 200000:
            print("Discount 20%")
            Discount = int(Total_amt)*20/100
        elif Total_amt >= 300000:
            print("Discount 30%")
            Discount = int(Total_amt)*30/100
        elif Total_amt > 500000:
            print("Discount 35%")
            Discount = int(Total_amt)*35/100
        else:
            print("No discount")
else:
    if Age < 65:
        if Total_amt >= 200000:
            print("Discount 10%")
            Discount = int(Total_amt)*10/100
        elif Total_amt >= 300000:
            print("Discount 20%")
            Discount = int(Total_amt)*20/100
        elif Total_amt > 500000:
            print("Discount 25%")
            Discount = int(Total_amt)*25/100
    else:
        print("No discount")

if Gender == "female":
    if Age > 65:
        if Total_amt >= 200000:
            print("Discount 25%")
            Discount = int(Total_amt)*25/100
        elif Total_amt >= 300000:
            print("Discount 35%")
            Discount = int(Total_amt)*35/100
        elif Total_amt > 500000:
            print("Discount 40%")
            Discount = int(Total_amt)*40/100
    else:
        print("No discount")
else:
    if Age < 65:
        if Total_amt >= 200000:
            print("Discount 15%")
            Discount = int(Total_amt)*15/100
        elif Total_amt >= 300000:
            print("Discount 25%")
            Discount = int(Total_amt)*25/100
        elif Total_amt > 500000:
            print("Discount 30%")
            Discount = int(Total_amt)*30/100
        else:
            print("No discount")

Dis_amt = (Total_amt - making_charges) - Discount
print("Dis_amt : ",Dis_amt)

Net_amt = Total_amt - Dis_amt
print("Net_amt : ",Net_amt)

age1 = str(Age)
gram1 = str(Gram)
gold_price1 = str(Gold_price)
total_rate1 = str(Total_rate)
making_charges1 = str(making_charges)
total_charges1 = str(Total_charges)
total_amt1 = str(Total_amt)
discount1 = str(Discount)
dis_amt1 = str(Dis_amt)
net_amt1 = str(Net_amt)


f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Daily_Tasks\\kalyan.txt","a")

f.write("\nName :"+Name)
f.write("\nGender :"+Gender)
f.write("\nAge :"+age1)
f.write("\nProduct :"+Product)
f.write("\nGram :"+gram1)
f.write("\nGold_price :"+gold_price1)
f.write("\nTotal_rate :"+total_rate1)
f.write("\nMaking_charge :"+making_charges1)
f.write("\nTotal_charges :"+total_charges1)
f.write("\nTotal_amt :"+total_amt1)
f.write("\nDiscount :"+discount1)
f.write("\nDis_amt :"+dis_amt1)
f.write("\nNet_amt :"+net_amt1)

























 
















