# program that takes a page, counts the occurrences of left angle brackets (<), right angle brackets (>),
# newlines, the lowercase letter e, the string <!-- and the string --> and prints out the results to a le results.txt.

"""
Pseudocode

Import the module 'os'
Ask the user to input the name of the file to be searched and set the variable 'file1' = the filename
Use the os.path.isfile() command to check if the file exists
IF the file doeen't exist
    print "File" 'file1' "does not exist"
ELSE
    open the file for reading and assign it to file handle 'fh1'
WHILE a file called 'results.txt' exists
    print "There is already a file called 'results.txt' in the active folder. Please move or delete this file and press enter to continue."
    requesting an input so that the program won't continue the loop until the user presses enter.
Create and open a file for writing called 'results.txt' and assign it to file handle 'fh2'
Initialise the list 'countlist' and assign it 6 values, all 0
output each of the lines in fh1 to a list 'L' using the command .readlines()
FOR 's' in 'L'
    set variable 'length' = the length of 's'
    FOR 'i' in range(start=0, end='length', step=1)
        IF 's' character [i] = <
            add 1 to countlist position 0
                IF i+3<length
                    IF 's' character [i+1] = b
                        IF 's' character [i+2] = r
                            IF 's' character [i+3] = >
                                add 1 to countlist position 2
                    ELIF 's' character [i+1] = !
                        IF 's' character [i+2] = -
                            IF 's' character [i+3] = -
                                add 1 to countlist position 4
        IF 's' character [i] = >
            add 1 to countlist position 1
        IF 's' character [i] = e
            add 1 to countlist position 3
        IF i+2 < length AND 's' character [i] = -
                IF 's' character [i+1] = -
                    IF 's' character [i+2] = >
                        add 1 to countlist position 5
Initialise list 'L2' = ["<", ">", "<br>", "e", "<!--", "-->"]
Initialise variable 'x'=0
FOR 'i' in range(start=0, end=6, step=1)
    write to fh2 using the .write() command
        "The number of times "
        str(L2[x])
        "appears in the file is "
        str(countlist[x])
        newline
        x = x + 1
Close fh1
Close fh2
print "The program has succesfully searched your file and you can review the results in the file "results.txt."

"""


import os
file1="Page.html"
if not os.path.isfile(file1):
    print("File " + file1 + " does not exist.")
else:
    fh1=open(file1, 'r')
while os.path.isfile("results.txt"):
    input("There is already a file called 'results.txt' in the active folder. Please move or delete this file and press enter to continue.")
fh2=open("results.txt", 'w')
countlist = [0 for i in range (6)]
L=fh1.readlines()
L2 = ["<", ">", "<br>", "e", "<!--", "-->"]
for s in L:
    for b in range(6):
        countlist[b]+=s.count(L2[b])
for i in range(6):
    fh2.write("The number of times ")
    fh2.write(str(L2[i]))
    fh2.write(" appears in the file is ")
    fh2.write(str(countlist[i]))
    fh2.write("\n")
fh1.close()
fh2.close()
print("The program has succesfully searched your file and you can review the results in the file \"results.txt\".")
