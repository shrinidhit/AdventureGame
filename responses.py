import random

#Responses Class. Has three major personalites, sweet, grumpy, and sassy. Each of those have a helps, gossip, insult, and compliment
#list of responses when initialized

class Responses(object):
	class Sweet(object):
		names = ['nemo', 'dori', 'sneezy']
		messages = ['Your friend', 'Pretty darn cute', 'SUPER hyper...ALL the time', 'Made of rainbows and unicorns...literally']
		def __init__(self):
			self.helps = ['Radar is your best friend', 'Knowledge is Power', 'Find a robotic friend']
			self.gossip = ['IDK too much about anything', 'Sowwy, I don''t gossip', 'DUDE, that''s not cool']
			self.insult = ['...', 'well then.', 'wow...guess I won''t be helping you']
			self.compliment = ['HI FRIEND!', 'I like you :)', 'We can get married?']

	class Sassy(object):
		names = ['dancer','mileyCyrus', 'beyonce']
		messages = ['Oh so cute...but DANGEROUS', 'Don''t get on their bad side...', 'One SASSY diva', 'will WRECK you']
		def __init__(self):
			self.helps = ['Pshhh...maybe if you pay me', 'Nice try bro']
			self.gossip = ['Yeaaa, I''m not too fond of them', 'I really like them']
			self.insult = ['DAMN. Someone''s got attitude.', 'EXCUSE me, you''re no match for me', 'Pshh...loser']
			self.compliment = ['Sucking up to me, huh?', 'Yea, you can''t bribe me with fancy talk. Seeya']

	class Grumpy(object):
		names = ['grumpy', 'dopey', 'rudolph', 'cookiemonster', 'Thor']
		messages = ['A meathead on a mission', 'Your grouchy gramps', 'Woke up on the wrong side of the bed today...']
		def __init__(self):
			self.helps = ['Hmph..you just woke me up and you expect help?', 'Nope.']
			self.gossip = ['Huff...youngsters these days', 'I don''t care.']
			self.insult = ['Whatever.', 'Take your ridiculousness elsewhere', 'WOW. you woke me up from my nap for that?']
			self.compliment = ['...I don''t know you', 'Try that on someone stupider']

	personalities = [Sweet, Sassy, Grumpy]

#Player Specific Sayings
class PlayerR(object):
	def __init__(self):
		person = random.choice(['professor', 'computer', 'troll', 'butterfly', 'badninja', 'trollhunter'])
		self.helps = ['Hey, couldja give a pal some advice?', 'Pweeease help me?', 'Help! I''m so confuzzled']
		self.gossip = ['Dude, isn''t the %s so nice?' %(person), 'WHAT is up with the %s? SO messed up...' %(person)]
		self.insult = ['You wanna go, bro?', 'Ew...you stink. Can you leave?', 'JUST saying...you gotta upgrade your style']
		self.compliment = ['I really like you :)', 'Wanna be friends?', 'Hey, you - up to be my partner in crime?']

#Object Specifics:
class MobileThingR(Responses.Sweet):
	taken = ['Aww I liked ', 'Sniffle. You took my ', 'Whatevs, I guess I can deal without my ', 'Good riddance -I don''t need my ', 'You wanna go bro? I''ll fight for my ']
	take = ['hehe :)', 'Great, another thing to carry', 'Heavy...this better be useful', 'YAY', '...fantastic?']
	drop = ['aww :(', 'Adios Amigo', 'So Long, Farewell', 'Adieu', 'Good bye, my love']
	give = ['Make good use of it. Or you WILL be sorry', 'Good Riddance', 'Love You!', 'Let''s be friends']

class BadNinjaR(Responses.Sassy):
	names = Responses.Sassy.names
	names.extend(['pinkpanda', 'swiper', 'wasabi'])
	messages = Responses.Sassy.messages
	messages.append(['Intense cooking gave this kid mad ninja skills...beware'])

	def __init__(self):
		Responses.Sassy.__init__(self)
		self.hwTaken = ['snatches the homework. Gotta have quicker hands, bro',
			'brushes by and some homework''s gone....suspicious',
			'ate the homework. Sorry, tell your teacher your dog ate it?']

		self.hwAlmostTaken = ['licks lips at the homework....delish',
			'didn''t finish their homework. Be wary...',
			'shyly glances at the homework']

		self.hwDestroy = ['Wow it''s so pwetty! Imma make it sparkle....with fire!',
		'Damn, this person''s smart. BURN! I can''t have competion.',
		'Gonna casually look at this. Oopsie, I accidentally lit it on fire',]

class ButterflyR(Responses.Sweet):
	names = Responses.Sweet.names
	names.extend(['Fwee', 'Fleur'])
	messages = Responses.Sweet.messages
	messages.append('Fweeeeeee. I like to be Freeeeeee')

class TrollHunterR(Responses.Grumpy):
    battle_phrases = ["AHA! I've got you now, troll!", "Taste my fury, you hellish beast!", "Die, fiend, DIE!"]
    search_phrases = ["I'm coming for you, troll!", "I can smell your fear from a mile away!", "Run all you want, but you cannot hide from me."]

class ComputerR(Responses.Sweet):
	names = Responses.Sweet.names
	names.extend(['R2D2', 'R2D2'])
	messages = ['So very handy. Try it!', 'Knows too much...suspiciously not human', 'Clink. Clink. Clack', 'Kind of adorable. A little monotoned and clinky but hey.']
