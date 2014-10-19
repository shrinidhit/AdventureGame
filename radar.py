from mobile import *
from room import *


class Radar (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)

    def get_locations(self, actor):
    	Items = []
    	[Items.extend(room.contents()) for room in Room.rooms]
    	return Items
    def use (self,actor):
        actor.say('I fiddle with the buttons on ' + self.name());
        Items = self.get_locations(actor)
        for item in Items:
        	if item != None:
	        	name = item.name()
	        	location = item.location().name()
        		actor.say("I detect " + name + " in " + location)