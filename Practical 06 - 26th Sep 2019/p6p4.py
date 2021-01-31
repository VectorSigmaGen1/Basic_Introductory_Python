# program to count incorrect entries of a password
# print a speciic response if entered incorrectly more than 3 times

'''


PSUEDOCODE:
Set count = 1
Set passc = 0
WHILE
    count <= 4 AND passc = 0
    request input
        print 'Please enter the password'
    IF input = 'John'
        THEN set passc = 1
            print 'You have successfully logged in'
    ELSE
        count = count + 1
IF passc = 0
    print 'You have been denied access'


'''

count = 1
passc = 0
while count <=4 and passc==0:
        attempt = str(input('Please enter the password: '))
        if attempt==('John'):
            # breaks loop after successful entry
            passc=1
            print ('You have successfully logged in')
        else:
            # breaks loop after 4 unsuccesful entries (more than 3)
            count=count+1
# Doesn't print statement if loop broken by successful entry
if passc==0:
    print ('You have been denied access')
            
