#Imports
import random
from player import *
from npc import *

#Class
class BadNinja(NPC):
	#Statics
	hwTaken = ['snatches the homework. Gotta have quicker hands, bro',
		'brushes by and some homework''s gone....suspicious',
		'ate the homework. Sorry, tell your teacher your dog ate it?']

	hwAlmostTaken = ['licks lips at the homework....delish',
		'didn''t finish their homework. Be wary...',
		'shyly glances at the homework']

	hwDestroy = ['Wow it''s so pwetty! Imma make it sparkle....with fire!',
	'Damn, this person''s smart. BURN! I can''t have competion.',
	'Gonna casually look at this. Oopsie, I accidentally lit it on fire',]

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
				self.location().report(self.name() + ' ' + random.choice(BadNinja.hwTaken))
				#Takes HW:
				homework = random.choice(Homeworks)
				homework.take(self)
				#Comment 2
				self.say(random.choice(BadNinja.hwDestroy))
				homework.destroy()

			else:
				self.location().report(self.name() + ' ' + random.choice(BadNinja.hwAlmostTaken))
