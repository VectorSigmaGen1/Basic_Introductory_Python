# Function that takes as it's arguements two strings and returns True if either of the strings
# appears at the very end of the other string, ignoring upper/lower case dierences

"""
Pseudocode

DEFINE function 'strcheck(s)'
    request the user to enter a string and assign it to variable 'str1'
    request the user to enter a string and assign it to variable 'str2'
    take a slice from the end of str1 that is equal in length to str2 and see if the slice is equal to str2
    take a slice from the end of str2 that is equal in length to str1 and see if the slice is equal to str1
    IF either condition is true
    RETURN TRUE
    ELSE
    RETURN FALSE


"""


def strcheck(s1,s2):
    if s1[-len(s2):].lower() == s2 or s2[-len(s1):].lower() == s1:
        return True
    else:
        return False
    
# Container to request arguement and call function
s1 = str(input("Please enter a string: "))
s2 = str(input("Please enter a string: "))
print(strcheck(s1,s2))
