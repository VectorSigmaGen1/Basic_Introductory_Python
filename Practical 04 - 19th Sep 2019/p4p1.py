# program to convert a specified amount from Euro to Dollars

Exchange_euro_dollar = 1.10676
Euro_amount = float(input('Enter amount in Euro: '))
if Euro_amount <= 0:
    print('Please enter a positive, nonzero value - restart program to proceed')
else:
    print('Amount in Dollars:', Euro_amount*Exchange_euro_dollar)
