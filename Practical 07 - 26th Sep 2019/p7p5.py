# This is a program to add the integers from 1 to 10,000
# that are divisible by 3 or by 5 and give a total.


'''


print 'This is a program to add the integers from 1 to 10,000 that are divisible by 3 or by 5 and give a total.'
set variable=int(0)
set sum=int(0)
While variable<=10000
    IF Num Mod3 = 0 or Num Mod5 = 0
        set sum=sum+variable
set variable=variable+1
print 'the program is now complete.'
print 'The sum of all of the integers from 1 to 10,000 that are divisible by 3 or by 5 is', Sum


'''

print ('This is a program to add the integers from 1 to 10,000 that are divisible by 3 or by 5 and give a total.')
Num=int(0)
Sum=int(0)
while Num<=10000:
    if (Num%3)==0 or (Num%5)==0:
        Sum=(Sum+Num)
    Num=(Num+1)
print ('The program is now complete.')
print ('The sum of all of the integers from 1 to 10,000 that are divisible by 3 or by 5 is', Sum)
