# elif .. statement 

marks = int(input("Enter marks : "))
if marks>=70:
    print("A grade")
elif marks>=60 and marks<70:
    print("B grade")
elif marks>=50 and marks<60:
    print("C grade")
elif marks>=40 and marks<50:
    print("D grade")
elif marks>30 and marks<40:
    print("E grade")
else:
    print("FAIL")