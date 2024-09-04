## NOTE Use # to add a comment or remove a line of code from running
#  Uncomment a line of code by remoing # in front of it


# print output, e.g., Welcome
print("Welcome")

#TODO:
# Write code to get user input and store it in a variable namded classname
#   then output (print) "This class is [classname]"
print("What is this class?")
# write your code below:
classname = input()
print("This class is" + classname)

# better code
#print("No way!", input(), "is such a hard class! I can't believe you're taking it! That is so impressive!")



### SyntaxError
# Violating prohramming langiage's rules: Print('welcome")

### TypeError
# An opperation uses incorrect types: "ABC" + 4

### NameError
# Uses a variable that does not exist: x = y # y is not defined

### ValueError
# Invalid value is used, such as giving letters to int() int("January")