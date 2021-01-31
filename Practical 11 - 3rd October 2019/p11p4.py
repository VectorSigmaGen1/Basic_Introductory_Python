# Program to check if an entered integer is a positive integer and if so to display that number of terms from the Catalan Sequence


"""
Pseudocode

request the input of an integer and assign it to variable 'numa'
print "Please enter an integer: "
WHILE numa >= 0
    print "The first " numa "numbers of the Catalan Sequence are: "
        set variable 'numb' = (numa - 1)
        set variable 'n' = 0    
        WHILE n <= numb
            set variable 'fact' = 1
            FOR i in range (1, n+1)
                fact = (fact * i)
            set variable 'fact2' = 1
            FOR i in range (1, 2n+1)
                fact2 = (fact2 * i)
            set variable 'fact3' = 1
            FOR i in range (1, n+2)
                fact3 = (fact3 * i)
            print"C" n "=" fact2/(fact3*fact)
            suppress newline
            n+=1
        print newline
        request the input of an integer and assign it to variable 'numa'
        print "Please enter an integer: "
print "You have entered a negative integer. The program has now terminated" 


"""



numa = int(input('Please enter an integer: '))
while numa>=0:
    print("The first ", numa, " numbers of the Catalan Sequence are: ", sep = "")
    # as the sequence begins with C0, if the user enters numa, then c numbers run from 0 up to numa-1
    numb = (numa-1)
    n=0
    # while loop out puts c numbers for n=0 up to n=numb
    while n<=numb:
        fact=1
        # caclulates the factorial of n
        for i in range(1, n+1):
            fact *= i
        fact2=1
        # caclulates the factorial of 2n
        for i in range(1, 2*n+1):
            fact2 *= i
        fact3=1
        # caclulates the factorial of n+1
        for i in range(1, n+2):
            fact3 *= i
        # prints each number Cn in the sequence as n increases in value for each run of the outer loop
        print("C",n,"=", fact2//(fact3*fact),", ", sep = "", end = "")
        n+=1
    print("")
    numa = int(input('Please enter an integer: '))
print("You have entered a negative integer. The program has now terminated")
