# Program that takes a series of integers and prints each time that number of terms of the Fibbonacci Sequence
# Uses a recursive function

"""
Pseudocode

DEFINE function 'fibb'
    print "The function is now considering term" 'x'
    IF variable 'x' = 0
        RETURN 0
    ELIF variable 'x' = 1
        RETURN 1
    ELSE
        set variable 'term' = fibb('x'-1) + fibb('x'-2)
        print "Calculating.....Term" 'x' "is" 'term'
        RETURN term

request the user to enter an integer and assign it to variable 'x'
Print "Please enter the number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "
WHILE x>= 0
    create list called 'sequence'
    FOR 'i' in range(start-0, end-x, iteration-1)
         add = fibb(i) to list 'sequence'
    Print "The first" 'x' "terms of the Fibonacci Sequence are: " 'sequence'
    request the user to enter an integer and assign it to variable 'x'
    Print "Please enter another number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "
print "You have entered a negative number. The program will now terminate."


"""


def fibb(x):
    print("The function is now considering term", x)
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        term = (fibb(x-1) + fibb(x-2))
        print("Calculating.....Term", x, "is", term)
        return term

   

x = int(input("Please enter the number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "))
while x >= 0:
    sequence = []
    for i in range(x):  
        sequence += [fibb(i)]
    print("The first", x, "terms of the Fibbonacci Sequence are: ", sequence)
    x = int(input("Please enter another number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "))
print("You have entered a negative number. The program will now terminate.")

