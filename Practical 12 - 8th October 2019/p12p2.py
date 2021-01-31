# Define the function fibonacci which displays 'a' number of terms of the Fibonacci Sequence
# Program to check if an entered integer is a positive integer and if so to apply the function factorial to produce an answer

"""
Pseudocode

Define function 'fibonacci' of a variable 'a':
    IF a > 0
        set variable 'num1' = 0
        set variable 'num2' = 1
        print "Your Fibonacci sequence is " num1 and suppress newline
        FOR i in range (1,a)
            set num1 = current value of num 2
            set new value of num2 = num1 + num2
            print num1
        print newline
    ELSE
        print "You have entered zero. This has returned no terms."

request the input of an integer and assign it to variable 'length'
print "Please enter the number of terms in the Fibonacci Sequence you would like: "
IF length < 0:
    print "Error: Number entered was less than 0."
ELSE
    execute the function 'fibonacci' on length


"""


#Defining function to caluclate and display 'a' number of terms of the Fibonacci Sequence
def fibonacci(a):
    if a>0:
        num1=0
        num2=1
        print("Your Fibonacci sequence is ", num1, " ", sep="", end="")
        for i in range(1,a):
            num1, num2 = num2, (num1+num2)
            print(num1, " ", sep="", end="")
        print()
    else:
        print("You have entered zero. This has returned no terms.")



# program to check entered integer and call function if appropriate  
length = int(input("Please enter the number of terms in the Fibonacci Sequence you would like: "))
if length < 0:
    print("Error: Number entered was less than 0.")
else:
    fibonacci(length)
