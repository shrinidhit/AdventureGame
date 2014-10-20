#Imports:
import random
from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from homework import *
from computer import *

#Global Variables
REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}
SAME_ROUND = 1
NEXT_ROUND = 2 
VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down')
}

#Creating Connections between locations
def connect (fr,dir,to):
    """add an exit in 'fr' toward 'to' in direction 'dir'"""
    fr.exits()[dir] = to

def biconnect (fr,dir,to):
    """Add an exit in 'fr' toward 'to' in direction 'dir' and an exit the other way, 
    in 'to' toward 'fr' in the reverse direction"""
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)

#Creating World
def create_world ():
    #Creating Locations
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

    #Connecting Locations
    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    biconnect(mh1st, 'north',  oval)
    biconnect(oval, 'east',  cc1st)
    biconnect(cc1st, 'east',  wh1)
    biconnect(wh1, 'up', wh2)
    biconnect(wh2, 'up', wh3)
    biconnect(wh3, 'up', wh4)    
    biconnect(wh1, 'east', eh1)
    biconnect(eh1, 'up', eh2)
    biconnect(eh2, 'up', eh3)
    biconnect(eh3, 'up', eh4)
    biconnect(oval, 'north',  babson)
    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)

    #Player Creation: The player is the first 'thing' that has to be created
    Player('Blubbering-Fool', oval, "That's you!")

    #Creating Other Objects
    Radar('handy radar',mh353,'So very handy.') 
    Thing('blackboard', ac113,'You can write on it.')
    Thing('lovely-trees', oval,'So very pretty.')
    Thing('n64',wh3,'Such games.')
    Thing('rock-band',wh4,'Jammin.')

    MobileThing('cs-book', oval,'Learning that CS.')
    MobileThing('math-book', oval,'Learning them maths.')
    MobileThing('backpack',wh1,'To hold all the things.')
    MobileThing('lunch',cc1st,'Yummy in your tummy.')
    MobileThing('knowledge',ac113,'The ultimate goal.')

    Computer('hal-9000', ac113,'He knows too much...')
    Computer('johnny-5', eh1,'Kind of adorable.')
    Professor('Riccardo',mh353,"He's the best!",random.randint(1,5),2)
    
    #Random Choosings:
    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']
    
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms),"A homework. It's not done. :(")

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    for student in students:
        NPC(student,
            random.choice(Room.rooms),
            'A student.',
            random.randint(1,5),
            random.randint(1,5))

    trolls = ['Polyphemus',
              'Gollum']

    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            'A troll!',
            random.randint(1,3),
            random.randint(1,3))

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))

def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


#Main Game Loop: 
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'


    # Create the world
    create_world()
    
    Player.me.look_around()

    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.me.look_around()
        else:
            print 'What??'
            
#Testing Loop:     
def test():
    create_world()
    while True:
        Player.me.peek_around()


#Automatic Run:
if __name__ == '__main__':
    # test()
    main()
