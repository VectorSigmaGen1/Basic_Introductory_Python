# program to add the integers up to an including an entered integer

"""
Pseudocode

request input for an integer
print "Please enter a positive integer: "
IF num >= 0:
    count = 0
    running total = 0
    WHILE
        count <= num
        running total = running total + count
        count = count + 1
    print "The sum of the integers up to and including your number is: ", run
ELSE:
    print 'That number was not a positive integer'
    print 'Program Terminated'


"""

num=0
while num>=0:
    num = int(input('Please enter a positive integer: '))
    if num >= 0:
        count=1
        run=1
        while count <= num:
            run *= count
            count += 1
    print('The factorial of the integers up to and including your number is: ', run)
else:
    print('That number was not a positive integer')
    print('Program Terminated')
    
        
