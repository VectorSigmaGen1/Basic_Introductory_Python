# Program to check if the strings 'cat' and 'dog' appear the same number of times in a user entered string

"""
Pseudocode

request the user to enter a string and assign it to variable 'string'
Print "Please enter a string of text: "

IF 'string' = ""
    PRINT "You have entered nothing. The program will now terminate"
ELSE
    create a variable called 'total1' and assign it to the output of (string.lower()).count("cat")
    create a variable called 'total2' and assign it to the output of (string.lower()).count("dog")
    IF total1 = total2 = 0
        print "Neither the word 'cat' nor the word 'dog' appears in your sentence"
    ELIF total1 = total2
        print "The word 'cat' appears more times in your sentence than the word 'dog'"
    ELIF total1>total2
        print "The word 'cat' appears more times in your sentence than the word 'dog'"
    ELSE
        print "The word 'dog' appears more times in your sentence than the word 'cat'"
    

"""

string = str(input("Please enter a string of text: "))
if string=="":
    print("You have entered nothing. The program will now terminate")
else:
    total1 = (string.lower()).count("cat")
    total2 = (string.lower()).count("dog")
    if total1==total2==0:
        print("Neither the word 'cat' nor the word 'dog' appears in your sentence")
    elif total1==total2:
        print("The word 'cat' appears the same number of times as the word 'dog' in your sentence")
    elif total1>total2:
        print("The word 'cat' appears more times in your sentence than the word 'dog'")
    else:
        print("The word 'dog' appears more times in your sentence than the word 'cat'")
