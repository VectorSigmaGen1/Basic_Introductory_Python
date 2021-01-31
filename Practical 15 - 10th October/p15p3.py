# program that takes as input a series of integers >= 0
# and for each integer prints that number of terms of a function
# Uses recursion

"""
Pseudocode

DEFINE function 'func3'
    IF variable 'x' = 0
        RETURN 13
    ELIF variable 'x' = 1
        RETURN 8
    ELSE
        RETURN func3(x-2) + 13*func3(x-1)

request the user to enter an integer and assign it to variable 'x'
Print "Please enter an integer equal or greater than 0: "
WHILE x>= 0
    print "The first" 'x' "terms of the function are: " and suppress newline
    FOR 'i' in range(start-0, end-x+1, iteration-1)
        print func3(i) and suppress newline
    Print newline
    request the user to enter an integer and assign it to variable 'x'
    Print "Please enter another integer equal to or greater than 0: "
print "You have entered a negative integer. The program will now terminate"

"""



def func3(x):
    if x == 0:
        return 13
    elif x == 1:
        return 8
    else:
        return func3(x-2) + 13*func3(x-1)

x = int(input("Please enter an integer equal or greater than 0: "))
while x>=0:
    print("The first", x, "terms of the function are: ", end="")
    for i in range(x+1):
        print(func3(i), end = ', ')
    print("")
    x = int(input("Please enter another integer equal to or greater than 0: "))
print("You have entered a negative integer. The program will now terminate")
