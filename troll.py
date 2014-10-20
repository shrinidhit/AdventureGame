import random
from npc import *

class Troll (NPC):
#Init
    def __init__ (self,name,loc,desc,restlessness,hunger):
        NPC.__init__(self,name,loc,desc,restlessness,10)
        self._hunger = hunger

#Functions
    def eat_people (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._hunger) == 0:
            people = self.people_around()
            if people:
                victim = random.choice(people)
                self.location().report(self.name() + ' takes a bite out of ' + victim.name())
                victim.suffer(random.randint(1,3))
            else:
                self.location().report(self.name() + "'s belly rumbles")