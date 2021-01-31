# Program to find all the perfect numbers up to and including a supplied number

"""
Pseudocode

DEFINE function 'finddivtot(x)'
    PRINT "The number being factored is" 'x'
    Create tuple called 'div' with no contents
    FOR i in range (start=1, end=(x), iteration=1)
        IF x modulus i = 0
            add (i,) to the tuple 'div'
    PRINT "The proper factors of" 'x' "are" 'div'
    create variable 'tot' and set it to 0
    FOR d in div
        tot = tot+d
    PRINT "The total of the proper factors of" 'x' "is" 'tot'
    RETURN 'tot'

request the user to enter a positive integer and assign it to variable 'num1'
Print "Please enter a positive integer: "
IF 'num1' <= 0
    PRINT "Entered numbers should be greater than 0"
ELSE
    create a tuple called 'perfnums' with no contents
    FOR 'i' in range(start=1, end=num1+1, iteration=1)
        if 'i' = finddivtot(i)
            add (i,) to tuple 'perfnums'
    PRINT "The perfect numbers up to and including" num1 "are" perfnums
PRINT "Finished"

"""

def finddivtot(x):
    print("The number being factored is", x)
    div = ()
    for i in range(1, x):
        if x%i==0:
            div+=(i,)
    print("The proper factors of", x, "are", div)
    tot=0
    for d in div:
        tot+=d
    print("The total of the proper factors of", x, "is", tot)
    return tot


num1 = int(input("Please enter a positive integer: "))
if num1<=0:
    print("Entered numbers should be greater than 0.")
else:
    perfnums=()
    for i in range(1, num1+1):
        if i == finddivtot(i):
            perfnums+=(i,)
    print("The perfect numbers up to and including",num1,"are:", perfnums)
print("Finished")       


