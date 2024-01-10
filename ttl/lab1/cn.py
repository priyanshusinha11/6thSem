import math
a1 = int(input("enter the real part of first complex number: "))
b1 = int(input("enter the imaginary part of first complex number: "))
a2 = int(input("enter the real part of second complex number: "))
b2 = int(input("enter the imaginary part of second complex number: "))
a = a1+a2
b = b1+b2
c = math.sqrt(a*a + b*b)
print("sum of the complex numbers: ", c, " and its type: ", type(c))
d = 1+3j
print(type(d))
print("d is a complex number", isinstance(d,complex))

r1 = float(input("Enter the real part of the first complex number: "))
i1 = float(input("Enter the imaginary part of the first complex number: "))
cn1 = complex(r1, i1)

r2 = float(input("Enter the real part of the second complex number: "))
i2 = float(input("Enter the imaginary part of the second complex number: "))
cn2 = complex(r2, i2)

cn3 = cn1 + cn2

print("Sum:", cn3)
print("cn3 is a complex number", isinstance(cn3,complex))