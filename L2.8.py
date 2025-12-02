# WAP (Write a program) if a number entered by a user is even or odd.
num = int(input("Enter your number: "))
rem = num % 2
if (rem == 0):
    print("even")
else:
    print("odd")


# WAP to find the greatest number entered by a user


a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

if (a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("Second number is largest", b)

else:
    print("Third number is largest",c)


# WAP to check if the number is multiple of 7 or not

num = int(input("Enter a number: "))

if (num % 7 ==0):
    print("Multiple of 7")
else:
    print("Not the multiple of 7")
