# program to calculate the integer cube root of a series of entered integers

"""
PSEUDOCODE

request input for a positive integer and assign to variable num
print "Please enter the positive integer you wish to calculate the square root of
       (Enter a zero to exit program): "
WHILE num != 0
    assign the value of 0 to a variable root
    IF num < 0
        THEN num2 = -num
    ELSE THEN num2 = num

    WHILE root cubed < num2
        root = root + 1
    IF root cubed is exactly equal to num2
        IF num < 0
            root = -root
        print "The cube root of"  num  "is" root
    ELSE
        print num "is not a perfect cube."
print "You have entered a zero. The program is terminated"


"""

num = int(input('Please enter the integer you wish to calculate the square root of\n(Enter a 0 to exit program): '))
while num  != 0:
    root = 0
    if num<0:
        num2=-num
    else:
        num2=num
    while root**3 < num2:
        root += 1
    if root**3 == num2:
        if num<0:
            root=-root
        print('The cubed root of', num, 'is', root)
    else:
        print(num, 'is not a perfect cube.')
    num = int(input('Please enter another positive integer you wish to calculate the square root of\n(Enter a zero to exit program): '))
print('You have entered a zero\nThe program is terminated')
