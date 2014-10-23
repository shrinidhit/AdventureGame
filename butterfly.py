#Imports
import random
from player import *
from mobile import *
from responses import ButterflyR
from room import Room

class Butterfly(MobileThing):
#Init
    def __init__(self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._state = 'caterpillar'
        self._desc = "An adorable caterpillar."
        Player.me.clock.add_to_register(self.transform, 1)
        Player.me.clock.add_to_register(self.move_somewhere, 1)
    
#Functions
    #Check state
    def state(self):
        return self._state
    
    #Proactive Behavior
    def transform(self,time):
        if self.state() == 'caterpillar':
            if time >= 3:
                self._state = 'coccoon'
                self._desc = "A weird coccoon thing."
                if self.location().is_person():
                    self.location().location().report(self.name() + " just bundled itself up into a coccoon...")
                else:
                    self.location().report(self.name() + " just bundled itself up into a coccoon...")
        if self.state() == 'coccoon':
            if time >= 8:
                self._state = 'butterfly'
                self._desc = "A beautiful butterfly! Sort of..."
                if self.location().is_person():
                    self.location().location().report(self.name() + " has emerged as a beautiful butterfly!")
                    self.drop(self.location())
                    self.location().report(self.name() + " has flown away!")
                else:
                    self.location().report(self.name() + " has emerged as a beautiful butterfly!")
                    
    #Proactive Behavior -- modified from method in NPC
    def move_somewhere (self,time):       
        if self.state() == 'butterfly':
            if time % 2 == 0:
                exits = self.location().exits()
                if exits:
                    dir = random.choice(exits.keys())
                    self.go(dir)

                
    #Override MobileThing's take() function 
    def take (self,actor):
        if self.state() == 'caterpillar' or self.state == 'coccoon':
            if self.location() == actor:
                actor.say('I already  have ' + self.name())
            else:
                if self.location().is_person():
                    self.location().say(choice(MobileThingR.taken) + self.name())
                self.move(actor)
                actor.say('I now have '+ self.name() + '. ' + choice(MobileThingR.take))
        else:
            actor.say("I try to catch "+self.name()+", but it's much too fast!")
            
    #Modified from method in Person for use in move_somewhere
    def go (self,direction):
        loc = self.location()
        if type(loc) is Room:
            exits = loc.exits()
            if direction in exits:
                t = exits[direction]
                loc.report(self.name()+' flies from '+ loc.name()+' to '+t.name())
                self.move(t)
                return True
        