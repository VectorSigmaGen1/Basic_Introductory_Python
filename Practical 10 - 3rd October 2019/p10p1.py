# program to calculate the positive integer square root of a series of entered positive integer

"""
PSEUDOCODE

request input for a positive integer and assign to variable num
print "Please enter the positive integer you wish to calculate the square root of
       (Enter a negative integer to exit program): "
WHILE num >= 0
    assign the value of 0 to a variable root
    WHILE root squared < num
        root = root + 1
    IF root squared is exactly equal to num
        THEN print"The square root of"  num  "is" root
    ELSE THEN
        print num "is not a perfect square."
print "You have entered a negative integer. The program is terminated"


"""

num = int(input('Please enter the positive integer you wish to calculate the square root of\n(Enter a negative integer to exit program): '))
while num  >= 0:
    root = 0
    while root**2 < num:
        root += 1
    if root**2 == num:
        print('The square root of', num, 'is', root)
    else:
        print(num, 'is not a perfect square.')
    num = int(input('Please enter another positive integer you wish to calculate the square root of\n(Enter a negative integer to exit program): '))
print('You have entered a negative integer\nThe program is terminated')
