# Class Activities (Lecture 9)

'''
1. Ask the user to input a random word, assign it to my_string.
First, check if my_string is all uppercased. 
If yes, print out "Good, all're uppercased!".
Otherwise, convert my_string to all uppercase and print out the result.
'''
my_string = input("Input a random word: \n")
if my_string.upper() == my_string:
    print("Good, all're uppercased!")
else:
    my_string=my_string.upper()
    print(my_string)

'''
2. Replace all occurrences of "coffee" with "hot chocolate" and "programmer" 
with "coder". Print out the result.
'''
paragraph = """In the town of Coderville, every programmer loved to drink coffee; 
coffee gave them the energy to code late into the night. 
However, some programmers preferred tea over coffee.""" 
# Note: In Python, a pair of triple double quotes like the ones above,
#   creates a multi-line string.
paragraph = paragraph.replace("coffee", "hot chocolate")
paragraph = paragraph.replace("programmer", "coder")
print(paragraph)


'''
3. Ask the user to type AT LEAST two words separated by spaces, store the input to a variable named my_string.
    a. Check if the first character is capitalized (upper case), 
        if yes, print out "[user input]'s first character is capitalized".
        otherwise, print out "[user input]'s first character is NOT capitalized".
        Hint: Access the first character using index.
    b. Check if the first character is a number: 0 - 9,
        if yes, print out "[user input]'s first character is a number".
        otherwise, print out "[user input]'s first character is NOT a number".
    c. Print how many words in my_string
        Hint: Split my_strings by space and print the length of the list of tokens.
'''
my_string = input("Type at least two words seperated by spaces:\n")
if my_string[0].isupper():
    print("[" + my_string + "]'s first character is capitalized.")
    print("[" + my_string + "]'s first character is NOT a number.")
if my_string[0].islower():
    print("[" + my_string + "]'s first character is NOT capitalized.")
    print("[" + my_string + "]'s first character is NOT a number.")
else:
    print("[" + my_string + "]'s first character is a number.")
print("[" + my_string + "] has", len(my_string.split()), "words in it.")