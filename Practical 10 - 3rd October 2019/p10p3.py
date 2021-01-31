# program to calculate the numbers of vowels in an entered string

"""
PSEUDOCODE

request input for a string and set it equal to the variable string
print "Please enter a string (Press Enter to Finish): "
WHILE string is not equal to an empty string:
    assign the value of 0 to a variable a1
    assign the value of 0 to a variable e1
    assign the value of 0 to a variable i1
    assign the value of 0 to a variable o1
    assign the value of 0 to a variable u1
    for each character in string
        if character = "a":
            add 1 to a1
        if character = "e":
            add 1 to e1
        if character = "i":
            add 1 to i1
        if character = "o":
            add 1 to o1
        if character = "u":
            add 1 to u1
    print "Your string contained the following numbers of each vowel: "
    print "The letter A was typed", a1, "times"
    print "The letter E was typed", e1, "times"
    print "The letter I was typed", i1, "times"
    print "The letter O was typed", o1, "times"
    print "The letter U was typed", u1, "times"
    request input for a string and set it equal to the variable string
    print "Please enter a string (Press Enter to Finish): "
print "The program has been terminated"



"""

string = input('Please enter a string (Press Enter to Finish): ')
while string!="":
    a1=0
    e1=0
    i1=0
    o1=0
    u1=0
    for ch in string:
        if ch=="a":
            a1+=1
        if ch=="e":
            e1+=1
        if ch=="i":
            i1+=1
        if ch=="o":
            o1+=1
        if ch=="u":
            u1+=1
    print("Your string contained the following numbers of each vowel: ")
    print("The letter A was typed", a1, "times")
    print("The letter E was typed", e1, "times")
    print("The letter I was typed", i1, "times")
    print("The letter O was typed", o1, "times")
    print("The letter U was typed", u1, "times")
    string = input('Please enter a string (Press Enter to Finish): ')
print("The program has been terminated")

