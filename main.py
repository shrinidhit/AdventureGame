
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


REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():

    mh353 = Room('Riccardo Office')
    mh3rd = Room('Milas Hall Third Floor')
    mh2nd = Room('Milas Hall Second Floor')
    mh1st = Room('Milas Hall First Floor')
    oval = Room('Oval')
    ac1st = Room('Academic Center First Floor')
    ac113 = Room('Academic Center 113')
    cc1st = Room('Campus Center First Floor')
    wh1 = Room('West Hall First Floor')
    wh2 = Room('West Hall Second Floor')
    wh3 = Room('West Hall Third Floor')
    wh4 = Room('West Hall Fourth Floor')
    eh1 = Room('East Hall First Floor')
    eh2 = Room('East Hall Second Floor')
    eh3 = Room('East Hall Third Floor')
    eh4 = Room('East Hall Fourth Floor')
    babson = Room('Babson College')

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
    biconnect(eh3, 'up', useeh4)
    biconnect(oval, 'north',  babson)
    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)

    # The player is the first 'thing' that has to be created

    Player('Blubbering-Fool', oval)

    Radar('handy radar',mh353) 
    Thing('blackboard', ac113)
    Thing('lovely-trees', oval)
    Thing('n64',wh3)
    Thing('rock-band',wh4)
    MobileThing('cs-book', oval)
    MobileThing('math-book', oval)
    MobileThing('backpack',wh1)
    MobileThing('lunch',cc1st)
    MobileThing('knowledge',ac113)

    Computer('hal-9000', ac113)
    Computer('johnny-5', eh1)

    Professor('Riccardo',mh353,random.randint(1,5),2)
    
    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']
    
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms))

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    for student in students:
        NPC(student,
            random.choice(Room.rooms),
            random.randint(1,5),
            random.randint(1,5))

    trolls = ['Polyphemus',
              'Gollum']

    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            random.randint(1,3),
            random.randint(1,3))


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
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
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
            

if __name__ == '__main__':
    main()
