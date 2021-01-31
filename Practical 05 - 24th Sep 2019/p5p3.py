# program to print a message indicating if a float is positive, negative or equal to 0

Entry = float(input('Enter a floating point number: '))
if Entry > 0:
    print('This is a positive floating point number')
elif Entry == 0:
    print('This number is zero')
else:
    print('This is a negative floating point number')
    
