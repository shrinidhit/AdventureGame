from thing import *


class Computer (Thing):
    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)

    def use (self,actor):
        for item in actor.backpack():
            if item.is_homework:
                item.do()
