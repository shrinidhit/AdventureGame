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
from badninja import *
from butterfly import *
from trollhunter import *
from responses import *
from initials import *

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
    #Connecting Locations
    for con in Connections:
        biconnect(con[0], con[1], con[2])

    #Player Creation: The player is the first 'thing' that has to be created
    Player('Blubbering-Fool', oval, "That's you!")

    #Needed Objects:
    Radar('handy radar',mh353,'So very handy. Try it!') 
    Thing('blackboard', ac113,'You can write on it.')
    Thing('lovely-trees', oval,'So very pretty.')
    Thing('n64',wh3,'Such games.')
    Thing('rock-band',wh4,'Jammin.')

    MobileThing('cs-book', oval,'Learning that CS ;).')
    MobileThing('math-book', oval,'Learning them maths.')
    MobileThing('backpack',wh1,'To hold ALL the things.')
    MobileThing('lunch',cc1st,'Yummy in your tummy.')
    MobileThing('knowledge',ac113,'The ultimate goal. Of life. nudge, nudge, hint')

    Computer('hal-9000', ac113,'Knows too much...suspiciously not human')
    Computer('johnny-5', eh1,'Kind of adorable. A little monotoned and clinky but hey.')
    Professor('Riccardo',mh353,"He's the best!",random.randint(1,5), random.randint(1,5))
    
    #Random Choosings:
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms),"A homework. It's not done. :(")

    for student in students:
        NPC(student,
            random.choice(Room.rooms),
            'A student.',
            random.randint(1,5),
            random.randint(1,5))

    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            'A troll!',
            random.randint(1,3),
            random.randint(1,3))

    for i in range(random.randint(2,4)):
        BadNinja(random.choice(BadNinjaR.names), random.choice(Room.rooms), random.choice(BadNinjaR.messages) ,random.randint(1,5),random.randint(1,5))

    for i in range(random.randint(2,4)):
        Butterfly(random.choice(ButterflyR.names), random.choice(Room.rooms), random.choice(ButterflyR.messages))

    for i in range(random.randint(2,4)):
        TrollHunter(random.choice(TrollHunterR.names),mh1st, random.choice(TrollHunterR.messages) ,random.randint(1,3),random.randint(1,8))


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
    Player.clock.add_to_register(print_tick_action, 3)

    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.clock.tick()
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
