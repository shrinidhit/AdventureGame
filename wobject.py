#Imports
import time

#Class
class WObject (object):
    #Init
    def __init__ (self,n):
        self._name = n.replace(' ', '-')
    #Return Attribute
    def name (self):
        return self._name
    #Check Types
    def is_thing (self):
        return False
  
    def is_mobile_thing (self):
        return False

    def is_person (self):
        return False

    def is_room (self):
        return False

    def is_homework (self):
        return False
