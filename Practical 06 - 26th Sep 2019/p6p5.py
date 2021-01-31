# Program for to check if password entry is correct
# Require 3 succesful password entries after a failed attempt

'''

PSEUDOCODE:
Set count = 0
Request input
    print 'Please enter the password'
IF input = 'John'
    THEN print ' you have successfully logged on
ELSE
    print ' Sorry the password is wrong'
    print 'Please enter your password 3 consecutive times'
    WHILE count <= 2
        requst input
            print 'Password:'
        IF input = 'John'
            THEN count = count + 1
        ELSE
            print 'You have been denied access'
            Set count = 4
IF 1 <= count <= 3
    THEN print 'You have successfully logged in'
      
'''


count = 0

attempt = str(input('Please enter the password: '))
if attempt==('John'):
    print ('You have successfully logged in')
else:
    print ('Sorry, the password is wrong.')
    print ('Please enter your password 3 consecutive times')
    while count <=2:
        attempt=str(input('Password: '))
        if attempt==('John'):
            # breaks loop after 3 succesful entries
            count = count+1
        else:
            print ('You have been denied access')
            # breaks loop & sends to final if
            count=(4)                                   
# ensures the statement doesn't print if coming from line 3 or coming from line 45
if count <=3 and count >=1:                             
    print ('You have successfully logged in')
            
