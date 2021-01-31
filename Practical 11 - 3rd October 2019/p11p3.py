# Program to check if an entered integer is a positive integer and if so to display that number of terms from the Fibonacci Sequence


"""
Pseudocode

request the input of an integer and assign it to variable 'length'
print "Please enter the number of terms in the Fibonacci Sequence you would like: "
WHILE length >= 0
    IF length > 0
        set variable 'num1' = 0
        set variable 'num2' = 1    
        print "Your Fibonacci sequence is " num1 and suppress newline
        FOR i in range (1, length)
            set new value of num1 = current value of num 2
            set new value of num2 = num1 + num2
            print num1
        print newline
    ELSE
        print "You have entered zero. This has returned no terms."
    request the input of an integer and assign it to variable 'length'
    print "Please enter the number of terms in the Fibonacci Sequence you would like: "
print "You have entered a negative number - it isn't possible to display a negative number of terms. Please run the program again."


"""


length=int(input("Please enter the number of terms in the Fibonacci Sequence you would like: "))
while length>=0:
    if length>0:
        num1=0
        num2=1
        print("Your Fibonacci sequence is ", num1, " ", sep="", end="")
        for i in range(1, length):
            num1, num2 = num2, (num1+num2)
            print(num1, " ", sep="", end="")
        print()
    else:
        print("You have entered zero. This has returned no terms.")
    length=int(input("Please enter the number of terms in the Fibonacci Sequence you would like: "))
print("You have entered a negative number - it isn't possible to display a negative number of terms. Please run the program again.")
    

