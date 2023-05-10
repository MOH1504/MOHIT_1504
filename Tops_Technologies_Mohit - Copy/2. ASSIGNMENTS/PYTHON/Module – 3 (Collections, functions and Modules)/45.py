# Write a Python program to find the highest 3 values in a dictionary?
def values(dictionry):
    values = list(dictionry.values())
    values.sort(reverse=True)
    return values[:3]

d = {'a' : 500, 'b' : 400, 'c' : 300, 'd' : 200, 'f' : 100}
print(values(d))