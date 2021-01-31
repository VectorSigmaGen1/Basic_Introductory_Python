# Program to calculate 2 rates of tax on 2 bands of 60% & 40%
Gross = float(input('Enter initial Tax Free amount: '))
if Gross <= 0:
    print('Amount of income must be >= 0. Please try again')
else:
    Low_Rate = Gross*0.6
    High_Rate = Gross-Low_Rate
    print('Initial Ex Tax Amount:', Gross)
    print('Tax at 23% Due:', Low_Rate*0.23)
    print('Tax at 41% Due:', High_Rate*0.41)
    print('Total Including Tax:', Gross-Low_Rate*0.23-High_Rate*0.41)
