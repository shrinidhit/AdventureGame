class Responses(object):
	class Sweet(object):
		names = ['nemo', 'dori', 'sneezy']
		messages = ['Your friend', 'Pretty darn cute', 'SUPER hyper...ALL the time', 'Made of rainbows and unicorns...literally']
	class Sassy(object):
		names = ['dancer','mileyCyrus', 'beyonce']
		messages = ['Oh so cute...but DANGEROUS', 'Don''t get on their bad side...', 'One SASSY diva', 'will WRECK you']
	class Grumpy(object):
		names = ['grumpy', 'dopey', 'rudolph', 'cookiemonster', 'Thor']
		messages = ['A meathead on a mission', 'Your grouchy gramps', 'Woke up on the wrong side of the bed today...']
	personalities = [Sweet, Sassy, Grumpy]

class MobileThingR(Responses.Sweet):
	taken = ['Aww I liked ', 'Sniffle. You took my ', 'Whatevs, I guess I can deal without my ', 'Good riddance -I don''t need my ', 'You wanna go bro? I''ll fight for my ']
	take = ['hehe :)', 'Great, another thing to carry', 'Heavy...this better be useful', 'YAY', '...fantastic?']
	drop = ['aww :(', 'Adios Amigo', 'So Long, Farewell', 'Adieu', 'Good bye, my love']
	give = ['Make good use of it. Or you WILL be sorry', 'Good Riddance', 'Love You!', 'Let''s be friends']

class BadNinjaR(Responses.Sassy):
	hwTaken = ['snatches the homework. Gotta have quicker hands, bro',
		'brushes by and some homework''s gone....suspicious',
		'ate the homework. Sorry, tell your teacher your dog ate it?']

	hwAlmostTaken = ['licks lips at the homework....delish',
		'didn''t finish their homework. Be wary...',
		'shyly glances at the homework']

	hwDestroy = ['Wow it''s so pwetty! Imma make it sparkle....with fire!',
	'Damn, this person''s smart. BURN! I can''t have competion.',
	'Gonna casually look at this. Oopsie, I accidentally lit it on fire',]

	names = Responses.Sassy.names
	names.extend(['pinkpanda', 'swiper', 'wasabi'])
	names.extend(['Intense cooking gave this kid mad ninja skills...beware'])

class ButterflyR(Responses.Sweet):
	names = Responses.Sweet.names
	messages = Responses.Sweet.messages
	names.extend(['Fwee', 'Fleur'])
	messages.extend('Fweeeeeee. I like to be Freeeeeee')

class TrollHunterR(Responses.Grumpy):
    battle_phrases = ["AHA! I've got you now, troll!", "Taste my fury, you hellish beast!", "Die, fiend, DIE!"]
    search_phrases = ["I'm coming for you, troll!", "I can smell your fear from a mile away!", "Run all you want, but you cannot hide from me--"]

class ComputerR(Responses.Sweet):
	names = Responses.Sweet.names
	names.extend(['R2D2', 'R2D2'])
	messages = ['So very handy. Try it!', 'Knows too much...suspiciously not human', 'Clink. Clink. Clack', 'Kind of adorable. A little monotoned and clinky but hey.']




