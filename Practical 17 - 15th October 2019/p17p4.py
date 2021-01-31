# Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Exits when an empty string is entered

"""

Pseudocode

define the function 'isPalindrome(s)'
    define the function 'toChars(s)'
        set s = s.lower() to convert the string to all lowercase letters
        initialise the string 'letterstring' with an empty value.
        FOR c in s
            if c in "abcdefghijklmnopqrstuvwxyz"
                'letterstring' = 'letterstring' + c
        RETURN 'letterstring'
    define the function 'isPal(s)
        IF the length of s is <= 1
            RETURN True
        ELSE
            RETURN s[0] = s[-1] and isPal(s[1:-1])
    RETURN isPal(toChars(s))
request the user to enter a string and assign it to variable 'str'
Print "Please enter a string (empty string to exit): "
WHILE str is not an empty string
    IF isPalindrome(str)
        print 'str' "is a palindrome"
    ELSE
        print 'str' "is not a palindrome"
    request the user to enter a string and assign it to variable 'str'
    print "Enter a string (empty string to exit): "
print "Finished"

   
"""



def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        letterstring = ''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                letterstring += c
        return letterstring
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
str = input("Please enter a string (empty string to exit): ")
while str != "":
    if isPalindrome(str):
        print(str, "is a palindrome")
    else:
        print(str, "is not a palindrome")
    str = input("Enter a string (empty string to exit): ")
print("Finished")                
