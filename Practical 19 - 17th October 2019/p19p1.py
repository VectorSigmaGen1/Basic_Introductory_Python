# function that takes as arguements a number in base 10, and a base,
# both positive ints, and, using the algorithm presented in lectures,
# returns the number in the base supplied.

"""
Pseudocode

Define the function 'basecal(x,y)'
    Initialise a tuple 'p' 
    WHILE x>0
        p=p+(x modulus y)
        x=the quotient of x/y
    q = p reveresed
    initialise string 's' with null value
    FOR 'i' in range(start=0, end=length of q, step=1)
        s = s + (the entry at position 'i' in tuple 'q') - converted to a string
    RETURN 's'

"""

"""
Pseudocode for container program

Request that the user inputs the number in base 10 to be converted assign it as an integer to variable 'x'
Request that the user inputs the base to convert the number to and assign it as an integer to the variable 'y'
print "The answer = " convdec(x,y)

"""

def basecalc(x,y):
    p=()
    while x>0:
        p+=(x%y,)
        x=x//y
    # The order has to be reversed as the first modulus returned is the last digit of the converted number
    q=p[::-1]
    # Returning the answer as a string looks better, but for clarity it might be better to leave it as a tuple for numbers with a base larger than 9
    # Though in that case letters are usually assigned.
    s=""
    for i in range(len(q)):
        s+=str(q[i])
    return(s)



x=int(input("Please enter a number in base 10: "))
y=int(input("Please enter a base to convert the number to: "))
print("The answer = ", basecalc(x,y))
