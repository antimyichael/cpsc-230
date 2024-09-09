# Class Activities (Lecture 3)

# Numbers
'''
Create a variable x and assign a random integer (e.g., 5) to it and 
print it and its type in one statement
'''
x = 93
print(x, type(x))

'''
Create a variable y and assign a random float (e.g., 1.3) to it and 
print it and its type in one statement
'''
y = 76.1
print(y, type(y))

# strings
'''
Create a string consisting of all types of characters:
numbers, letters, symbols, and spaces.
Print out the string and its type.
'''
new_str = "Section 10 of CSPC-230 is in Keck-156!"
print(new_str, type(new_str))

# List
'''
Create a list of 1, 2, 3, 4, 5
'''
new_list = [1,2,3,4,5]


'''
Create a list consisting of a string, an integer, a float
and a list.
Print out the list and its type.
'''
other_list = ["CSPC-230", 99, 1.56]
print(other_list, type(other_list))

# Dictionary
'''
Create a variable of dictionary, named cpsc230
- keys are 'Name', 'School', 'Credits'
- values are 'Computer Science I', 'Engineer', an integer of 3
- Print out the dictionary and its type.
'''
cpsc230 = {"Name" : "Computer Science I" , "School" : "Engineer" , "Credits" : 3}
print(cpsc230, type(cpsc230))

# Set
'''
Create a set called my_set, consisting of 1, 2, 3, 4, 5, 5, 5, 6 
Print out my_set. Did it change at all? 
Explain why.
'''
my_set = {1,2,3,4,5,5,5,6}
print(my_set)
# Yes, the set did change after being defined. This is because the value of '5' was
# already included in the set. Sets are ordered numerically and without duplicates, preventing
# the value of '5' from recurring in the set.

# Type conversions
'''
Create two variables, a and b, assigned with '1.3' and '5',
Convert the first variable into a float 
Convert the second variable into an integer
Sum them up and assign the result to another variable, c
Print out the value of c, and its type.
Explain why the result is that type.
'''
a = 1.3
b = 5
c = a + b
print (c, type(c))
# 'c' is defined as a float because during the addition of 'a' and 'b', at least
# one of the values is a float. Python does not truncate this form of addition
# to provide accuracy.