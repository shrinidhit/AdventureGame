from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)
        self._original_location = loc

    #Check Type Function:
    def is_mobile_thing (self):
        return True

    #Return Attributes:
    def creation_site (self):
        return self._original_location

    #Action Functions:
    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    #Take/Drop/Give/Exchange Functions:
    def take (self,actor):
        if self.location() == actor:
            actor.say('I already  have ' + self.name())
        else:
            if self.location().is_person():
                self.location().say('Sniffle. You took ' + self.name() + ' away from me')
            self.move(actor)
            actor.say('I now have the '+ self.name() + '. hehehe :)')

    def take_silent (self, actor):
        if self.location() == actor:
            actor.say('I already  have ' + self.name())
        else:
            self.move(actor)

    def drop (self,actor):
        if self.location() == actor:
            self.move(actor.location())
            actor.del_thing(self)
            actor.say('I have now dropped ' + self.name())
        else:
            print actor.name(),'is not carrying',self.name()

    def give(self, actor, target):
        if actor != self.location():
            print actor.name(),'is not carrying',self.name()
        else:
            actor.say('I give ' + self.name() + ' to ' + target.name())
            target.accept(self, actor)


