from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc):
        Thing.__init__(self,name,loc)
        self._original_location = loc

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True

    def take (self,actor):
        if self.location() == actor:
            actor.say('I already  have ' + self.name())
        else:
            actor.say('I try to take '+ self.name())
            self.move(actor)
            actor.add_thing(self)
            actor.say('I now have ' + self.name())

    def drop (self,actor):
        if self.location() == actor:
            self.move(actor.location())
            actor.del_thing(self)
            actor.say('I have now dropped ' + self.name())
        else:
            print actor.name(),'is not carrying',self.name()

    def give(self, actor, target):
        if actor != self.location:
            print actor.name(),'is not carrying',self.name()
        else:
            self.drop(actor)
            self.take(target)
