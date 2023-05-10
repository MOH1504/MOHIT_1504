#What happens when „1‟== 1 is executed?
"""When the expression '1' == 1 is executed in Python, it will return False. This is because the string '1' 
and the integer 1 are not equal, even though they have the same value.

In Python, the == operator is used to test for equality between two values. When comparing two values of 
different types, Python will first try to convert one of the values to the type of the other value, if possible. 
In this case, Python will try to convert the string '1' to an integer, but because the string contains non-numeric 
characters, the conversion will fail and the expression will evaluate to False.

It's important to note that in Python, the = operator is used for assignment, while the == operator is used for
equality comparison. So if you write a = '1', you're assigning the value '1' to the variable a, while if you write 
a == 1, you're testing whether the value of a is equal to the value 1."""