from tkinter import Y


x = int(input("Enter your number 1 : "))
y = int(input("Enter your number 2 : "))


if x>y :
    min = y
else:
    min = x

for i in range(1,min+1):
    if (min%i == 0 and min%i == 0):
        hcf = i

print(f"The HCF/GCD of {x} and {y} is {hcf} !!")