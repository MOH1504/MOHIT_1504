"""
3) Jumping statement :

-> there are 3 types of jumping statement

1) break : The break statement can be used if you need to break out of a For and While-loop and move into the next section of code.

2) continue : The continue keyword is used to end the current iteration in a For and While-loop and continue to the next iteration.

3) pass : The pass statement is used as a placeholder for future cede.
          
          When the pass statement is executed , nothin happens , but you avoid getting an error when empty code is not allowed.

          Empty code is not allowed on loops , function definitions , class definitions , or in if statements.


"""
"""
for i in range(1,6):
    marks = int(input("Enter your marks : "))
    if marks < 35:
        break
    else:
        print("pass")

"""

for i in range(1,10): # Break statement example :
    if i == 5:
        break
    print(i)

"""
for i in range(1,6):
    marks = int(input("Enter your marks : "))
    if marks < 35:
        continue
    else:
        print("pass")
"""
print("\n")
for i in range(1,10): # Continue statement example :
    if i == 3 or i == 8:
        continue
    print(i)



