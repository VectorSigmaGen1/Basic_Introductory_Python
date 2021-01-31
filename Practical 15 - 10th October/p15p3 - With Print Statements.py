# program that takes as input a series of integers >= 0
# and for each integer prints that number of terms of a function
# Uses recursion

"""
Pseudocode

DEFINE function 'func3'
    print "The function is now considering term" 'x'
    IF variable 'x' = 0
        RETURN 13
    ELIF variable 'x' = 1
        RETURN 8
    ELSE
        set variable 'term' = func3(x-2) + 13*func3(x-1)
        print "Calculating.....Term" 'x' "is" 'term'
        RETURN 'term'

request the user to enter an integer and assign it to variable 'x'
Print "Please enter an integer equal to or greater than 0: "
WHILE x>= 0
    create list called 'sequence'
    FOR 'i' in range(start-0, end-x+1, iteration-1)
        add func3(i) to list 'sequence'
    Print "The first" 'x' "terms of the Fibonacci Sequence are: " 'sequence'
    request the user to enter an integer and assign it to variable 'x'
    Print "Please enter another integer equal to or greater than 0: "
print "You have entered a negative integer. The program will now terminate"

"""



def func3(x):
    print("The function is now considering term", x)
    if x == 0:
        return 13
    elif x == 1:
        return 8
    else:
        term = func3(x-2) + 13*func3(x-1)
        print("Calculating.....Term", x, "is", term)
        return term

x = int(input("Please enter an integer equal to or greater than 0: "))
while x>=0:
    sequence = []
    for i in range(x+1):
        sequence += [func3(i)]
    print("The first", x, "terms of the Sequence are: ", sequence)
    x = int(input("Please enter another integer equal to or greater than 0: "))
print("You have entered a negative integer. The program will now terminate")
