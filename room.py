from wobject import *
from player import *


class Room (WObject): #,Container):

    rooms = []

    def __init__ (self,name,desc):
        WObject.__init__(self,name)
        self._exits = {}
        self._contents = []
        self._desc = desc
        Room.rooms.append(self)

    # Check Type Function:
    def is_room (self):
        return True

    # Extract Attribute Functions:
    def desc (self):
        return self._desc

    def exits (self):
        return self._exits

    def contents (self):
        return self._contents

    # Communication Functions
    def report (self,msg):
        if Player.me.location() is self:
            print msg
        elif Player.god_mode:
            print '(At', self.name(), msg+')'

    def broadcast (self,msg):
        print msg

    # Location/Person Shared Functions
    def have_thing (self,t):
        for c in self.contents():
            if c is t:
                return True
        return False

    def add_thing (self,t):
        self._contents.append(t)

    def del_thing (self,t):
        self._contents = [x for x in self._contents if x is not t]

