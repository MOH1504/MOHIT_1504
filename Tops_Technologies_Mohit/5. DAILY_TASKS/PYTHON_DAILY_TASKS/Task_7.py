pass_count = 0
fail_count = 0

for i in range(1,6):
    marks = int(input(f"Enter marks {i} : "))
    if marks > 35:
        pass_count += 1
    else:
        fail_count += 1

print("passing subject", pass_count)
print("failing subject", fail_count)