# program to check if a year entered is a leap year

'''

request input
print 'Please enter the year'
IF input >=0
    IF input mod4=0 and input mod100!=0 or input mod400=0
        print input'is a leap year'
    ELSE
        print input 'is not a leap year'
ELSE
    print 'Please enter a positive year number'


'''

Year = int(input('Please enter the year: '))
if Year>=0:
    if Year%4!=0:
        print (Year, 'is not a leap year')
    elif Year%100!=0:
        print (Year, 'is a Leap Year')
    elif Year%400!=0:
        print (Year, 'is not a leap year')
    else:
        print (Year, 'is a Leap Year')
else:
    print ('Please enter a positive year number')
    
