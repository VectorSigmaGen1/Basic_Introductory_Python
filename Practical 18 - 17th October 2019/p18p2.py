# Function to take a string as an arguement and return the number of times the string "code" appears in the string.

"""
Pseudocode

DEFINE function 'strcount(s)'
    get the length of 's' and assign it to variable 'length'
    set variable 'count' = 0
    FOR 'i' in range (start = 0, end = length-3, iteration = 1)
        IF s character [i] = "c"
            IF s character[i+1]="o"
                IF s character [i+2] = "d"
                    IF s character [1+3] = "e"
                        count = count + 1
    print "The string "code" appears" count "times in your string"
    RETURN count
            

"""

# Since this is far too easy with the s.count function, I'm assuming we are to do it from first principles?
def strcount(s):
    length=len(s)
    count=0
    for i in range(length-3):
        if s[i]=="c":
            if s[i+1]=="o":
                if s[i+2]=="d":
                    if s[i+3]=="e":
                        count+=1
    print("The string \"code\" appears", count, "time(s) in your string")
    return count

# Container to request arguement and call function
s=str(input("please enter a string to check: "))
strcount(s)
