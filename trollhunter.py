#Imports
import random
from player import *
from npc import *

class TrollHunter(NPC):
#Init
    def __init__(self,name,loc,desc,restlessness,miserly):
        NPC.__init__(self,name,loc,desc,restlessness,miserly)
        Player.me.clock.add_to_register(self.attack_troll, 1)


#Functions
    #Proactive Behavior
    def attack_troll(self,time):

        battle_phrases = ["AHA! I've got you now, troll!", "Taste my fury, you hellish beast!", "Die, fiend, DIE!"]
        search_phrases = ["I'm coming for you, troll!", "I can smell your fear from a mile away!", "Run all you want, but you cannot hide from me--"+self.name()+"--SLAYER OF EVIL!"]
              
        attacked = False
        if not self.is_in_limbo():
            for person in self.people_around():
                if person.is_troll():                
                    self.say(random.choice(battle_phrases))
                    person.suffer(2)
                    attacked = True
                    break
                break
            if attacked == False:
                self.say(random.choice(search_phrases))
                self.move_and_take_stuff(time)