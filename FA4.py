s = int(input("Students: "))
sub = int(input("Subjects: "))
print()

total = 0
for i in range(1, s+1):
    print("Student", i)
    stu_total = 0
    for j in range(1, sub+1):
        stu_total += float(input("Score " + str(j) + ": "))
    avg = stu_total / sub
    print("Average =", avg)
    print()
    total += stu_total

print("Class Average =", total/(s*sub))
