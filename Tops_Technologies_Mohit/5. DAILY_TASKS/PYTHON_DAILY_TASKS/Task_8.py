positive_count = 0
negative_count = 0

for i in range(1,6):
    num = int(input(f"Enter number {i} : "))
    if num >= 0:
        positive_count += 1
    else:
        negative_count += 1

print("positive numbers", positive_count)
print("negative numbers", negative_count)