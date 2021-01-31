# program to print a simple multiplication table from 1  20 for an entered value.

"""
Pseudocode

request input for multiple
print "Please enter your the number for your Multiplication Table: "
set row = 0
print newline
print "Times", multiple, "Table"
print "___________"
WHILE row <= 20:
    print "| ", row, " | ", row*fac, " |"
    row = row + 1

"""

fac = int(input('Please enter your the number for your Multiplication Table: '))
row = 0
print()
print('Times', fac, 'Table')
print('_____________')
while row <= 20:
    print('| ', row, ' | ', row*fac, ' |')
    row += 1

    
              
        
        
