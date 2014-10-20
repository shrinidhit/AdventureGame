from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._done = False
        
    def is_done (self):
        return self._done
        
    def do (self):
        if not self.is_done:
            self._done = True
            self._name = 'done-'+self.name

    def is_homework (self):
        return True
