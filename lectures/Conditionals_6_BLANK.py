# Class Activities (Lecture 6)

'''
** Update your previous code to use if-elif-else statements instead. **
Let's implement a simpler version of the game "Rock, Paper, Scissors" using conditionals.
* Rock crushes Scissors
* Scissors cuts Paper
* Paper covers Rock
1. Get two inputs from the user and stored them in variables player1_choice and player2_choice
2. Compare their choices:
    Assume player 1 always chooses 'Rock'
        i.e., assign 'Rock' to player1_choice
    When players 1 and 2 choose the same: print "It's a tie!"
    If player 2 chooses Scissors, print "Player 1 wins! Rock crushes Scissors!"
    If player 2 chooses Paper, print "Player 2 wins! Paper covers Rock!"
'''
# write your code below





'''
Ask the user to input an integer and store it in the variable x.
Convert the value of x into an integer. 
Check whether the number is even and greater than 17.
If yes, print "Yes!"; otherwise, print "No."
Use if-else statement and a logical operator.
Hint: an even number can be exactly divided by 2, leaving a remainder of 0. 
'''
# write your code below
x = int(input("Please input an integer\n"))
if (x%2==0) and x > 17:
    print("Yes!")
else:
    print("No.")



'''
EXTRA EXERCISE (Optional)
You are designing a system for a park to determine whether a visitor 
is allowed to enter based on their age and height.

Write a program that:
* Asks the user for their age (integer input)
* Asks the user for their height (in centimeters, float input)
* The visitor can etner the park if they are AT LEAST 10 years old
    AND AT LEAST 120.0 cm tall.
* If they don't meet both conditions, deny their entry with a message
    AND let them know the reason.
* Otherwise, print a message to welcome them!

Use if-else and logical operators (and/or) for this question.
'''
# write your code below
age = int(input("How old are you?"))
height = float(input("How tall are you? (cm)"))
if (age>=10) and (height>=120.0):
    print("Welcome in!")
else:
    print("Entry Denied. \nReason:")
    if not (age>=10):
        print("- Too young")
    if not (height>=120.0):
        print("- Too short")