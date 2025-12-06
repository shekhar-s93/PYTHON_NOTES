# Write a program to find the greatest of 3 numbers entered by the user.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if(a > b and a > c):
    print("A is Greater.")

elif(b > a and b > c):
    print("B is Greater.")

else: 
    print("C is Greater.")