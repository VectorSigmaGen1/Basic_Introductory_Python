# Program to print out the largest of two entered numbers
# Uses 2 functions called "max" and "print_max"

"""
Pseudocode

DEFINE function 'print_max'
    DEFINE function 'print_max' of variables a & b
        IF variable a is greater than variable b
            RETURN a
        ELSE
            RETURN B
    Request the user to input a float and assign it to variable 'num1'
    Request the user to input a float and assign it to variable 'num2'
    PRINT "The largest of" 'num1' "and" 'num2' "is" the output of the function 'max' on 'num1' & 'num2'
    RETURN nothing

Call the function 'print_max'

"""



def print_max():
    """Function that prints out the largest of two numbers

    Uses the function "max" to find the largest"""
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
    return

print_max()
