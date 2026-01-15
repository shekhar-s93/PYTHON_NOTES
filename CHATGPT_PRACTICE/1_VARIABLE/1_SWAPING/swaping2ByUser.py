# Create two variables a and b. Swap their values using third variable and the values entered by the user.

a = int(input("Enter First Value : "))
b = int(input("Enter Second Value : "))

print("Before Swaping : ", a, "and", b)

# Swapping Process 

c = a
a = b
b = c

print("After Swaping : ", a,"and", b)