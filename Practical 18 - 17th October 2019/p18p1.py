# an iterative version of the isPal function
# Checks whether a supplied string is a palindrome


"""
Pseudocode

DEFINE function 'isPal(s)'
    Get the length of 's' and assign it to variable 'length'
    IF 'length' <=1
        RETURN TRUE
    ELSE
        set variable 'check' = 0
        FOR 'i' in range (start = 0, end = 'length'/2, iteration = 1)
            set variable 'result' = ('s' character[i] = 's' character['length'-1-'i'])
            IF 'result' is FALSE
                change variable 'check' to 1
    IF check is not equal to 0
        variable 'result2' = FALSE
        print 's' "is not a palindrome"
    ELSE
        variable 'result2' = TRUE
        print 's' "is a palindrome"      
    RETURN 'result2'


"""



def isPal(s):
    length = len(s)
    if length <= 1:
        return True
    else:
        check=0
        for i in range(length//2):
            result = s[i]==s[length-1-i]
            if not result:
                check=1             
    if check!=0:
        result2=False
        print(s, "is not a palindrome")
    else:
        result2=True
        print(s, "is a palindrome")
    return result2        

# Container to request arguement and call function
s=str(input("please enter a string for palindrome check: "))
isPal(s)

