AdventureGame
=============

Shrinidhi Thirumalai & Haley Pelletier



Type "help" at any time for a list of verbs and what they do!


Reflection:
We thought the assignment was really fun and a reasonable amount of work. It was exciting how we not only got to code, but had the chance to be creative with what we were making as well. It made us not only think about programming but the design process. It made us want to make our own adventure games from scratch.  :)

Our only concern is that because we had so much freedom, we weren't aware of the optimal ways in which to implement certain parts of our code. We had to think about what architecture would be best for characters to have personalities/responses/the ability to have conversations for a while, and we're still not sure if there's a better/more organized way to implement what we have. If we could get feedback on that bit, that would be great.



For Part 3, we implemented the following extensions:

	- Ability to talk to NPCs, which have distinct personalities. 

		-Phrase Types: You can choose one of 4 types of phrases to say to an NPC(getting help, gossiping, saying an insult, or saying a compliment). One of each type is pulled out randomly as an option for the player to say

		-Personalities: Each NPC has a personality and will respond appropriately based on their "personality". This Makes use of the responses class, which has "sassy", "grumpy", and "sweet" as three parent personalite. See responses.py and the talk() method in verbs.py for more info.

		-Code Specifics: 
			-Responses is a class containing a list of subclasses "sassy", "sweet", and "grumpy". Some players' personalities are chosen randomly from this list and others are assigned a specific personality based on type(TrollHunter = grumpy). 
			-Name and Message are static variables present in all response classes that are used in main to create objects with a certain name and message. 
			-Helps, insult, compliment, and gossip are attributes of each personality used when a person responds to a player's speech. A personality object is created as an atrribute of every single person in the game.

		-Example:
			What is thy bidding? talk Sophie-Sophomore

			What would you like to say?: 
			1. Pweeease help me?
			2. WHAT is up with the badninja? SO messed up...
			3. You wanna go, bro?
			4. Hey, you - up to be my partner in crime?

			4

			Blubbering-Fool says -- Hey, you - up to be my partner in crime?

			Sophie-Sophomore says -- Try that on someone stupider



	- Ability to take courses:
	 	- There are 4 courses placed in the classrooms of the AC
	 	- Upon taking all four, the player will complete a semster at Olin and win the game
	 	- See courses.py for more info.
	 	-Example:
		 	You are in Academic-Center-Room-326
			Home of AHS
			You see: AHS, hw-3
			You see: Joe-Junior
			You aren't holding anything.
			Exits: south

			What is thy bidding? take AHS

			Blubbering-Fool says -- I just took AHS! Gee, what a great class. I feel full of knowledge.


	- Sleeping: 
		- The player starts with 50 health. Every round, the player loses 1 health. Upon taking a class, the player loses 10 health.
		- When the player's health starts to get low, they will say something about how sleepy they are. The player can go to any dorm room in West Hall or East Hall to sleep.
		-They will wake up the next round with their health restored. See the sleep() method in verbs.py and sleeproom.py for more info.
		-Example:
			EX 1: 
			You are in East-Hall-First-Floor
			1st Floor of East Hall
			You see: johnny-5
			You see: pinkpanda
			You aren't holding anything.
			Exits: west, north, up

			What is thy bidding? sleep

			Blubbering-Fool says -- I can't sleep here, there's no bed!

			EX 2:
			You are in East-Hall-Room-116
			What a comfy room. Seems great for napping.
			The room is empty
			You see no one around
			You aren't holding anything.
			Exits: south

			What is thy bidding? sleep

			Blubbering-Fool says -- I got 10 hours of sleep... but that won't stop me from taking a nap!
			Blubbering-Fool sleeps for 14 hours before finally waking up.
			The clock ticks 16. 

