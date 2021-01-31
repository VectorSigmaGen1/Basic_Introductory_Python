# program to display a number of terms of the Fibonacci Sequence based on input


"""

Pseudocode

Request input and assign to the variable 'length'
Print "Please enter the number of terms in the Fibonacci Sequence you would like: "
IF length > 0
    set variable 'count' = 0
    set variable 'num1' = 0
    set variable 'num2' = 1
    print "Your Fibonacci sequence is " num1 and suppress newline
    WHILE count < length-1
        set num1 = current value of num 2
        set new value of num2 = num1 + num2
        print num1
        set count = count + 1
    print newline
ELIF length = 0
    print "You have entered zero. This has returned no terms."
ELSE
    print "You have entered a negative number - it isn't possible to display a negative number of terms. Please run the program again."


"""


length=int(input("Please enter the number of terms in the Fibonacci Sequence you would like: "))
if length>0:
    count=0
    num1=0
    num2=1
    print("Your Fibonacci sequence is ", num1, " ", sep="", end="")
    while count<length-1:
        num1, num2 = num2, (num1+num2)
        print(num1, " ", sep="", end="")
        count+=1
    print()
elif length==0:
    print("You have entered zero. This has returned no terms.")
else:
    print("You have entered a negative number - it isn't possible to display a negative number of terms. Please run the program again.")
    

