# program to print different responses base on inputs

'''

request input
IF input = 'John'
    print 'That is a cool name'
ELIF input = 'Mickey Mouse' or 'Spongebob Squarepants'
    print "I'm not sure that is really your name"
ELSE print 'You have a nice name'


'''

Name = str(input('Please enter your name: '))
if Name==('John'):
    print ('That is a cool name!')
elif Name==('Mickey Mouse') or Name==('Spongebob Squarepants'):
    print ("I'm not sure that is really your name.....")
else:
    print ('You have a nice name.')
    
