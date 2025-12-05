# Negetive slicing works as the Positive slicing but in the negative slicing they start from the last and its indexing start from the -1 not from the 0.

# For Example: Orange
# In 'Orange' the Indexing value of O is -6, r is -5, a is -4, n is -3, g is -2, and e is -1

str = "Orange"
print(str[-5 : -1])
print(str[-5 : ])
print(str[ : -1])
print(str[-1 : -6]) # Code Execute but noting gives in the output

