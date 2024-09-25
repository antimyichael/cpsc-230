# Class Activities (Lecture 7)

'''
0. What's wrong with this while loop and how can you fix it?
'''
print(" \n0)")

#x = 1
#while x < 10:
#     print(x)

print(" The while loop never adds to the value of 'x'. It can be fixed by adding to 'x' each time the loop itterates")
x = 1
while x < 10:
    x += 1
    print(x)
'''
1. Use a while loop, print out all the numbers between 1 and 10 (including).
'''
print(" \n1)")

x = 1
while x != 11:
    print(x)
    x += 1

'''
2. Use a while loop, print out all the numbers between 1 and 100 (including) that are
divisible by BOTH 5 and 9.
Add comment for each line to explain the code
Hint: When a is divisible by b, the remainder of a/b is 0.
    Recall: How to check an even number? (it is a number that is divisible by 2).
'''
print(" \n2)")

x = 1 # Defines 'x' at the beginning of the 1-100
while x != 101: # Prevents numbers past 100 from being accounted
    if (x%5==0) and (x%9==0): # 'x' must be divisible by both 5 and 9 in this case. an easy way to do this is with the modulus operator to avoid handling floats.
        print(x) # Simply prints out the current value of 'x' if the If statement passed
    x += 1 # Adds 1 to the current value of 'x'


    

'''
3. Use a while loop, print out all the numbers between 1 and 100 (including) that are
divisible by both 5 and 9.
Exit the loop when the number is greater than 50.
Use break for this question.
Add comment for each line to explain the code
'''
print(" \n3)")

x = 1 # Defines 'x' at the beginning of the 1-100
while x != 101: # Prevents numbers past 100 from being accounted
    if x > 50: # Checks to see if the current value of 'x' is over 50
        break # Ends the while loop
    if (x%5==0) and (x%9==0): # 'x' must be divisable by both 5 and 9 in this case. an easy way to do this is with the modulus operator to avoid handling floats.
        print(x) # Simply prints out the current value of 'x' if the If statement passe
    x += 1 # Adds 1 to the current value of 'x'

'''
4. Use a while loop, print out all the numbers between 1 and 10 (including) 
EXCEPT for those which are divisiable by 3.
Use continue for this question.
Add comment for each line to explain the code
'''
print(" \n4)")
x = 0 # Defines 'x' at the beginning of the 1-10
while x != 10: # Prevents numbers past 10 from being accounted
    x += 1 # Adds 1 to the current value of 'x'
    if (x%3!=0): # Checks to make sure 'x' is not divisable by 3
        print(x) # Prints the current value of 'x'
