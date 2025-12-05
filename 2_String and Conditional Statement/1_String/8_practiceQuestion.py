# Write a program to input user's first name and print its length.

name = input("Enter your First Name: ")
print("Length of you name is : ",len(name))



# Write a program to find the occurrence of '$' in a String.

str = "dollor is a american currency the value of $ in india is 85 rupees"
str_1 = "$ dollor is a american currency $ the value of $ in india is 85 rupees"

print(str.find("$"))
print(str_1.count("$"))