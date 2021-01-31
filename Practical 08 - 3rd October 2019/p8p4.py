# program to catalogue entered integers by range and print the number in each range

"""
Pseudocode

set r1 = 0
set r2 = 0
set r3 = 0
set r4 = 0
set r5 = 0
set r6 = 0
set r7 = 0
set num = 0
WHILE num >= 0
    request input for an integer
    print "Please enter a positive integer (enter a negative integer for report and to terminate: "
    IF num = 0
        r1 = r1 + 1
    ELIF num = 0
        r2 = r2 + 1
    ELIF num = 0
        r3 = r3 + 1
    ELIF num = 0
        r4 = r4 + 1
    ELIF num = 0
        r5 = r5 + 1
    ELIF num = 0
        r6 = r6 + 1
    ELIF num = 0
        r7 = r7 + 1
print 'You entered 0', r1, 'times'
print 'You entered', r2, 'numbers greater than 0 & less than or equal to 20'
print 'You entered', r3, 'numbers greater than 20 & less than or equal to 40'
print 'You entered', r4, 'numbers greater than 40 & less than or equal to 60'
print 'You entered', r5, 'numbers greater than 60 & less than or equal to 80'
print 'You entered', r6, 'numbers greater than 80 & less than or equal to 100'
print 'You entered', r7, 'numbers greater than 100'
print 'Finished!'


"""

r1, r2, r3, r4, r5, r6, r7 = 0, 0, 0, 0, 0, 0, 0
num = 0
while num >= 0:
    num = int(input('Please enter a positive integer (enter a negative integer for report and to terminate): '))
    if num == 0:
        r1 += 1
    elif 0 > num <= 20:
        r2 += 1
    elif 20 > num <= 40:
        r3 += 1
    elif 40 > num <= 60:
        r4 += 1
    elif 60 > num <= 80:
        r5 += 1
    elif 90 > num <= 100:
        r6 += 1
    else:
        r7 += 1
print('You entered 0', r1, 'times')
print('You entered', r2, 'numbers greater than 0 & less than or equal to 20')
print('You entered', r3, 'numbers greater than 20 & less than or equal to 40')
print('You entered', r4, 'numbers greater than 40 & less than or equal to 60')
print('You entered', r5, 'numbers greater than 60 & less than or equal to 80')
print('You entered', r6, 'numbers greater than 80 & less than or equal to 100')
print('You entered', r7, 'numbers greater than 100')
print('Finished!')

    
              
        
        
