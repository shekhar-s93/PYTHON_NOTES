# Create two variable a and b. Swap their value without using third variable.

a = 10
b = 20
print("Before Swapping : ", a, b )

# Swapping process
a = a+b
b = a-b
a = a-b
print("After Swapping : ", a,b)