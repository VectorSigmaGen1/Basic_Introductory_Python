# Program to print out the largest of two entered numbers
# Uses a function called "max"

"""
Pseudocode

DEFINE function 'max' of variables a & b
    IF variable a is greater than variable b
        RETURN a
    ELSE
        RETURN B

Request that the user enter two numbers and assign them to the variables 'num1' & 'num2'
Call the output of the function 'max' on 'num1' & 'num2' and assign the outpur to the variable 'biggest'
PRINT "The largest of" 'num1' "and" 'num2' "is" 'biggest'
PRINT "Finished"

"""


def max(a, b):
    """Function that returns the largest of two arguments"""
    if a>b:
        return a
    else:
        return b



# Prompt the user for two numbers
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
biggest = max(num1, num2)
print("The largest of", num1, "and", num2, "is", biggest)
print("Finished!")
