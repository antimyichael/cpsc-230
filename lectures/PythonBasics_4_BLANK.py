# Class Activities (Lecture 4)

'''
Without using Python, figure out the answer to this statement.

    10 + 2 ** 3 - (4+5) + 49/7 * 2

1. What's the Answer? BONUS: will this be a float or int?
2. What Order should we go in?
3. Rewrite this expression using more parenthese to make it
    clearer on what order things are run in.
4. Check your answers using Python.
'''
# your answers here
# 1. 23.0 (Float because of 49/7)
# 2. Left to right
# 3. 10 + (2 ** 3) - (4 + 5) + (49/7) * 2
print(10 + 2 ** 3 - (4+5) + 49/7 * 2)
print(10 + (2 ** 3) - (4 + 5) + (49/7) * 2)
print((10 + 2 ** 3 - (4+5) + 49/7 * 2) == (10 + (2 ** 3) - (4 + 5) + (49/7) * 2))
# 4. Both equations are equal to each other and both equal 23.0


'''
Using Comparison operators and arithmetic operators, make a complicated 
expression (use at least 5 operators, repeats allowed) that evaluates to False.
Check your answer by printing out the result of the expression (should be a False).
'''
# your answer here
print(((7 ** 9) + (3 - 81/4) * 104) == ((7 ** 9) + (3 - 81//4) * 104))