# Conditional Statements.

# if - elif - else (SYNTAX)
"""

    if(condition):
        Statement1
    elif(conditon):
        Statement2
    else:
        statement3

"""

# For Example : 
#   If your age is 18 you can vote and apply for the license.

#   CODE:

age = 18
if(age >= 18):
    print("1 \t You can vote and apply for the license")

#   You can run multiple statement at a time.
#   Like if your statement is true, and you want to execute multiple statement then first statement will 
#       1 - You can apply for voter ID  
#       2 - You can vote
#       3 - you can apply Driving License

age2 = 18
if(age >= 18):
    print("2 \t You can apply for voter ID")
    print("3 \t You can vote")
    print("4 \t You can apply for driving License")


# Another method to add the condition.

age_2 = 14
if(True): # The condition (True) just print the value it's does not matter what type or data in your variable it just print the statement.
    print("5 \t You can apply for voter ID")
    print("6 \t You can vote")
    print("7 \t You can apply for driving License")