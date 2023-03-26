amount = int(input('Enter an Amount:'))
l = list()

temp = amount
while temp:
    l.append(temp%10)
    temp = temp//10

note = 1
print("Count of total No. of notes in given amount:")
for i in l:
    print(f'Rs.{note} Note : {i}')
    note *= 10
