# Program to illustrate scoping in Python
# Added extra variables and operations



"""
Pseudocode

DEFINE function 'f' of variable 'x' and variable 'y'
    PRINT "In function f:"
    Set x = x+1
    Set y = y * 2
    set z = x-1
    PRINT "x is", 'x'
    PRINT "y is", 'y'
    PRINT "z is", 'z'
    RETURN 'x' & 'y'

Set x = 5
Set y = 10
Set z = 15

print "Before function f:"
print "x is", 'x'
print "y is", 'y'
print "z is", 'z'

CALL function 'f'

print "After function f:"
print "x is", 'x'
print "y is", 'y'
print "z is", 'z'

"""



def f(x, y):
    """Function that adds 1 to its argument and prints it out"""
    print("In function f:")
    x+=1
    y*=2
    z=x-1
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x, y


x, y, z = 5, 10, 15

print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)

x, y=f(x, y)

print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)

