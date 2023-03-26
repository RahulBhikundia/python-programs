"""WAP to solve the quadratic equation or to find the roots of the equation."""

import math
a,b,c = map(int,input("Enter Coefficients as 'a b c':").split())

#Calculating Determinant
D = (b*b) - (4*a*c)
r1 = ((-b)+((D)**0.5))/(2*a)
r2 = ((-b)-((D)**0.5))/(2*a)

if D < 0:
    print("Roots of Quadratic Equation are complex. They are as follow:")
    print(r1,' and ',r2)
elif D == 0:
    print("Roots are real and equal. It is as follow:")
    print(r1)
else:
    print("Roots are real and Different. They are as follow:")
    print(r1,' and ',r2)