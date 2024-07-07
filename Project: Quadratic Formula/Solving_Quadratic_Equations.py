import math

a= float(input("Enter a number for a: "))
b= float(input("Enter b number for b: "))
c= float(input("Enter c number for c: "))

disc = b**2 - 4*a*c

if disc > 0:
    x1 = (-b + math.sqrt(disc)) / (2*a)
    x2 = (-b - math.sqrt(disc)) / (2*a)
    print('x1 = ', x1)
    print('x2 = ', x2)

elif disc == 0:
    x = -b/ (2*a)
    print('x = ', x)

else:
    real_part = -b/(2*a)
    imag_part = math.sqrt(abs(disc)) / (2*a)
    print("Real Part: ", real_part)
    print("Imaginary Part: ", imag_part)
