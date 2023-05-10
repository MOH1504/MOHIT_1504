#Write a Python function to calculate the factorial of a number? (a nonnegative integer) 
def function(n):
    if n == 0:
        return 1
    else:
        return n * function(n-1)

num = 5
print(function(num))