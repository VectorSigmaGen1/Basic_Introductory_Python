# Program to print out the largest of two entered numbers
# Uses a function called "max"
# Uses "max" in a print statement

"""
Pseudocode

DEFINE function 'max' of variables a & b
    IF variable a is greater than variable b
        RETURN a
    ELSE
        RETURN B

Request that the user enter two numbers and assign them to the variables 'num1' & 'num2'
PRINT "The largest of" 'num1' "and" 'num2' "is" the output of the function 'max' on 'num1' & 'num2'
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
print("The largest of", num1, "and", num2, "is", max(num1, num2))
print("Finished!")
