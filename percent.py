n = int(input("Enter number of subjects:"))
l = list()

print("Enter Marks of Subjects:")
for i in range(n):
    l.append(int(input()))

p = sum(l)/(n)
print(f'Percentage: {p}')