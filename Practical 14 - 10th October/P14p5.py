# Program that takes a series of integers and prints each time that number of terms of the Fibbonacci Sequence
# Uses a recursive function

"""
Pseudocode

DEFINE function 'fibb'
    IF variable 'x' = 0
        RETURN 0
    ELIF variable 'x' = 1
        RETURN 1
    ELSE
        RETURN fibb('x'-1) + fibb('x'-2)

request the user to enter an integer and assign it to variable 'x'
Print "Please enter the number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "
WHILE x>= 0
    print "The first" 'x' "terms of the Fibbonacci Sequence are: " and suppress newline
    FOR 'i' in range(start-0, end-x, iteration-1)
        print fibb(i) and suppress newline
    Print newline
    request the user to enter an integer and assign it to variable 'x'
    Print "Please enter another number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "
print "You have entered a negative number. The program will now terminate."


"""


def fibb(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return(fibb(x-1) + fibb(x-2))

   

x = int(input("Please enter the number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "))
while x >= 0:
    print("The first", x, "terms of the Fibbonacci Sequence are: ", end="")
    for i in range(x):  
        print(fibb(i), end=", ")
    print("")
    x = int(input("Please enter another number of terms of the Fibbonacci Sequence you wish to display (Enter a negative number to exit program): "))
print("You have entered a negative number. The program will now terminate.")

