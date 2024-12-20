# Homework for Lectures 15 & 16
# Rename the file as HW_9_YOURNAME.py

print("QUESTION 1:")
'''
1. Can you manage a guest list based on the requirements below using list methods?
    a) Create a guest list of Alice, Bob, and Cory.
    b) Alice decided to bring two friends, Cory (another Cory) and David, to the party. 
        Use the append() method to add "Cory" and "David" to the list, respectively. 
    c) You realized that you mistakenly added Bob, who won't be attending. 
        Use the remove() method to remove them from the list.
    d) Use the insert() method to add "Eva" to the list, making sure they are the second in the order.
    e) Pop the last person from the list, store their name to a variable, extra_guest, and print a message saying they are on standby.
    f) Use count() to to check if there is any guest named "Cory". 
        If yes, 
            print how many guests are named "Cory"; 
            use index() to find the position (i.e., index) of the FIRST "Cory" in the list and print their position; 
        Otherwise, 
            print "Cory is not in the list".
    g) Finally, print the sorted guest list based on REVERSED alphabetical order.
'''
# write your code below

### a)
guestList = ["Alice", "Bob", "Cory"]
### b)
guestList.append("Cory")
guestList.append("David")
### c)
guestList.remove("Bob")
### d)
guestList.insert(1, "Eva")
### e)
extra_guest = guestList.pop(-1)
print("e) " + str(extra_guest) + " is on standby")
### f)
if guestList.count("Cory") > 1:
    print("f) " + str(guestList.index("Cory")))
else:
    print("f) Cory is not on the list")
### g)
print("g) " + str(sorted(guestList, reverse=True)))




print("QUESTION 2:")

'''
2. Simulate a simple banking system with functions to deposit, withdraw, and check balance.
    a) Create a global variable account_balance initialized to 0.
    b) Write a function, deposit, with one input parameter, amount, that adds the amount to account_balance; no return.
    c) Write a function, withdraw, with one input parameter, amount, that subtracts the amount from account_balance; no retutn.
        ENSURE that the withdrawal does not cause a negative balance. 
        If so, warn the user, and only allow them to withdraw the available amount (i.e., account_balance) 
        and set account_balance to be 0.
    e) Write a function, check_balance, with no input parameter and only prints the current balance; no return.
    f) Perform a series of deposits and withdrawals, and check the balance as below. 
        Deposite $100 => Withdraw $50 => Withdraw $60 => Deposite $30 => Check_balance
       
NOTE: 
    Define all the required functions first and then call them one after another in f);
      Refer to Q1 of the in-class exercise of Lecture 16.
    Clearly EXPLAIN how account_balance has been changed for each action listed above, 
      leading to the final result in your report.
'''
# write your code below

### a)
global account_balance
account_balance = 0
### b)
def deposit(input):
    global account_balance
    account_balance+=input
### c)
def withdraw(input):
    global account_balance
    if (account_balance-input) >= 0:
        account_balance-=input
    else:
        print("Warning: Insufficient funds")
        account_balance = 0
### e)
def check_balance():
    global account_balance
    print("f) $" + str(account_balance))
### f)
deposit(100)
withdraw(50)
withdraw(60)
deposit(30)
check_balance()