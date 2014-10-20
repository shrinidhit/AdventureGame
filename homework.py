from mobile import *


class Homework (MobileThing):
    #Init
    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self._done = False

    #Check Type Function:
    def is_homework (self):
        return True

    #Other Functions:
    def is_done (self):
        return self._done
        
    def do (self):
        if not self.is_done():
            self._done = True
            self._name = 'done-'+self._name
            self._desc = "A homework. It's done!"
