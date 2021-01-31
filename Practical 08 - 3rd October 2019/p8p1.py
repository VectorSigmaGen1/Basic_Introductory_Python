# program to list which of 2,3,5 & 7 an entered number is divisible by and to display same

"""
Pseudocode

Set num = 0
WHILE input >= 0;
    Request input
    Print "Please enter your first number: "
    IF input mod 2 = 0 AND input >= 0:
        print input "is divisible by 2"
    IF input mod 3 = 0 AND input >= 0:
        print input "is divisible by 3"
    IF input mod 5 = 0 AND input >= 0:
        print input "is divisible by 5"
    IF input mod 7 = 0 AND input >= 0:
        print input "is divisible by 7"
print "Finished!"

"""

num = int(0)
while num >= 0:
    num = int(input('Please enter your number (If you wish to terminate the program, please enter a negative number): '))
    if (num%2)==0 and num >=0:
        print(num, 'is divisible by 2')
    if (num%3)==0 and num >=0:
        print(num, 'is divisible by 3')
    if (num%5)==0 and num >=0:
        print(num, 'is divisible by 5')
    if (num%7)==0 and num >=0:
        print(num, 'is divisible by 7')
print('Finished!')

    
              
        
        
