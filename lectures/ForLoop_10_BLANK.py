# Class Activities (Lecture 10)

'''
1. Use a for loop and range() to create integers from 0 to 5 (inclusive) and print them out.
'''
print("QUESTION 1:")
# write your code below
for i in range(0,6):
    print(i)
    i+=1


'''
2. Use a for loop and range() to create integers from 0 to 5 and print them out.
Use a loop variable to count iteration number and print it out after the for loop.
'''
print("QUESTION 2:")
# write your code below
for i in range(0,5):
    print(i)
    i+=1
print(i, "times")



'''
3. Use a for loop to iterate a list of numbers, use variable num_neg 
    to count the number of negative numbers (< 0), and print the result.
'''
print("QUESTION 3:")
numbers = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
num_neg = 0
# write your code below
for i in numbers:
    if i < 0:
        num_neg+=1
print(num_neg)



'''
4. Ask the user to input two words of the SAME LENGTH. If they give words of the same length,
use a for loop, count how many corresponding letters are the same in the two strings. 
For example in 'spam' and 'span', 3 of the letters (s,p,a) are the same. 
In the words 'bitter' and 'better',5 of the letters are the same. 
Print out a message telling the user how many letters are the same.
Hint: 
 1. Get both words' lengths and compare.
 2. Access the corresponding charaters of the same index in both words and compare them.
'''
print("QUESTION 4: ")
# write your code below
str1 = input("Word 1: ")
str2 = input("Word 2: ")
count = 0
same = []
if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count+=1
            same.append(str1[i])
    if count > 1:
        print(count, "letters matched:\n" + same)
    else:
        print(count, "letter matched:\n", same)



