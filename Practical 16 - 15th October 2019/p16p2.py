# Program to find the common divisors of two entered positive integers
# Demonstrates the use of tuples

"""
Pseudocode

DEFINE function 'finddiv(x, y)'
    Create tuple called 'div' with no contents
    FOR i in range (start=1, end=(the minimum of (x, y)+1), iteration=1)
        IF x modulus i = 0 and y modulus i = 0
            add (i,) to the tuple 'div'
    RETURN 'div'


request the user to enter a positive integer and assign it to variable 'num1'
Print "Please enter a positive integer: "
request the user to enter another positive integer and assign it to variable 'num2'
Print "Please enter another positive integer: "
IF 'num1' <= 0 or 'num2' <= 0
    PRINT "Entered numbers should be greater than 0"
ELSE
    create a tuple called 'commdiv' and assign it to the output of finddiv(num1, num2)
    PRINT "The common divisors of" 'num1' "and" 'num2' "are:" commdiv
    create the variable 'total' and assign it the value 0
    FOR 'd' in commdiv
        'total' = 'total' + 'd'
    PRINT "The sum of the common divisors is:" 'total'
PRINT "Finished"


"""



def finddiv(x, y):
    """Finds the common divisors of x and y

    Assumes that x and y are positive integers
    Returns a tuple containing the common divisors of x and y"""
    
    div = ()
    for i in range(1, min(x, y)+1):
        if x%i==0 and y%i==0:
            div+=(i,)
    return div


num1 = int(input("Please enter a positive integer: "))
num2 = int(input("Please enter another positive integer: "))
if num1<=0 or num2<=0:
    print("Entered numbers should be greater than 0.")
else:
# First of all, get the common divisors and print them out
    commdiv = finddiv(num1, num2)
    print("The common divisors of", num1, "and", num2, "are:", commdiv)
# Now sum them and print the total
    total=0
    for d in commdiv:
        total+=d
    print("The sum of the common divisors is:", total)
print("Finished")


