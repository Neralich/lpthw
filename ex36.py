# Import exit function
from sys import exit
import os


user_name = raw_input("What is your name?")

actions = ['- Talk', '- Attack', '- Run\n']
directions = ['- Left', '- Right', '- Straight', '- Up', '- Down', '- Back\n']

def start():
	print "\nYou awaken when a Troll guard comes into your cell."
	print "He puts your dinner on the floor and leaves,"
	print "but you realize he has forgotten to lock the door!"
	print "It's now or never, %s...You have to escape!" % user_name
	print "You sneak past him when he isn't looking, and run down the hallway."
	first_choice()

def first_choice():
	print "\nYou come to three doors.\n"
	print "Which will you take?"
	for i in directions[:3]:
		print i

	next = raw_input("> ")

	if next == "Left" or "Right":
		os.system('clear')
		troll_room()
	elif next == "Straight":
		dead("You walk in on a group of Trolls finishing their dinner, and promptly become their dessert.")
	else:
		print "That wasn't an option. Your misstep has caused you your freedom, as a Troll finds you and clubs you unconscious."
		start()

def troll_room():
	print "\nThere's a Huge Troll in this room!"
	troll_exhausted = False

	print "What are you going to do?\n"
	for i in actions:
		print i
	while True:

		next = raw_input("> ")
	
		if next == "Talk" and not troll_exhausted:
			os.system('clear')
			print "\nTrolls don't like to talk.  He hits you over the head"
			print "with his club and knocks you unconscious."
			start()
		elif next == "Attack" and not troll_exhausted:
			os.system('clear')
			dead("You can't beat a Troll!  Enraged, he clubs you to death.")
		elif next == "Run" and not troll_exhausted:
			os.system('clear')
			print "He chases you, but you run in circles until he collapses."
			print "Now what do you do?\n"
			for i in actions:
				print i
			troll_exhausted = True
		elif next == "Run" and troll_exhausted:
			dead("In your haste, you trip on his club, fall, and break your own neck.")
		elif next == "Attack" and troll_exhausted:
			os.system('clear')
			print "After you punch him in the face, the Troll shows you a secret passage."  
			print "You kill him, take his club, and exit the room into the passage."
# Add a got_club conditional?
# like armed = True?
			passage()
		elif next == "Talk" and troll_exhausted:
			print "The Troll says he will tell you where a great deal of gold is hidden if you spare his life. Intrigued, you step closer."
			dead("The Troll grabs you, pokes out your eyes, and crushes your head.")
		else:
			print "Quit wasting time! What are you going to do?"


def passage():
	print "You walk in the dark until you come to a dead end."
	print "There is a ladder on the wall. Where do you go?\n"
	for i in directions[3:]:
		print i

	ladder = raw_input()

	if ladder == "Up":
		riddle_room()
	elif ladder == "Down":
		dead("You climb down into a pit of snakes and die from 1,000 bites.")
	elif ladder == "Back":
		dead("A group of Trolls are waiting for you in the room. Enraged by what you've done to their friend, They tear off your arms and legs.")
	else:
		print "That's not an option."
		passage()

def riddle_room():
	os.system('clear')
	print "A croaky voice utters a powerful spell, and suddenly you're frozen in place, unable to move."
	print "Ahahahahahaha!\" says a little goblin sitting on a throne." 
	print "Welcome to the riddle room."
	print "\nAnswer my question correctly,"
	print "and I shall let thee go free."
	print "Respond wrong to what I've said,"
	print "and Trolls will come to make you dead."
	print "\nHere...is my question:"
	print "\tGuess a number, one through nine."
	print "\tGet within one, and you'll be fine."
	print "\tGet it exact and you'll get gold too,"
	print "\tBut guess anything else and bid your life adieu."

	riddle = int(raw_input("> ")))

	if 5 > riddle or riddle > 7:
		dead("Wrong! Trolls rush into the room and torture you for days before finally killing you.")
	elif riddle == 5 or riddle == 7:
		print "Great Job.  You're free!"
	elif riddle == 6:
		print "You are the smartest peraon on the planet. Enjoy your hard-earned gold!"
	else:
		dead("You're dropped into a boiling cauldron and cooked alive. Learn to count!")

def dead(why):
	os.system('clear')
	print why, "So sad!"
	exit(0)

start()	