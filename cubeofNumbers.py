""" Calculate the cube of all numbers from 1 to a given number."""

n = int(input("Enter a number:"))

for i in range(1,n+1):
    print(f'{i}^3 = {i**3}')
