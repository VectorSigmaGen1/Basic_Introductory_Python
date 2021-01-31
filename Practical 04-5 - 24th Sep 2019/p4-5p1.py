# program to convert a specified amount from Euro to Dollars

Exchange_euro_dollar = 1.10033
Euro_amount = float(input('Enter amount in Euro: '))
if Euro_amount <= 0:
    print('Amount must be >=0. Please try again')
    
else:
    print('Amount in Dollars:', Euro_amount*Exchange_euro_dollar)
