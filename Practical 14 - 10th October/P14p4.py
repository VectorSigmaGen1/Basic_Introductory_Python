# Program to illustrate the use of the else statement on a for loop
# Program searches for Prime Numbers in a range of Integers
"""
Pseudocode

FOR 'num' in range(start-2, end-20, increment-1)
    set variable 'count' = 0
    FOR 'i' in range(start-2, end-num, increment-1)
        IF 'num' % 'i' = 0
            set 'count' = 'count' + 1
            print 'num' "equals" 'i' "*" 'num'/'i'
    IF count = 0:
        print 'num' "is a prime number"


"""

for num in range(2, 20):
    count=0
    for i in range (2, num):
        if num % i == 0:
            count += 1
            print(num, "equals", i, "*", num//i)
    if count == 0:
        print(num, "is a prime number")
