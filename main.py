#Shrinidhi Thirumalai and Haley Pelletier
#Game Programming 2014
#Adventure Based Text Game

#Title: OlinLand
#Description: You are an Oliner inside Olin's very quirky campus. Find a way to learn as much as you can,
#and survive a semester. And of course, socialize with others to explore the quirky and unique culture. 

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
from course import *
from sleeproom import *
from responses import *
from initials import *


#Global Variables
    #defines directions
REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}
    #defines rounds
SAME_ROUND = 1
NEXT_ROUND = 2 
    #Maps verbs to corresponding functions
VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'talk' : Talk(),
    'sleep' : Sleep(),
    'help' : Help(),
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
def static_world():
    """Non-Random Necessities in the world that must be created every time"""
    #Craetes Rooms
    mh353 = Room("Riccardo's Office",'Where Riccardo works.')
    mh3rd = Room('Milas Hall Third Floor','3rd Floor of Milas Hall')
    mh2nd = Room('Milas Hall Second Floor','2nd Floor of Milas Hall')
    mh1st = Room('Milas Hall First Floor','1st Floor of Milas Hall')
    oval = Room('Oval','Quite round in appearance.')
    ac1st = Room('Academic Center First Floor','Ah, the sweet smell of knowledge.')
    ac2nd = Room('Academic Center Second Floor','Ah, the sweet smell of knowledge.')
    ac3rd = Room('Academic Center Third Floor','Ah, the sweet smell of knowledge.')
    ac4th = Room('Academic Center Fourth Floor','Ah, the sweet smell of knowledge.')
    ac113 = Room('Academic Center Room 113','Home of GPro')
    ac213 = Room('Academic Center Room 213','Design Studio')
    ac326 = Room('Academic Center Room 326','Home of AHS')
    ac429 = Room('Academic Center Room 429','Home of ISIM')
    cc1st = Room('Campus Center First Floor','Dat food though.')    
    wh1 = Room('West Hall First Floor','1st Floor of West Hall')
    wh2 = Room('West Hall Second Floor','2nd Floor of West Hall')
    wh3 = Room('West Hall Third Floor','3rd Floor of West Hall')
    wh4 = Room('West Hall Fourth Floor','4th Floor of West Hall')
    wh113 = SleepRoom('West Hall Room 113','What a comfy room. Seems great for napping.')
    wh214 = SleepRoom('West Hall Room 214','What a comfy room. Seems great for napping.')
    wh325 = SleepRoom('West Hall Room 325','What a comfy room. Seems great for napping.')
    wh426 = SleepRoom('West Hall Room 426','What a comfy room. Seems great for napping.')
    eh1 = Room('East Hall First Floor','1st Floor of East Hall')
    eh2 = Room('East Hall Second Floor','2nd Floor of East Hall')
    eh3 = Room('East Hall Third Floor','3rd Floor of East Hall')
    eh4 = Room('East Hall Fourth Floor','4th Floor of East Hall')
    eh116 = SleepRoom('East Hall Room 116','What a comfy room. Seems great for napping.')
    eh215 = SleepRoom('East Hall Room 215','What a comfy room. Seems great for napping.')
    eh324 = SleepRoom('East Hall Room 324','What a comfy room. Seems great for napping.')
    eh423 = SleepRoom('East Hall Room 423','What a comfy room. Seems great for napping.')
    babson = Room('Babson College','You see Babbies, literally everwhere. A small, faint voice whispers in the distance... ~busssinesssss~')

    #List of Room Connections
    Connections = [[mh353, 'east',  mh3rd],
    [mh3rd, 'down',  mh2nd],
    [mh2nd, 'down',  mh1st],
    [mh1st, 'north',  oval],
    [oval, 'east',  cc1st],
    [cc1st, 'east',  wh1],
    [wh1, 'north', wh113],
    [wh1, 'up', wh2],
    [wh2, 'north', wh214],
    [wh2, 'up', wh3],
    [wh3, 'north', wh325],
    [wh3, 'up', wh4],
    [wh4, 'north', wh426],
    [wh1, 'east', eh1],
    [eh1, 'north', eh116],
    [eh1, 'up', eh2],
    [eh2, 'north', eh215],
    [eh2, 'up', eh3],
    [eh3, 'north', eh324],
    [eh3, 'up', eh4],
    [eh4, 'north', eh423],
    [oval, 'north',  babson],
    [oval, 'west',  ac1st],
    [ac1st, 'north',  ac113],
    [ac1st, 'up', ac2nd],
    [ac2nd, 'north', ac213],
    [ac2nd, 'up', ac3rd],
    [ac3rd, 'north', ac326],
    [ac3rd, 'up', ac4th],
    [ac4th, 'north', ac429]]

    #Connects all rooms
    for con in Connections:
        biconnect(con[0], con[1], con[2])

    #Player Creation: Must be first thing that's created
    Player('Blubbering-Fool', oval, "That's you!")

    #Needed Objects:
        #Radar
    Radar('handy radar',mh353,'So very handy. Try it!')
        #Random Things
    Thing('blackboard', ac113,'You can write on it.')
    Thing('lovely-trees', oval,'So very pretty.')
    Thing('n64',wh3,'Such games.')
    Thing('rock-band',wh4,'Jammin.')
    Thing('knowledge',ac113,'The ultimate goal. Of life. nudge, nudge, hint')
        #Course
    Course('DesNat',ac213,4,"The smell of molten Delrin fills the air. Taking in a deep breath, you can feel the carcinogens gnawing away at your life's very essence. This, truly, is what it means to be an engineer.")
    Course('ISIM',ac429,4,"Resistors are strewn across every visible surface. If your personal hygiene were as bad as your circuit hygiene, you'd probably have contracted the Bubonic Plague by now.")
    Course('AHS',ac326,4,"What is this shit? This isn't engineering...")
    Course('ModSim',ac213,4,"There are so many sharks, rays, and scallops that you can't see anything else. The world has been consumed by marine life.")
        #Mobile Things
    MobileThing('study-abroad-pamphlet',cc1st,"Hmm... maybe I'll go to Europe next semester...")
    MobileThing('cs-book', oval,'Learning that CS ;).')
    MobileThing('math-book', oval,'Learning them maths.')
    MobileThing('ruler',wh1,'To measure ALL the things.')
    MobileThing('lunch',cc1st,'Yummy in your tummy.')
        #Computers
    Computer('hal-9000', ac113,'Knows too much...suspiciously not human')
    Computer('johnny-5', eh1,'Kind of adorable. A little monotoned and clinky but hey.')
        #Professor
    Professor('Riccardo',mh353,"He's the best!",random.randint(1,5), random.randint(1,5))

