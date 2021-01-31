# program that takes as input a series of integers >= 1
# and for each integer prints that number of terms of a function
# Uses recursion

"""
Pseudocode

DEFINE function 'func2'
    print "The function is now considering term" 'x'
    IF variable 'x' = 1
        RETURN 1
    ELSE
        set variable 'term' = func2(x-1) + 2**(x-1)
        print "Calculating.....Term" 'x' "is" 'term'
        RETURN 'term'

request the user to enter an integer and assign it to variable 'x'
Print "Please enter an integer equal to 1 or greater: "
WHILE x>= 1
    create list called 'sequence'
    FOR 'i' in range(start-1, end-x+1, iteration-1)
        add func2(i) to list 'sequence'
    Print "The first" 'x' "terms of the Fibonacci Sequence are: " 'sequence'
    request the user to enter an integer and assign it to variable 'x'
    Print "Please enter another integer equal to or greater than 1: "
print "You have entered either zero or a negative integer. The program will now terminate"

"""

def func2(x):
    print("The function is now considering term", x)
    if x == 1:
        return 1
    else:
        term = func2(x-1) + 2**(x-1)
        print("Calculating.....Term", x, "is", term)
        return term
    
x = int(input("Please enter an integer equal to 1 or greater: "))
while x>=1:
    sequence = []
    for i in range(1, x+1):
        sequence += [func2(i)]
    print("The first", x, "terms of the Sequence are: ", sequence)
    x = int(input("Please enter another integer equal to or greater than 1: "))
print("You have entered either zero or a negative integer. The program will now terminate")
