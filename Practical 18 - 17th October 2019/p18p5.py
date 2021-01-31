# function that takes a string as an argument and returns True if the given string
# contains an appearance of "xyz" where the "xyz" is not directly preceeded by a period

"""
Pseudocode

Define function 'strchk5(s)'
    set variable 'length' = the length of string 's'
    initialise variable 'count' with value 0
    FOR 'i' in range(start = 0, end = 'length'-3, step=1)
        IF 's' character [i] is not equal to .
            IF 's' character [i+1] = x
                IF 's' character [i+2] = y
                    IF 's' character [i+3] = z
                        'count' = 'count' + 1
    IF 'count' = 0
        RETURN FALSE
    ELSE
        RETURN TRUE
    


"""





def strchk5(s):
    length=len(s)
    count=0
    for i in range(length-3):
        if s[i]!=".":
            if s[i+1]=="x":
                if s[i+2]=="y":
                    if s[i+3]=="z":
                        count+=1
    if count == 0:
        return False
    else:
        return True
    
# Container to request arguement and call function    
s = str(input("Please enter a string: "))    
print(strchk5(s))
