# Define the function factorial which calculates the factorial of a positive integer
# Program to check if an entered integer is a positive integer and if so to apply the function factorial to produce an answer

"""
Pseudocode

DEFINE function 'factorial' of a variable 'a':
    set variable 'fact' = 1
    set variable 'i' = 1
    WHILE i <= a
        fact = (fact * i)
        i = (i+1)
    RETURN fact


request the input of an integer and assign it to variable 'number'
print "Enter the number for which you wish to calculate the factorial (an int >= 0): "
IF number < 0:
    print "Error: Number entered was less than 0."
ELSE
    print the output of the function 'factorial' as performed on number


"""



#Defining function to caluclate factorial
def factorial(a):
    fact=1
    i=1
    while i<=a:
        fact*=i
        i+=1
    return fact

# program to check entered integer and call function if appropriate   
number = int(input("Enter the number for which you wish to calculate the factorial (an int >= 0): "))
if number < 0:
    print("Error: Number entered was less than 0.")
else:
    print(factorial(number))
