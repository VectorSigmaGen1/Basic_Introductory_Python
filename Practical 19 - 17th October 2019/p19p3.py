# Program that reads a le and checks that brackets (ie ( and ), < and >, { and } and [ and ]) are balanced.

"""
Pseudocode

Import the module 'os'
Assign the variable 'file1' to the string "Page.html"
Use the os.path.isfile() command to check if file1 exists
IF the file doeen't exist
    print "File" 'file1' "does not exist"
ELSE
    open the file for reading and assign it to file handle 'fh1'
Initialise the list 'countlist' and assign it 8 values, all 0
output each of the lines in fh1 to a list 'L' using the command .readlines()
close fh1
Initialise list 'L2' = ["(", ")", "<", ">", "{", "}", "[", "]"]
FOR 's' in 'L'
    FOR 'i' in range(start=0, end='length of 's'', step=1)
        FOR 'b' in range(start=0, end=8, step=1)
            IF 's' character [i] = L2 entry [b]
                add 1 to countlist position [b]


Initialise variable 'c'=0
FOR 'i' in range(start=0, end=8, step=1)
    print "The number of times" L2[i] "appears in the file is" countlist[i]
    c = c + countlist[i]
print 2 newlines
IF c modulus 2 = 0
    print "This file has balanced brackets"
ELSE
    print "This file does NOT have balanced brackets" 


"""


import os
file1="Page.html"
if not os.path.isfile(file1):
    print("File " + file1 + " does not exist.")
else:
    fh1=open(file1, 'r')
countlist = [0 for i in range (8)]
L=fh1.readlines()
fh1.close()
L2 = ["(", ")", "<", ">", "{", "}", "[", "]"]
for s in L:
    for i in range(len(s)):
        for b in range(8):
            if s[i]==L2[b]:
                countlist[b]+=1
# Although the question said to "return" the total number of each bracket, it asked for a program, not a function, so I printed the numbers to screen
c=0
for i in range(8):
    print("The number of times", L2[i], "appears in the file is", countlist[i])
    c+=countlist[i]
print("\n"*2)
if c%2==0:
    print("This file has balanced brackets")
else:
    print("This file does NOT have balanced brackets")   


