# program to print a multiplication table from 1 up to an entered value.

"""
Pseudocode

request input for size
print "Please enter the number of lines in your table: "
set row = 1
WHILE row <= size:
    set col = 1
    WHILE col <= size:
        print row * col & space and suppress newline
        col = col + 1
    print newline
    row = row + 1


"""

size = int(input('Please enter your the number of lines in your table: '))
row = 1
while row <= size:
    col = 1
    while col <= size:
        print(row*col, " ", end = "")
        col += 1
    print()
    row += 1

    
              
        
        
