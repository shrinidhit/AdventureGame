from mobile import *
from player import*

class Course(MobileThing):

    def __init__ (self,name,loc,credits,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._credits = credits

    def is_course(self):
        return True

    def credits(self):
    	return self._credits

    #Override MobileThing's functions
    def take (self,actor):    	
    	if actor == Player.me:
    		if self.location() == actor:
    			actor.say('I already have ' + self.name())
        	else:
	            self.move(actor)
	            actor.say('I just took '+self.name()+'! Gee, what a great class. I feel full of knowledge.')
	            actor._credits += self.credits()
	            if actor.credits() >= 16:
	            	actor.say("Wow, looks like I just finished a semester at Olin! I'm so smart now!")
	            	print "You win - See ya later"
	            	sys.exit(0)

    def drop (self,actor):
    	pass

    def give(self, actor, target):
    	pass