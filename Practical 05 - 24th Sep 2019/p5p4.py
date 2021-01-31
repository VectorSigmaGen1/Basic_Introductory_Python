# program to take input of an integer and print one of a series of messages based on qualifying ranges

Entry = int(input('Enter an integer: '))
if Entry == 0:
    print('Number is equal to 0')
elif Entry > 0 and Entry <= 20:
    print('Number is greater than 0 and less than or equal to 20')
elif Entry > 20 and Entry <= 40:
    print('Number is greater than 20 and less than or equal to 40')
elif Entry > 40 and Entry <= 60:
    print('Number is greater than 40 and less than or equal to 60')
elif Entry > 60 and Entry <= 80:
    print('Number is greater than 60 and less than or equal to 80')
elif Entry > 80 and Entry <= 100:
    print('Number is greater than 80 and less than or equal to 100')
elif Entry > 100:
    print('Number is greater than 100')
else:
    print('Number is negative')
    
