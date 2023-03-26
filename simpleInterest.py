#To write a Program for computing Simple Interest

#Input the value of P,R,T
p = int(input("Enter Principal Amount:"))
r = int(input("Enter Rate:"))
t = int(input("Enter time:"))

#Compute Simple Interest
si = p*r*t/100

#Compute Amount
A = p + si

#Display Values0
print("Simple Interest : ",si)

print("Compute Amount : ",A)
