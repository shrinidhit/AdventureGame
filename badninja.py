#Imports
import random
from player import *
from npc import *
from responses import BadNinjaR

#Class
class BadNinja(NPC):
	#Init
	def __init__(self,name,loc,desc,restlessness, hwHunger):
		NPC.__init__(self,name,loc,desc,restlessness,20)
		self._hwHunger = hwHunger

	#Functions
	def steal_hw(self, time):
		if not self.is_in_limbo():
			if random.randrange(self._hwHunger) == 0:
				#getting Homework in Room
				Homeworks = [item for item in self.stuff_around() if item.is_homework()]
				# Homeworks.extend[item for item in self.peek_around() if item.is_homework()]
				#Comment 1
				self.location().report(self.name() + ' ' + random.choice(BadNinjaR.hwTaken))
				#Takes HW:
				homework = random.choice(Homeworks)
				homework.take(self)
				#Comment 2
				self.say(random.choice(BadNinjaR.hwDestroy))
				homework.destroy()

			else:
				self.location().report(self.name() + ' ' + random.choice(BadNinjaR.hwAlmostTaken))
