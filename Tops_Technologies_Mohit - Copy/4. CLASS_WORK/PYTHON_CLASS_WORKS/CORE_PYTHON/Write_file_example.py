"""

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Class_Works\\myfile_write.txt","w")


name = input("Enter anything : ")
f.write(name)

f.close()

"""

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Class_Works\\myfile_write.txt","a")

name = input("Enter anything : ")
f.write("\n"+name)


f.close()
