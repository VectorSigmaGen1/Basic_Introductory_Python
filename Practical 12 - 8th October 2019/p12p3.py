# Define the function approx_sqrt which takes a number & a tolerance and returns an approximate Square Root
# Program to check if an entered integer is a positive integer and if so to apply the function factorial to produce an answer

"""
Pseudocode

Define function 'approx_sqrt' of variables 'a' & 'b':
(a is the number you want the root of and b is the tolerance)
    set variable 'step' = b squared
    set variable 'root' = 0.0
    WHILE the absolute value of (a - root squared) >= b and root squared <= a:
        root = root + step
    IF the absolute value of (a - root squared) < b
        THEN return root
    ELSE
        THEN return "fail"


request the input of a floating point number and assign it to variable 'num'
print "Please enter a floating point number you would like to calculate the square root of: "
set variable 'epsilon' = 0
IF num < 0:
    print "Error: Number entered was less than 0."
ELSE
    IF the output of the function 'approx sqr_rt' on (num, epsilon) returns "fail"
        THEN print "Error: Number entered was less than 0."
    ELSE
        THEN print the output of the function 'approx_sqrt' on (num, epsilon)


"""


# define the function to calculate the approximate square root
def approx_sqrt(a, b):
    step = b**2
    root = 0.0
    while abs(a-root**2) >= b and root**2 <= a:
        root = root + step
    # number of guesses functionality removed as it gives a printed output, not a return
    if abs(a - root**2) < b:
        return root
    # Changing the printed output to a return which can be used to indicate a printed output in the calling program
    else:
        return "fail"
        

# program to check entered integer and call function if appropriate and print appropriate response based on return
num = float(input("Please enter a floating point number you would like to calculate the square root of: "))
epsilon = 0.01
if num < 0:
    print("Error: Number entered was less than 0.")
else:
    if approx_sqrt(num, epsilon) == "fail":
        print("Failed to find the square root of", num)
    else:
        print(approx_sqrt(num, epsilon))





















