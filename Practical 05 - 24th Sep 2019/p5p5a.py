# program to match a city name against a list and output which province the city is in

Entry = input('Enter a City Name: ')
if Entry == 'Dublin':
    print('You entered ', Entry, '. ', Entry, ' is in Leinster.', sep = '')   
elif Entry == 'Belfast':
    print('You entered ', Entry, '. ', Entry, ' is in Ulster.', sep = '')
elif Entry == 'Cork':
    print('You entered ', Entry, '. ', Entry, ' is in Munster.', sep = '')
elif Entry == 'Limerick':
    print('You entered ', Entry, '. ', Entry, ' is in Munster.', sep = '')
elif Entry == 'Derry':
    print('You entered ', Entry, '. ', Entry, ' is in Ulster.', sep = '')
elif Entry == 'Galway':
    print('You entered ', Entry, '. ', Entry, ' is in Connaught.', sep = '')
elif Entry == 'Lisburn':
    print('You entered ', Entry, '. ', Entry, ' is in Ulster.', sep = '')
elif Entry == 'Kilkenny':
    print('You entered ', Entry, '. ', Entry, ' is in Leinster.', sep = '')
elif Entry == 'Waterford':
    print('You entered ', Entry, '. ', Entry, ' is in Munster.', sep = '')
elif Entry == 'Sligo':
    print('You entered ', Entry, '. ', Entry, ' is in Connaught.', sep = '') 
else:
    print("Sorry, I didn't recognise the name")
    
