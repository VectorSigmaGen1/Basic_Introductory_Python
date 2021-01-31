# program that takes as input a series of integers >= 1
# and for each integer prints that number of terms of a function
# Uses recursion

"""
Pseudocode

DEFINE function 'func1'
    print "The function is now considering term" 'x'
    IF variable 'x' = 1
        RETURN 2
    ELSE
        set variable 'term' = 2*func1(x-1)
        print "Calculating.....Term" 'x' "is equal to" 'term'
        RETURN 'term'

request the user to enter an integer and assign it to variable 'x'
Print "Please enter an integer greater than or equal to 1: "
WHILE x>= 1
    create tuple called 'seq'
    FOR 'i' in range(start-1, end-x+1, iteration-1)
        add func1(i) to tuple 'seq'
    Print "The first" 'x' "terms of the sequence are: " 'seq'
    request the user to enter an integer and assign it to variable 'x'
    Print "Please enter another integer equal to or greater than 1: "
print "You have entered either zero or a negative integer. The program will now terminate"

"""

def func1(x):
    print("The function is now considering term", x)
    if x==1:
        return 2
    else:
        term = 2*func1(x-1)
        print("Calculating.......Term", x, "is equal to", term)
        return term

x = int(input("Please enter an integer greater than or equal to 1: "))
while x>=1:
    seq = ()
    for i in range(1, x+1):
        seq += (func1(i),)
    print("The first", x, "terms of the sequence are: ", seq)
    x = int(input("Please enter another integer greater than or equal to 1: "))
print("You have entered either zero or a negative integer. The program will now terminate.")

    
