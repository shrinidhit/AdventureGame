#Imports
import sys
from player import *

#Globals
SAME_ROUND = 1
NEXT_ROUND = 2  

#General Verb Class
class Verb (object):

    def act (self,input):
        if len(input)==0:
            return self.action0()
        if len(input)==1:
            wo1 = Player.me.thing_named(input[0])
            if wo1 is None:
                print 'Word',input[0],'not understood'
                return SAME_ROUND
            return self.action1(wo1)
        if len(input)>1:
            wo1 = Player.me.thing_named(input[0])
            if wo1 is None:
                print 'Word',input[0],'not understood'
                return SAME_ROUND
            wo2 = Player.me.thing_named(input[1])
            if wo2 is None:
                print 'Word',input[1],'not understood'
                return SAME_ROUND
            return self.action2(wo1,wo2)

    def action0 (self):
        print 'Input not understood'
        return SAME_ROUND

    def action1 (self,wo1):
        print 'Input not understood'
        return SAME_ROUND

    def action2 (self,wo1,wo2):
        print 'Input not understood'
        return SAME_ROUND

#Specific Verb Classes:
class Quit (Verb):
    def action0 (self):
        print 'Goodbye'
        sys.exit(0)

class Direction (Verb):
    def __init__ (self,dir):
        self._direction = dir
    def action0 (self):
        if Player.me.go(self._direction):
            return NEXT_ROUND
        else:
            return SAME_ROUND

class Look (Verb):
    def action0 (self):
        Player.me.look_around()
        return SAME_ROUND    
    def action1 (self,obj):
        print obj.desc()
        return SAME_ROUND

class Wait (Verb):
    def action0 (self):
        return NEXT_ROUND

class God (Verb):
    def action0 (self):
        if Player.god_mode:
            Player.god_mode = False
        else:
            Player.god_mode = True
        print '(God mode is now','on)' if Player.god_mode else 'off)'
        return SAME_ROUND

class Use (Verb):
    def action1 (self,obj):
        obj.use(Player.me)
        return SAME_ROUND

class Take (Verb):
    def action1 (self,obj):
        obj.take(Player.me)
        return SAME_ROUND

class Drop (Verb):
    def action1 (self,obj):
        if not Player.me.have_thing(obj):
            Player.me.say('I am not carrying '+obj.name())
        else:
            obj.drop(Player.me)
        return SAME_ROUND

class Give (Verb):
    def action2 (self,obj1,obj2):
        obj1.give(Player.me,obj2)
        return SAME_ROUND

class Talk (Verb):
    def action1 (self, obj1):
        Player.me.converse(obj1)
        return SAME_ROUND

class Sleep (Verb):
    def action0 (self):
        if Player.me.location().is_sleeproom():
            if Player.me.health() >= 18:
                Player.me.say("I got 10 hours of sleep... but that won't stop me from taking a nap!")
            elif Player.me.health >= 12:
                Player.me.say("I'm getting pretty tired... better take a nap.")
            elif Player.me.health >= 6:
                Player.me.say("Wow, I'm really sleepy. Time to go to bed!")
            else:
                Player.me.say("FINALLY! I HAVEN'T SLEPT IN DAYS!")
            print Player.me.name() + " sleeps for " + str(20-Player.me.health()) + " hours before finally waking up."

            Player.me.reset_health()
            return NEXT_ROUND
        else:
            Player.me.say("I can't sleep here, there's no bed!")

class Help (Verb):
    def action0 (self):
        print "quit ==> Ends the game."
        print "wait ==> Skips a turn."
        print "look ==> The player looks around, or looks at a specified item or person."
        print "take ==> The player takes the specified item, if it can be taken."
        print "drop ==> The player drops the specified item, if it is currently being held."
        print "give ==> The player gives the specified item to the specified person, if the item is currently being held."
        print "use ==> The player uses the specified item, if it is in the same room as the player or it is being held. "
        print "talk ==> The player talks to the specified person."
        print "sleep ==> The player goes to sleep, if they are in a sleeping area."
        print "north ==> The player moves north."
        print "south ==> The player moves south."
        print "east ==> The player moves east."
        print "west ==> The player moves west."
        print "up ==> The player moves up a level."
        print "down ==> The player moves down a level."


        
