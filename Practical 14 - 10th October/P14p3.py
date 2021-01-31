# Program to illustrate the use of the else statement on a for loop
# Program searches for Prime Numbers in a range of Integers
"""
Pseudocode

FOR 'num' in range(start-2, end-20, increment-1)
    Print 'num'
    FOR 'i' in range(start-2, end-num, increment-1)
        print 'i'
        IF 'num' % 'i' = 0
            print 'num' "equals" 'i' "*" 'num'/'i'
            break
    ELSE:
        print 'num' "is a prime number"


"""


for num in range(2, 20):
    print(num)
    for i in range (2, num):
        print(i)
        if num % i == 0:
            print(num, "equals", i, "*", num//i)
            break
    else:
        # loop fell through without finding a factor
        print(num, "is a prime number")
