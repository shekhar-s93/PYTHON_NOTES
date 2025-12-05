str_1 = "Shekhar"
str_2 = "Suman"

str = str_1 + str_2

# lengh of the string
print("Length of First String: ", len(str_1))
print("Length of Second String: ", len(str_2))
print("Length of Concetinaded String: ", len(str))

# For Example if we concinate the "str_1" and "str_2" the final output will (ShekharSuman) not (Shekhar Suman)
print(str)
print("Length of:",str,"is:", len(str))

# If we want to add a space between them then we have to write a blank space string in it like (" ")
str = str_1 + " " + str_2
print(str)
print("Length of:",str,"is -",len(str))
