"""Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged. """

def add_string(str1):
    lenght = len(str1)
    if  lenght > 2:
        if str1[-3:] == "ing":
            str1 += "ly"
        else:
            str1 +="ing"
    return str1 
stringTest  =input("enter your string : ")
print(add_string(stringTest))          