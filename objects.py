from room import *

homeworks = ['hw-1', 
             'hw-2',
             'hw-3',
             'hw-4',
             'hw-5',
             'hw-6']

students = ['Frankie Freshman',
            'Joe Junior',
            'Sophie Sophomore',
            'Cedric Senior']

trolls = ['Polyphemus',
          'Gollum']

Connections = [[mh353, 'east',  mh3rd],
	[mh3rd, 'down',  mh2nd],
	[mh2nd, 'down',  mh1st],
	[mh1st, 'north',  oval],
	[oval, 'east',  cc1st],
	[cc1st, 'east',  wh1],
	[wh1, 'up', wh2],
	[wh2, 'up', wh3],
	[wh3, 'up', wh4],
	[wh1, 'east', eh1],
	[eh1, 'up', eh2],
	[eh2, 'up', eh3],
	[eh3, 'up', eh4],
	[oval, 'north',  babson],
	[oval, 'west',  ac1st],
	[ac1st, 'north',  ac113]]
	
#Rooms
def create_rooms():
	mh353 = Room('Riccardo Office','Where Riccardo works.')
	mh3rd = Room('Milas Hall Third Floor','3rd Floor of Milas Hall')
	mh2nd = Room('Milas Hall Second Floor','2nd Floor of Milas Hall')
	mh1st = Room('Milas Hall First Floor','1st Floor of Milas Hall')
	oval = Room('Oval','Quite round in appearance.')
	ac1st = Room('Academic Center First Floor','Ah, the sweet smell of knowledge.')
	ac113 = Room('Academic Center 113','Home of GPro')
	cc1st = Room('Campus Center First Floor','Dat food though.')
	wh1 = Room('West Hall First Floor','1st Floor of West Hall')
	wh2 = Room('West Hall Second Floor','2nd Floor of West Hall')
	wh3 = Room('West Hall Third Floor','3rd Floor of West Hall')
	wh4 = Room('West Hall Fourth Floor','4th Floor of West Hall')
	eh1 = Room('East Hall First Floor','1st Floor of East Hall')
	eh2 = Room('East Hall Second Floor','2nd Floor of East Hall')
	eh3 = Room('East Hall Third Floor','3rd Floor of East Hall')
	eh4 = Room('East Hall Fourth Floor','4th Floor of East Hall')
	babson = Room('Babson College','BABBIES')



