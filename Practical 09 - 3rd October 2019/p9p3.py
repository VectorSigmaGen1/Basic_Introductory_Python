# program to calculate the factorial of an entered integer

"""
Pseudocode

Set num = 0
WHILE input >= 0;
    Request input
    Print "Please enter a positive integer (If you wish to terminate the program, please enter a negative integer): "
    run = 1
    for i in range(1, input+1, 1)
        run = run * i
    if input >= 1
        print 'The factorial of the integers up to and including your number is: ', run
print 'You have entered a negative integer'
print 'Program Terminated'


"""


num = int(0)
while num >= 0:
    num = int(input('Please enter a positive integer (If you wish to terminate the program, please enter a negative integer): '))
    run = 1
    for i in range(1, num+1):
        run *= i
    if num >= 0:
        print('The factorial of the integers up to and including your number is: ', run)
print('You have entered a negative integer')
print('Program Terminated')


    
              
        
        
