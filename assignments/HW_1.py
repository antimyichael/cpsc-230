# Homework for Lectures 1 & 2
# NOTE: This file is ONLY for code and comments, 
#       Write your written report in a separate document
print("1)")
'''
1. Write code to print out: Hello, what is your name?
    then ask the user to input their name, 
    assign their name to a variable called user_name
    and print out: Hello [their name]
'''
print("Hello, what is your name?")
user_name = input()
print("Hello", user_name + "!")


print(" \n2)") ##############################################################

'''
2. Given variables x and y, can you write code to assign 9 to x and x + 1 to y, 
    and print out the values of x and y with one statement? Include comments to EACH line
    to explain the code.
'''

x = 9; y = x + 1
# Semicolon just to combine lines.
# First, "x" must be initialized/defined because "y" is dependant on the value of "x".
# If we switch line 25 with line 32, ["x" is not defined (Pylance) reportUndefinedVariable] is returned.
# y = x + 1; x = 9
# "x" must be defined before "y" because the defining of "y" relies on the "x" variable.

print("X:",x,"\nY:",y)
# Using commas, spaces can be added. Commas are an alternative to using [" " + ]
# The \n is just used to make a new line so that the values for "x" and "y" can be printed nicely
# In the beginning of the print function, the use of quotations (" ") sets the "X:" to a string.
# Placing a comma outside of that creates space between whatever is on the left and right of that comma.
# Calling the variable "x" which was already defined, "x" is printed out.
# After printing the value of "x", a comma is used for the same purpose that is was previously used.
# Using the "\n" makes a new line and places the next part of the print statement on that new line.
# With the same process as before with "x", the variable "y" can be printed out on a new line while
# keeping everything in one print statement.

print(" \n3)") ##############################################################

'''
3. Write a statement that assigns total_coins with the sum of nickel_count and 
    dime_count to complete the code. Include comments to EACH line
    to explain the code.
'''
# Initializes the variable "total_coins" with the int value "1"
total_coins = 0

# Defines "nickel_count" as the next line of input in the terminal and type casts it as an int.
nickel_count = int(input())

# Defines "dime_count" as the next line of input in the terminal while also type casting it as an int.
dime_count = int(input())

### write your code below
total_coins = nickel_count + dime_count

# From question 3, it is clear that "total_coins" needs to represent the sum of "nickel_count" and "dime_count".
# In line 52, "total_coins" was initialized with the int value of "1". Now, it will represent the int value of "dime_count"
# added to the int value of "nickel_count".

# prints the int value of "total_coins".
print(total_coins)

# ideally i wouldve wanted to add a line such as:
# print("Nickel Count?:")
# To someone who is not able to see the code, they would be able to understand what value
# is intended to be typed in.
##############################################################