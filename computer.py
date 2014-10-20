from thing import *


class Computer (Thing):
    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)

    def use (self,actor):
        actor.location().report("BEEP BOOP BEEP BOP")
        actor.say('I use '+self.name()) 
        
        done_hws = []
        for item in actor.backpack():
            if item.is_homework():
                item.do()
                done_hws.append(item)
        if len(done_hws) == 0:
            actor.say('I do not have any homework to work on.')
        else:
            actor.say('I work on my homework.')
                
