str = "i'm Shekhar Suman from Bihar"

# 1st Function is 'endwith()' function.
    # Syntax of 'endwith' function = var_name.endswith("last word of your sentence")
    # it returns true if string ends with valid sentence word.

print("1st \t endswith Function answer: ",str.endswith("r"))



# 2nd Function is 'capitalize()' function
    #   Syntax of 'capitalize()' = var_name.capitalize()
    #   The work of this function is it capitalize the first letter of the string.

print("2nd \t", str.capitalize()) 

    # Incase in future after use this function if you want to print the original string like this (print("str")), after using this function then it will not updated because of their function.

print("3rd \t",str) # Here you can see the original string after using this function.

    # if you want to updated original string to capitalize function then you have to use this method.

str = str.capitalize() # Here capitalize function are stored in the the variable.
print("4th \t", str)


# 3rd Function is 'replace()' function
    # Syntax of 'replace()' = var_name.replace("old", "new")
    # replaces all words to the new word from the string, like if your sting is "Apple is Yellow color"

str_1 = "Apple is Yellow color"
print("5th \t",str_1.replace("Apple", "Banana"))

    # In case you want to replace all the "o" letter to "e" letter from the string then you can

print("6th \t", str_1.replace("o", "e"))


# 4th Funciton is 'find()' function
    # Syntax of 'find()' = var_name.find("word")
    # Works of find() function is, it give the indexing position of the word where they comes first time from the string.

print("7th \t", str.find("bihar")) # here i write the word "bihar" instid of "Bihar", its gives the correct output because it is the text.
print("8th \t", str.find("N")) # here its return -1 because "N" is not exit in the string


 
# 5th Function is 'count()' function
    # Syntax of 'count()' = var_name.count("word")
    # Works of count() function is, it counts the word how many time it comes in the string.

print("9th \t", str_1.count("l"))

str_2 = "Incase in future after use this function if you want to print the original string like this , after using this function then it will not updated because of their function"

print("10th \t", str_2.count("this"))