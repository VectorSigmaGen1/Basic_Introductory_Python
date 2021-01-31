# program to add the first 5000 integers and give an answer
# for this program, I've used the first 5000 positive integers,
# starting with 0 and ending with 4999.

"""


print 'This is a program to add the integers 0 to 4999 and give a total'
set variable=int(0)
set sum=int(0)
While variable <5000
    set sum=sum+variable
    set variable=variable+1
print 'the program is now complete'
print 'The sum of all of the integers from 0 to 4999 is', sum


"""

print('This is a program to add the integers from 0 to 4999 and give a total')
Num = int(0)
Sum = int(0)
while Num < 5000:
    Sum = (Sum+Num)
    Num = (Num+1)
print('The program is now complete')
print('The sum of all of the integers from 0 to 4999 is', Sum)
