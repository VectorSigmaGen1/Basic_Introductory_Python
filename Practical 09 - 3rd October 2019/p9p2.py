# program to calculate the sum of numbers up to and including an entered integer
# for multiple integer entries

"""
Pseudocode

Set num = 0
WHILE input >= 0;
    Request input
    Print "Please enter a positive integer (If you wish to terminate the program, please enter a negative integer): "
    run = 0
    for i in range(0, input+1, 1)
        run = run plus i
    print 'The sum of the integers up to and including your number is: ', run
print 'You have entered a negative integer'
print 'Program Terminated'


"""


num = int(0)
while num >= 0:
    num = int(input('Please enter a positive integer (If you wish to terminate the program, please enter a negative integer): '))
    run = 0
    for i in range(num+1):
        run += i
    if num>=0:
        print('The sum of the integers up to and including your number is: ', run)
print('You have entered a negative integer')
print('Program Terminated')


    
              
        
        
