from mobile import *


class Person (MobileThing):    # Container...

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._max_health = 3
        self._health = self._max_health
        self._backpack = []

    #Check Type Function
    def is_person (self):
        return True

    # Extract/Change attribute Functions:
    def backpack (self):
        return self._backpack

    def health (self):
        return self._health

    def reset_health (self):
        self._health = self._maxHealth

    # Basic Communication Functions
    def say (self,msg):
        loc = self.location()
        loc.report(self.name()+' says -- '+msg)

    def have_fit (self):
        self.say('Yaaaaah! I am upset!')

    # Location/Room Shared Functions:
    def have_thing(self, thing):
        if thing in self.backpack():
            return True
        return False

    def add_thing (self,t):
        self._backpack.append(t)

    def del_thing (self,t):
        self._backpack = [x for x in self._backpack if x is not t]

    #Check Surroundings Functions:
    def people_around (self):
        return [x for x in self.location().contents()
                    if x.is_person() and x is not self]

    def stuff_around (self):
        return [x for x in self.location().contents() if not x.is_person()]

    def peek_around (self):
        return [item for x in self.people_around() for item in x.backpack()]

    # Take/Give/Exchange Objects
    def take (self,actor):
        actor.say('I am not strong enough to just take '+self.name())

    def drop (self,actor):
        print actor.name(),'is not carrying',self.name()

    def give (self,actor,target):
        print actor.name(),'is not carrying', self.name()

    def accept (self,obj,source):
        if obj.location() == source:
            obj.take_silent(self)
            self.say('Thanks, ' + source.name())
        else:
            self.say('Thanks, but you don''t have' + obj.name())

    # Movement Functions:
    def enter_room (self):
        people = self.people_around()
        if people:
            self.say('Hi ' + ', '.join([x.name() for x in people]))

    def leave_room (self):
        pass   # do nothing to reduce verbiage

    def go (self,direction):
        loc = self.location()
        exits = loc.exits()
        if direction in exits:
            t = exits[direction]
            self.leave_room()
            loc.report(self.name()+' moves from '+ loc.name()+' to '+t.name())
            self.move(t)
            self.enter_room()
            return True
        else:
            print 'No exit in direction', direction
            return False

    # Action Functions:
    def lose (self,t,loseto):
        self.say('I lose ' + t.name())
        self.have_fit()
        t.move(loseto)

    def suffer (self,hits):
        self.say('Ouch! '+str(hits)+' hits is more than I want!')
        self._health -= hits
        if (self.health() < 0):
            self.die()
        else:
            self.say('My health is now '+str(self.health()))

    def die (self):
        self.location().broadcast('An earth-shattering, soul-piercing scream is heard...')
        self.destroy()
