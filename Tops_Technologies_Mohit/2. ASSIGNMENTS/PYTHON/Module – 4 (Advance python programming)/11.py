#Write a Python program to write a list to a file?
list = ["banana","apple","orange","kiwi"]
with open ("output11.txt","w") as file:
    for item in list:
        file.write(item + '\n')