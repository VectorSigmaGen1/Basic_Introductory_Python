# program to compare 3 inputs and print the largest odd number if one is present

'''

request input1
request input2
request input3

IF input1 is even
    set input1=0
IF input2 is even
    set input2=0
IF input3 is even
    set input3=0
IF input1 > (input2 and input3)
    print input1
IF input2 > (input1 and input3)
    print input2
IF input3 > (input1 and input2)
    print input3
ELSE
    print 'None of these numbers is odd'


'''
Num1 = int(input('Please enter the first number: '))
Num2 = int(input('Please enter the second number: '))
Num3 = int(input('Please enter the third number: '))
# Sets any even numbers to 0 so that they will be less than any odd numbers
# This solution only works for positive integers
if Num1%2==0:
    Num1=0
if Num2%2==0:
    Num2=0
if Num3%2==0:
    Num3=0
if Num1>(Num2 and Num3):
    print (Num1)
elif Num2>(Num1 and Num3):
    print (Num2)
elif Num3>(Num1 and Num2):
    print (Num3)
else:
    print ('None of these numbers is odd')

    
