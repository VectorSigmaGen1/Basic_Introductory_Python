# program that takes as input a series of integers >= 1
# and for each integer prints that number of terms of a function
# Uses recursion

"""
Pseudocode

DEFINE function 'func1'
    IF variable 'x' = 0
        RETURN 2
    ELSE
        RETURN x + func1(x-1)

request the user to enter an integer and assign it to variable 'x'
Print "Please enter an integer equal to 1 or greater: "
WHILE x>= 1
    print "The first" 'x' "terms of the function are: " and suppress newline
    FOR 'i' in range(start-1, end-x+1, iteration-1)
        print func1(i) and suppress newline
    Print newline
    request the user to enter an integer and assign it to variable 'x'
    Print "Please enter another integer equal to or greater than 1: "
print "You have entered either zero or a negative integer. The program will now terminate"

"""



def func1(x):
    if x == 1:
        return 2
    else:
        return x + func1(x-1)


x = int(input("Please enter an integer equal to 1 or greater: "))
while x>=1:
    print("The first", x, "terms of the function are: ", end="")
    for i in range(1, x+1):
        print(func1(i), end = ', ')
    print("")
    x = int(input("Please enter another integer equal to or greater than 1: "))
print("You have entered either zero or a negative integer. The program will now terminate")

    
