# Homework for Lecture 10
# Rename the file as HW_10_YOURNAME.py
print("QUESTION 1:")
'''
1. Use range and for loop to iterate all the integers from 1 to 10.
    Evaluate each number to be even or odd and print out:
    "[number] is even" or "[number] is odd"
'''
print("QUESTION 1: ")
# write your code below
for i in range(1,11):
    if i%2==0:
        print(i, "is even")
    else:
        print(i, "is odd")


'''
2. Ask the user to type a sentence made of a few words. Using a for loop to count the number of 
a's, e's, i's, o's, and u's in that sentence (for both upper and lower cases). 
Print out a message letting the user know the count for each letter. 
For example, if the user typed "Amazing, thank you!", the message could be: 
"Your sentence has 3 a, 0 e, 1 i, 1 o, and 1 u"
Hint: 
- Use a for loop to iterate all the character in the string (user input sentence)
        and compare it with a, e, i, o, u, individually, for both upper and lower cases.
        If the same, increment their loop variables, individually.
- Refer to Lecture 10's in-class exercise: Q4.
'''
print("QUESTION 2:")
# write your code below
str1 = input("Please enter a sentence made up of a few words.")
cA = 0
cE = 0
cI = 0
cO = 0
cU = 0
for i in range(len(str1)):
    if str1[i] == "a" or str1[i] == "A":
        cA+=1
    if str1[i] == "e" or str1[i] == "E":
        cE+=1
    if str1[i] == "i" or str1[i] == "I":
        cI+=1
    if str1[i] == "o" or str1[i] == "O":
        cO+=1
    if str1[i] == "u" or str1[i] == "U":
        cU+=1
print("Your sentence has", cA,"a,", cE, "e,", cI, "i,", cO, "o, and", cU, "u.")