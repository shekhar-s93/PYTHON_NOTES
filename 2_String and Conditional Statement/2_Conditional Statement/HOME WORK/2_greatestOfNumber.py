# Write a program to check greatest of 3 numbers entered by user.

num_1 = int(input("Enter First Number : "))
num_2 = int(input("Enter Second Number : "))
num_3 = int(input("Enter Third Number : "))

if(num_1 >= num_2 and num_1 >= num_3):
    print(num_1, "is Greater : ")

elif(num_2 >= num_3):
    print(num_2, "is Greater : ")

else:
    print(num_3, "is Greater : ")