def fact_rec(x):
    if x == 0:
        return 1
    else:
        return x*fact_rec(x-1)

import time
num = int(input("Please enter an integer to calculate the factorial of: "))
while num<0:
    num = int(input("You have entered a negative integer and unfortunately the factorial of negative integers is undefined. Please enter a positive integer: "))
start = time.time()
print("The factorial of", num, "is", fact_rec(num))
stop = time.time()
print("Elapsed time =", stop-start)
