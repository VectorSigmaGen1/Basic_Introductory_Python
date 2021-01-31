# Program to illustrate scoping in Python


"""
Pseudocode

DEFINE function 'f' of variable 'x'
    PRINT "In function f:"
    Set x = x+1
    Set y = 1
    PRINT "x is", 'x'
    PRINT "y is", 'y'
    PRINT "z is", 'z'
    RETURN 'x'

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



def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print("In function f:")
    x+=1
    y=1
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x

x, y, z = 5, 10, 15

print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)

z=f(x)

print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)

