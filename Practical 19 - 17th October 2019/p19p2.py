# Function that takes a string of digits, representing a number,
# and a base (an int) as arguments, and returns the number in decimal (Base 10).
# The digits can include the letters A-F (uppercase and lowercase), so that hexadecimal numbers can be supplied and converted.

"""
Pseudocode

define the function 'convdec(x,y)
    apply the .lower() function to 'x' to convert any capitals to lowercase in the string
    Initialise a list and call it 'L'
    FOR 'i' in 'x'
        'L' = 'L+i'
    FOR 'i' in range(start=0, end = length of 'L', step = 1)
        initialise variable 'd' as the string 'abcdef'
        FOR 't'in range(start=0, end=6, step=1)
            IF the entry at position 'i' in 'L' is equal to the entry at position 't' in 'd'
                Change the value of the entry at position 'i' in 'L' to ('t' + 10)
        Change the value of the entry at position 'i' in 'L' to an integer and multiply it by 'y' to the power of (the length of L -1 -'i')
    Initialise the variable 'ans' as 0
    FOR 'e' in L
        ans = ans + 'e'
    RETURN ans

   
"""

"""
Pseudocode for container program

Request that the user inputs the number to be converted and assign it as a string to variable 'x'
Request that the user inputs the base of the number entered and assign it as an integer to the variable 'y'
print "Your number in decimal(base 10) is" convdec(x,y)

"""


def convdec(x,y):
    # convert any capitals to lowercase
    x=x.lower()
    L=[]
    for i in x:
        L+=[i]
    for i in range(len(L)):
        # Converts any letters to numbers
        d='abcdef'
        for t in range(6):
            if L[i]==d[t]:
                L[i]=(t+10)
        # converts base 16 numbers to base 10
        L[i]=int(L[i])*(y**(len(L)-1-i))  
    ans=0
    # adds the entries in the list together
    for e in L:
        ans+=e
    return ans
# Container to request arguements and call function   
x=str(input("Please enter the number you wish to convert to decimal: "))
y=int(input("Please enter the base of the number you entered: "))
print("Your number in decimal(base 10) is", convdec(x,y))
