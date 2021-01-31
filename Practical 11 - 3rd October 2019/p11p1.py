# Calculating the factorial of a number
# Program prompts the user for the number

"""
Pseudocode

Request input and assign to the variable 'number'
Print "Please enter your first number: "
IF number < 0:
    print "Error: Number entered was less than 0."
ELSE:
    set the variable 'fact' = 1
    set the variable 'i' = 1
    WHILE i <= number
        fact = fact + i
        i = i + 1
    print "Factorial of" number "is" fact
print "Finished!"


"""

number = int(input("Enter the number for which you wish to calculate the factorial (an int >= 0): "))
if number < 0:
    print("Error: Number entered was less than 0.")
else:
    fact = 1
    i = 1
    while i <= number:
        fact *= i
        i += 1
    print("Factorial of", number, "is", fact)
print("Finished!")
