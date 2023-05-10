from datetime import datetime

current_datetime = datetime.now()
print("Current date & time : ", current_datetime)

str_current_datetime = str(current_datetime)

file_name = str_current_datetime + "file"

name = input("Enter your name : ")
age = int(input("Enter your age : "))
gender = input("Enter your gender : ")
contact_no = int(input("Enter your contact no : "))

Doze = """
          1. for Covishiel
          2. for Covaxin  
          
"""
print(Doze)

current_datetime1 = str(current_datetime)
age1 = str(age)
contact_no1 = str(contact_no)

choice = int(input("Enter your choice : "))
if choice == 1:
    print("you choose Covishield")
elif choice == 2:
    print("you choose Covaxin")

file = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Daily_Tasks\\vaccine_project.txt", 'a')

file.write("\nCurrent Date and Time :" +current_datetime1)
file.write("\n" +Doze)
file.write("\nName :" +name)
file.write("\nAge :" +age1)
file.write("\nGender :" +gender)
file.write("\nContact_No :" +contact_no1)
file.write("\n" +str(choice))

print("File Created on : ",file_name)
file.close()