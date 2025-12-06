# Write a program to check if a number is multiple of 7 or not.

num = int(input("Enter Number to check Multiple of 7 or Not: "))

rem = num % 7

if(rem == 0):
    print("Multiple of 7.")

else: 
    print("Not Multiple of 7.")