# program that takes a page, counts the occurrences of left angle brackets (<), right angle brackets (>),
# newlines, the lowercase letter e, the string <!-- and the string --> and prints out the results to a le results.txt.

"""
Pseudocode

Import the module 'os'
Assign the variable 'file1' to the string "Page.html"
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
output the entirety of fh1 to a string 's' using the command .read()
Close fh1
Initialise list 'L2' = ["<", ">", "<br>", "e", "<!--", "-->"]
FOR 'b' in range(start=0, end=6, step=1)
    assign the entry in countlist at position [b]=
        the entry in countlist at position [b] + the number of times the entry in 'L2' at position [b])
            appears in string 's'
FOR 'i' in range(start=0, end=6, step=1)
    write to fh2 using the .write() command
        "The number of times "
        str(L2[i])
        "appears in the file is "
        str(countlist[i])
        newline

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
# I decided to change the reading method from 'readlines() to .read() ie. the whole file at once,
# as with html files, multiple character strings such as "<br>" may be broken up over 2 lines and so
# reading one line at a time might underestimate the number of occurances
s=fh1.read()
fh1.close()
L2 = ["<", ">", "<br>", "e", "<!--", "-->"]
for b in range(6):
    countlist[b]+=s.count(L2[b])
for i in range(6):
    fh2.write("The number of times ")
    fh2.write(str(L2[i]))
    fh2.write(" appears in the file is ")
    fh2.write(str(countlist[i]))
    fh2.write("\n")
fh2.close()
print("The program has succesfully searched your file and you can review the results in the file \"results.txt\".")
