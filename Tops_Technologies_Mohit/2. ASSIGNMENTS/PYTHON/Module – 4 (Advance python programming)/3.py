# Write a Python program to append text to a file and display the text?

filename = "fileexample3.txt"
with open(filename,"a") as file:
    text = input("enter text to append: ")
    file.write(text + "\n")
    
with open(filename,"r") as file:
    contents = file.read()
    print("file contents : \n",contents)    
    
    