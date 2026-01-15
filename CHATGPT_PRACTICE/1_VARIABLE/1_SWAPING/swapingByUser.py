# Create two variable a and b. Swap their value without using third variable and the values given by the user.

a = int(input("Enter first Value : "))
b = int(input("Enter Second Value : "))

# Value before Swappint 
print("Before Swapping the value is : ", a,"and", b)

# Swapping process
a += b
b = a-b
a = a-b

print("After Swaping : ", a,"and", b)