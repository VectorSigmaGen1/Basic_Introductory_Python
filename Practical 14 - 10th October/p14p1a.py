
def fact_iter(x):
    fact = 1
    i = 1
    while i <= x:
        fact *= i
        i += 1
    return fact

import time
num = int(input("Please enter an integer to calculate the factorial of: "))
while num<0:
    num = int(input("You have entered a negative integer and unfortunately the factorial of negative integers is undefined. Please enter a positive integer: "))
start = time.time()
print("The factorial of", num, "is", fact_iter(num))
stop = time.time()
print("Elapsed time = ", stop-start)
