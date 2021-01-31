# program to calculate the number of combinations of toppings on a pizza
# user inputs total possible toppings
# user inputs number of toppings allowed per pizza

"""
Pseudocode

request input for an integer and assign to variable poss
print "Please enter the total number of possible toppings: "
request input for an integer and assign to variable allow
print "Please enter the allowed number of toppings on a standard pizza: "
IF poss >= 0 and allow >= 0 and allow <= poss:
    poss_fac = 1
    FOR i in range (1, (poss+1), 1):
        poss_fac = poss_fac + 1
    allow_fac = 1
    FOR i in range (1, (poss+1), 1):
        poss_fac = poss_fac + 1
    comb_fac = 1
    FOR i in range (1, (comb+1), 1):
        comb_fac = comb_fac + 1
    print 'The total number of possible pizza topping combinations is: ', (poss_fac / (allow_fac * comb_fac))
ELSE
    print 'Topping numbers cannot be less than zero'
    print 'Program Terminated'


"""

poss = int(input('Please enter the total number of possible toppings: '))
allow = int(input('Please enter the allowed number of toppings on a standard pizza: '))
if poss >= 0 and allow >= 0 and allow <= poss:
    poss_fac = 1
    for i in range(1, poss+1):
        poss_fac *= i
    allow_fac = 1
    for i in range(1, allow+1):
        allow_fac *= i
    comb_fac = 1
    for i in range (1, (poss-allow)+1):
        comb_fac *= i
    print('The total number of possible pizza topping combinations is: ', (poss_fac//(allow_fac*comb_fac)))
else:
    print('Topping numbers cannot be less than zero')
    print('Program Terminated')

    
        
