# Program to find the common divisors of two entered positive integers
# Demonstrates the use of tuples
# Uses optimised function to calculate the common factors

"""
Pseudocode

DEFINE function 'finddiv(x, y)'
    set x = the minimum of 'x' and 'y'
    IF 'x' modulus 'z' = 0 and 'y' modulus 'z' = 0
        Create a tuple called 'div' and populate it with (1, z)
    ELSE
        Create a tuple and populate it with (1,)
    FOR 'i' in range (start=2, end=z/2+1, iteration=1)
        IF 'x' modulus 'i' = 0 and 'y' modulus 'i' = 0
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
    z=min(x,y)
    if x%z==0 and y%z==0:
        div = (1, z)
        print("div = ",div)
    else:
        div = (1,)
        print("div = ",div)
    for i in range(2, z//2+1):
        if x%i==0 and y%i==0:
            div+=(i,)
    return div

    


num1 = int(input("Please enter a positive integer: "))
num2 = int(input("Please enter another positive integer: "))
if num1<=0 or num2<=0:
    print("Entered numbers should be greater than 0.")
else:
    commdiv = finddiv(num1, num2)
    print("The common divisors of", num1, "and", num2, "are:", commdiv)
    total=0
    for d in commdiv:
        total+=d
    print("The sum of the common divisors is:", total)
print("Finished")


