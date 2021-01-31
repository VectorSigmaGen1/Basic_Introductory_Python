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
if input1=0 and (input2 and input3)!=0
    if input2>input3
        print input2
    else:
        print input3
elif input2=0 and (input1 and input3)!=0
    if input1>input3
        print input1
    else:
        print input3
elif input3=0 and (input1 and input2)!=0
    if input1>input2
        print input1
    else:
        print input2
elif (input1 and input2)=0 and input3!=0
    print input3
elif (input1 and input3)=0 and input2!=0
    print input2
elif (input2 and input3)=0 and input1!=0
    print input1
ELSE
    print 'None of these numbers is odd'


'''
Num1 = int(input('Please enter the first number: '))
Num2 = int(input('Please enter the second number: '))
Num3 = int(input('Please enter the third number: '))
# Sets any even numbers to 0 so that they will be less than any odd numbers
# This solution only works for all integers both positive and negative
if Num1%2==0:
    Num1=0
if Num2%2==0:
    Num2=0
if Num3%2==0:
    Num3=0
# Removes Num1 if it was even and the other two are odd
if Num1==0 and (Num2 and Num3)!=0:
    if Num2>Num3:
        print (Num2)
    else:
        print (Num3)
# Removes Num2 if it was even and the other two are odd
elif Num2==0 and (Num1 and Num3)!=0:
    if Num1>Num3:
        print (Num1)
    else:
        print (Num3)
# Removes Num3 if it was even and the other two are odd
elif Num3==0 and (Num1 and Num2)!=0:
    if Num1>Num2:
        print (Num1)
    else:
        print (Num2)
# prints Num3 if the other two were even
elif (Num1 and Num2)==0 and Num3!=0:
    print (Num3)
# prints Num2 if the other two were even
elif (Num1 and Num3)==0 and Num2!=0:
    print (Num2)
# prints Num1 if the other two were even
elif (Num2 and Num3)==0 and Num1!=0:
    print (Num1)
# prints the statement if they were all even
else:
    print ('None of these numbers is odd')

    
