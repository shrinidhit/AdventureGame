from room import *

class SleepRoom (Room):
	def __init__ (self,name,desc):
		Room.__init__(self,name,desc)

	def is_sleeproom(self):
		return True