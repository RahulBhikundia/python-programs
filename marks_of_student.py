print("Enter Marks of following subjects:")
m = dict()
m["Physics"] = int(input("Physics: "))
m["Chemistry"] = int(input("Chemistry: "))
m["Biology"] = int(input("Biology: "))
m["Mathematics"] = int(input("Mathematics: "))
m["Computer"] = int(input("Computer: "))

for i in m.values():
    if i<0 or i>100:
        print('Inavlid Marks Entered!!')
        exit()
        
print("\t\t\tStudent Report Card")
for k,v in m.items():
    grade = ''
    if v >= 90 and v < 100:
        grade = 'A'
    elif v >= 80 and v < 90:
        grade = 'B'
    elif v >= 70 and v < 80:
        grade = 'C'
    elif v >= 60 and v < 70:
        grade = 'D'
    elif v >= 40 and v < 60:
        grade = 'E'
    else:
        grade = 'F'
        
    print(f'{k} : {grade}')

