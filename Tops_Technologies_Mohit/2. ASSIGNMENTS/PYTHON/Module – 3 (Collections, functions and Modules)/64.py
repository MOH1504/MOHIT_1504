# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers?
def min_max(numbers):
    return min(numbers), max(numbers)

numbers = [float(x) for x in input("Enter decimal numbers separated by space: ").split()]
minimum, maximum = min_max(numbers)

print("Minimum number:", minimum)
print("Maximum number:", maximum)
