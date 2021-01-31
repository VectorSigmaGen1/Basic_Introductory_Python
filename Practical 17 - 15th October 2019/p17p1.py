# Program to find the divisors of an entered positive integer
# Demonstrates the use of tuples
# Uses an optimised function

"""
Pseudocode

DEFINE function 'finddiv(x)'
    Create tuple called 'div' with the contents (1, x)
    FOR i in range (start=2, end=x, iteration=1)
        IF x modulus i = 0
            add (i,) to the tuple 'div'
    RETURN 'div'


request the user to enter a positive integer and assign it to variable 'num1'
Print "Please enter a positive integer: "
IF 'num1' <= 0
    PRINT "Entered numbers should be greater than 0"
ELSE
    create a tuple called 'divnum' and assign it to the output of finddiv(num1)
    PRINT "The divisors of" 'num1' "are:" divnum
    create the variable 'total' and assign it the value 0
    FOR 'd' in divnum
        'total' = 'total' + 'd'
    PRINT "The sum of the common divisors is:" 'total'
PRINT "Finished"


"""



def finddiv(x):
    """Finds the divisors of x

    Assumes that x is a positive integer
    Returns a tuple containing the divisors of x"""
    
    div = (1, x)
    for i in range(2, x//2+1):
        if x%i==0:
            div+=(i,)
    return div


num1 = int(input("Please enter a positive integer: "))
if num1<=0:
    print("Entered numbers should be greater than 0.")
else:
# First of all, get the divisors and print them out
    divnum = finddiv(num1)
    print("The divisors of", num1, "are:", divnum)
# Now sum them and print the total
    total=0
    for d in divnum:
        total+=d
    print("The sum of the divisors is:", total)
print("Finished")


