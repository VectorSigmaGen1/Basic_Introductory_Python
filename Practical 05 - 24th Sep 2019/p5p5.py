# program to match a city name against a list and output which province the city is in

Entry = input('Enter a City Name: ')
if Entry == 'Dublin' or Entry == 'Kilkenny':
    print('You entered ', Entry, '. ', Entry, ' is in Leinster.', sep = '')   
elif Entry == 'Belfast' or Entry == 'Derry' or Entry == 'Lisburn':
    print('You entered ', Entry, '. ', Entry, ' is in Ulster.', sep = '')
elif Entry == 'Cork' or Entry == 'Limerick' or Entry == 'Waterford':
    print('You entered ', Entry, '. ', Entry, ' is in Munster.', sep = '')
elif Entry == 'Galway' or Entry == 'Sligo':
    print('You entered ', Entry, '. ', Entry, ' is in Connaught.', sep = '')
else:
    print("Sorry, I didn't recognise the name")
    
