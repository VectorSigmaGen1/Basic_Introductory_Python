# Program to calculate the factorial of a positive integer using recursion

"""
Pseudocode

DEFINE function 'fact' of variable 'x'
    PRINT 'x'
    IF 'x' = 0
        RETURN 1
    ELSE
        RETURN x * fact(x-1)

Request that the user enter an integer and assign it to the variable 'num'
WHILE 'num' < 0
    PRINT "You have entered a negative integer and unfortunately the factorial of negative integers is undefined. Please enter a positive integer: "
    Assign input to variable 'num'
PRINT "The factorial of" 'num' "is" fact('num')

"""





def fact(x):
    print(x)
    if x == 0:
        return 1
    else:
        return x*fact(x-1)


num = int(input("Please enter an integer to calculate the factorial of: "))
while num<0:
    num = int(input("You have entered a negative integer and unfortunately the factorial of negative integers is undefined. Please enter a positive integer: "))
print("The factorial of", num, "is", fact(num))
