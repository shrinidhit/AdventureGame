from person import *
from clock import *
from responses import PlayerR

import sys

class Player (Person):

#Statics:
    # static field representing the player
    me = None
    # static field recording god_mode
    god_mode = False
    # static field representing the clock
    clock = Clock(0)

#Init:
    def __init__ (self,name,loc,desc):
        Person.__init__(self,name,loc,desc)
        Player.me = self
        self._credits = 0
        self._courses = []
        self._personality = PlayerR()
        self._health = 50
        self._max_health = 50
        self.clock.add_to_register(self.monitor_health, 20)
        self.clock.add_to_register(self.get_tired,1)

#Functions:
    def credits(self):
        return self._credits

    def courses(self):
        return self._courses

    def health(self):
        return self._health

    def thing_named (self,name):
        """Grab any kind of thing from player's location, given its name. The thing may be in the possession of
    the place, or in the possession of a person at the place."""
        for x in self.location().contents():
            if x.name() == name:
                return x
        for x in self.peek_around():
            if x.name() == name:
                return x
        for x in self.backpack():
            if x.name() == name:
                return x
        return None

    def look_around (self):
        def names (lst):
            return ', '.join([x.name() for x in lst])

        loc = self.location()
        exits = loc.exits()
        people = self.people_around()
        all_stuff = self.stuff_around()
        backpack = self.backpack()
        courses = self.courses()

        print '------------------------------------------------------------'
        print 'You are in', loc.name()
        print loc.desc()

        if all_stuff:
            print 'You see:', names(all_stuff)
        else: 
            print 'The room is empty'

        if people:
            print 'You see:', names(people)
        else:
            print 'You see no one around'
            
        if backpack:
            print 'You are holding:', names(backpack)
        else:
            print "You aren't holding anything."

        if courses:
            print 'Classes taken: ',names(courses)

        if exits:
            print 'Exits:', ', '.join([x for x in exits])
        else:
            print 'There are no exits'

    #Override Person's method
    def add_thing (self,t):
        if t.is_course():
            self._courses.append(t)
        else:
            self._backpack.append(t)

    def die (self):
        self.say('I am slain!')
        Person.die(self)
        print 'This game for you is now over...'
        sys.exit(0)

    def converse(self, target):
        if target.is_person():
            #Getting Options
            options = [random.choice(self._personality.helps), random.choice(self._personality.gossip),
            random.choice(self._personality.insult), random.choice(self._personality.compliment)]
            #Displaying Options
            print 'What would you like to say?: '
            for i in range(len(options)):
                print '%d. %s' %(i + 1, options[i])
            #Getting Response
            response = int(raw_input(''))
            while response < 1 or response > 4:
                print 'Enter a valid choice from 1-4: '
                response = int(raw_input(''))
            self.say(options[int(response) - 1])
            print response
            target.talk(response)
        else:
            self.location().report("You can only talk to people. Sorry, this world isn't magical.")

    def get_tired(self, time):
        self._health -= 1

    def monitor_health(self, time):        
        if self.health() <= 25:
            self.say("Gosh, I'm feeling pretty worn out. I should probably take a nap...")
        elif self.health() <= 10:
            self.say("I'm EXHAUSTED! I really should go to sleep...")