#Creating World
def create_world ():
    """Creates Initial World with exits and connections"""
    static_world() #Non-random Necessities

    #Random Choosings:
        #Homeworks
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms),"A homework. It's not done.")
        #Students
    for student in students:
        NPC(student,
            random.choice(Room.rooms),
            'A student.',
            random.randint(1,5),
            random.randint(1,5))
        #Trolls
    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            'A troll!',
            random.randint(1,3),
            random.randint(1,3))
        #Bad Ninjas
    for i in range(random.randint(2,4)):
        BadNinja(random.choice(BadNinjaR.names), random.choice(Room.rooms), random.choice(BadNinjaR.messages) ,random.randint(1,5),random.randint(1,5))
        #Butterflies
    for i in range(random.randint(2,4)):
        Butterfly(random.choice(ButterflyR.names), random.choice(Room.rooms), random.choice(ButterflyR.messages))
        #Troll Hunters
    for i in range(random.randint(2,4)):
        TrollHunter(random.choice(TrollHunterR.names), random.choice(Room.rooms), random.choice(TrollHunterR.messages) ,random.randint(1,3),random.randint(1,8))

def print_tick_action (t):
    """Prints Time to Player"""
    #Special Messages:
    if 8 >= (t % 12) > 6:
        message = 'It''s getting dark'
    elif 11 >= (t % 12) > 8:
        message = 'Sleepy Time! Go to sleep.'
    else:
        message = ''
    #Report Time + Message:
    Player.me.location().report('The clock ticks '+str(t) + '. ' + message)

def read_player_input ():
    """Get's player's input and perfoms the action"""
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()

def start_sequence():
    """Starting Display Lines with Instructions"""
    print '------------------------------------------------------------'
    print 'Olinland, version 1.4 (Fall 2014)'
    print '------------------------------------------------------------\n'
    print 'You are a new first year inside Olin''s VERY quirky campus.' 
    print 'Find a way to learn as much as you can,and survive a semester ;)' 
    print 'And of course, socialize with others to explore the quirky and unique culture.\n'
    print 'type "help" to see a list of possible commands'

#Main Game Loop: 
def main ():
    """Main Game Loop"""
    #Display's start sequence/instructions
    start_sequence()
    # Create the world
    create_world()
    #Displays Items Around
    Player.me.look_around()
    #Performs Items in Register
    Player.clock.add_to_register(print_tick_action, 3)

    #Loops to get player input
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
            
#Automatic Run:
if __name__ == '__main__':
    main()