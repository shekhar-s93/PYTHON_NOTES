# Inputs in Python: 

# input() statement is used to accept values (using keyboard) from user.

# 1_input() = result for input() is always be string.

# 2_int(input()) = for integer values.

# 3_float(input()) = for float values.

# 1_input()
name = input("Enter your name: ")
print("Welcome to the Programming World: ", name)

# 2_int(intput())
age = int(input("Enter your Age: "))
print("Your age is : ", age)

# 3_float(input())
salary = float(input("Enter your Salary: "))
print("Your Salary is : ", salary)

# Combined them:
print("Welcome ",name, "your age is: ",age, "and your salary is: ",salary)