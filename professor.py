from player import *
from npc import *
import random

class Professor (NPC):

      def __init__ (self,name,loc,desc,restlessness,professorial):
      	  NPC.__init__(self,name,loc,desc,restlessness,100)
          self._professorial = professorial

      _topics = ['Turing machines',
                 'the lambda calculus',
                 'Godel']

      def lecture (self,time):
        if not self.is_in_limbo():
          if random.randrange(self._professorial) == 0:
              if self.people_around():
                  self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
              else:
                  self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))

      def win(self):
        self.say('Congrats, you passed the class.')
        print "You win - See ya later"
        sys.exit(0)

      def accept (self,obj,source):
        if obj.location() == source:
          obj.take_silent(self)
          if obj.is_homework():
            if not obj.is_done():
              self.say('Excuse me....this homework isn''t completed. Try again.')
              obj.give(self, source)
            else:
              self.say('Aah, finally a homework that''s completed')
              time.sleep(1)
              self.say('Hmm...Could be better but I guess this passes')
              time.sleep(1)
              self.say('Good Job. Perhaps you''re not a fool after all')
              time.sleep(1)
              obj.give(self, source)
              self.win()
          else:
            self.say('Thanks ' + source.name())
        else:
            self.say('You have no homework to give me, fool!' + obj.name())
