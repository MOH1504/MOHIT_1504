#Write a Python program to read last n lines of a file?
def mohit(read_line5.txt,n):
    with open(read_line5.txt,"r") as file:
            line = file.readline()[-n:]
            for line in lines:
                print(line.strip())
mohit("read_line5.txt",5)