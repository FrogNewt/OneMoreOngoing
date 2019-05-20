#!/usr/bin/env python3

import sys
import os
import re
import pickle
import organisms
import creatures
import random
from shufflecipher import *
from environments import *
import classicenvironments
import pygame
import time




#debugging
grains = organisms.hpFood()

def begingame():
	def start():
		#pygame.mixer.init()
		#pygame.mixer.music.load('woodfrog.wav')
		#pygame.mixer.music.play()

		
		
		
		### USE DEBUGPOP FOR BUILDING; USE POPMAIN FOR NORMAL GAMES ###
		
		newplayer = Player()
		print("Hey--what's your name?")
		userinput = input("")
		newplayer.name = userinput
		print("######################################################################")
		print("Hi {0}!".format(newplayer.name))
		
		### USE POPMAIN FOR NORMAL GAMES AND DEBUGPOP FOR BUILDING ###
		#newplayer.popmaster = popmain.popmaster

		print("Oh--before we get started, we should pick a game mode!")
		print("(Press any key to continue)")
		input("")
		print("You can choose between 'Fixed' and 'Flex' modes:")
		print("(Press any key)")
		input("")
		print("\t'Fixed' (default) comes pre-loaded with common daily goals.")
		print("(Press any key)")
		input("")
		print("\t'Flex' mode allows you to choose and customize your own goals (recommended for people who trust themselves not to cheat!)")
		print("(Press any key)")
		input("")
		gameready = False
		while gameready == False:
			print("What would you prefer? (type 'flex' or 'fixed')")
			flexchoice = input("")
			if "l" in flexchoice.lower():
				newplayer.fixed = False
				newplayer.setactivitydict()
				gameready = True
			elif "d" in flexchoice.lower():
				newplayer.fixed = True
				newplayer.setactivitydict()
				gameready = True
			else:
				print("I didn't get your choice--can you try again? (type either 'fixed' or 'flex'")
		print("And would you rather play a modern, 'organism'-driven game or a classic 'rpg'-style game?")
		gameready = False
		while gameready == False:
			print("What would you prefer? (type 'organism' or 'rpg')")
			flexchoice = input("")
			if "o" in flexchoice.lower():
				newplayer.mode = "organism"
				gameready = True
				print("Please hold--we're shuffling all your organisms into the game!\n")
				popmain.shufflebegin()
				newplayer.popmaster = popmain.popmaster
			elif "p" in flexchoice.lower():
				newplayer.mode = "rpg"
				gameready = True
			else:
				print("I didn't get your choice--can you try again? (type either 'organism' or 'rpg'")

		soundready = False
		while soundready == False:
			print("One last thing--would you like to begin with sound 'on' or 'off'?")
			soundinput = input("")
			if "n" in soundinput:
				print("Sound on!")
				import pygame
				newplayer.soundon = True
				newplayer.musicon = True
				pygame.mixer.init()
				soundready = True
			elif "f" in soundinput:
				print("Sound off!")
				newplayer.soundon = False
				newplayer.musicon = False
				soundready = True
			else:
				print("I didn't get that--try again!")
		print("Got it--we're ready to go! (Press any key to continue)")
		input("")
		return newplayer

	while True:	
		print("######################################################################")
		welcome = input("Welcome back!  Would you like to start a new game or load an existing game? ")
		if "n" in welcome.lower():
			return start()

		elif "l" in welcome.lower():
			path = "Saves/"
			filelist = []
			if os.path.exists(path):
				for item in os.listdir(path):
						if item.endswith(".pickle"):
							filelist.append(item[:-7])
			if filelist:
				while True:
					print("######################################################################")
					print("These are the available files: ")
					for item in filelist:
						print(item)
					choosefile = input("What's your filename? (Give the exact filename!) ")
					if choosefile in filelist:
						truepath = os.path.join("Saves", choosefile+".pickle")
						with open(truepath, 'rb') as handle:
							newplayer = pickle.load(handle)
							return newplayer
					else:
						print("I can't find that file!")
			else:
				print("######################################################################")
				print("There are no saved files--starting a new game!")
				return start()
		else:
			print("Whoops--try again!")



def choosenext(self):
	while True:
		self.playmusic("Music/Vanadiel_March_1.ogg")
		print("######################################################################")
		print("So, {0}, what would you like to do next?  You can choose from any of these (or 'quit'):\n".format(self.name))
		for key in self.optionlist.keys():
			print(key.title())
		print("######################################################################")
		print("")
		ready = False
		usrinput = input("")
		if 'quit' in usrinput:
			self.quitsave()
		for option in self.optionlist.keys():
			if ((usrinput) and (usrinput.lower() in option) or (usrinput == option)) and usrinput != "":
				print("######################################################################")
				print(option.title())
				print("######################################################################")
				while ready == False:
					print("######################################################################")
					for key in self.optionlist[option].keys():
						print(key.title())
					print("######################################################################")
					print("What would you like to do?")
					print("######################################################################")
					usrinput2 = input("")
					for key in self.optionlist[option].keys():
						if ((usrinput2.lower() in key) or (usrinput2.lower() == key.lower())) and usrinput2 != "":
							if usrinput2 and ((usrinput2.lower() == "go back") or ("go back" in usrinput2) or ("0" in usrinput2)):
								ready = True
								break
							elif usrinput2 != "":
								self.optionlist[option][key]()
								break
					else:
						print("######################################################################")
						print("I didn't get that--try again!")
						print("######################################################################")
					
					
		if ready == False:
			print("Ooops--didn't get that!")


def shufflebegin(poplist):
	opened = organisms.openitup()
	popmaster = organisms.shuffleboth(organisms.givetype(organisms.scrapetypes(organisms.populatemaster(opened))))
	

	for organism in popmaster:
		organism.name = organism.meganame
	return popmaster
### TURN BACK ON AFTER DEBUGGING ###
#shufflebegin(popmaster)


# Creates an object in-game with just a name (mostly exists just to allow for the cultivation of new fixed elements later)
class gameObject(object):
	def __init__(self):
		self.name = name


# Used in generating the initial population list
class Population(gameObject):
	def __init__(self):
		self.name = "Organism-Mode Population Master"
		self.popmaster = []
	def shufflebegin(self, poplist = ""):
		opened = organisms.openitup()
		self.popmaster = organisms.shuffleboth(organisms.givetype(organisms.scrapetypes(organisms.populatemaster(opened))))
	#def rpgbegin(self, poplist = ""):
	#	self.name = "RPG-Mode Population Master"
	#	self.popmaster = creatures




# Anything alive gets this class
class livingThing(gameObject):
	def __init__(self, name="Living Thing", HP = 1):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True

# A class that represents anything that can take action
class Actor(livingThing):
	def __init__(self, name, HP = 0, MP = 0):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True

# Captures all actions and abilities unique to the player
class Player(Actor):
	def __init__(self, name = "Unknown"):
	# Fundamentals of the player
		self.name = name
		self.popmaster = []
		
	# Player Stats (Unaccessed during gameplay after initialization)
		self.maxHP = 10
		self.HP = 10
		self.strength = 1
		self.intellect = 1
		self.naturalism = 1
		#self.happiness = 1
		self.luck = 40
		self.fixed = True
		self.soundon = True
		self.musicon = True

	# USABLE Player stats--reference these in combat/interactions (rather than the originals)
		self.stats = {
		"HP" : self.HP,
		"Max HP" : self.maxHP,
		"Strength" : self.strength,
		"Intellect" : self.intellect,
		"Naturalism" : self.naturalism,
		"Luck" : self.luck
		}

	# Links experience categories to stat categories
		self.statexpdict = {
		"fitness" : "Strength",
		"fitness2" : "Max HP",
		"intellect" : "Intellect",
		"happiness" : "Luck",
		"naturalism" : "Naturalism"

		}

	# Aggregates experience by category

		self.expdict = {"fitness" : 0, "intellect" : 0, "naturalism": 0, "happiness" : 0, "game" : 0}



		self.orgsdict = {
		"set companion [1]" : self.setcompanion,
		"inspect companion [2]" : self.examinecompanion,
		"rename companion [3]" : self.renamecompanion,
		"feed companion [4]" : self.feedcompanion,
		"rest companion [5]" : self.restcompanion,
		"check resting organisms [6]" : self.checkresting,
		"breed organisms [7]" : self.breed,
		"view nursery [8]" : self.checknursery,
		"view bestiary [9]" : self.examinebestiary,
		"go back [0]" : self.goback

		}

		self.playerdict = {
		"add new activities [1]" : self.getactivities,
		"check stats [2]" : self.checkstats,
		"check inventory [3]" : self.checkinventory,
		"check my exp [4]" : self.checkexp,
		"check nature log [5]" : self.checklog,
		"go back [0]" : self.goback
		}

		self.exploredict = {
		"explore a new environment [1]" : self.explorenew,
		"explore my current environment [2]" : self.explorecurrent,
		"go back [0]" : self.goback

		}

		self.civdict = {
		"found a settlement [1]" : self.foundnew,
		"visit a settlement [2]" : self.visitsettlement,
		"go back [0]" : self.goback
		}

		self.settingsmenu = {
		"toggle flex [1]" : self.toggleflex,
		"toggle sound [2]" : self.togglesound,
		"toggle music [3]" : self.togglemusic,
		"save game [4]" : self.save,
		"go back [0]" : self.goback
		}

		# Creates list of all options for a player to choose
		self.optionlist = {
			#"add new activities" : self.getactivities,
			"explore the natural world [1]" : self.exploredict,
			"player options [2]" : self.playerdict,
			"care for your organisms [3]" : self.orgsdict,
			"explore civilization [4]" : self.civdict,
			
			"settings [5]" : self.settingsmenu
			#"[demo] print all animals" : self.printanimals,
			#"set companion" : self.setcompanion,
			#"examine companion" : self.examinecompanion,
			#"breed organisms" : self.breed,
			#"check nursery" : self.checknursery,
			#"play the game" : self.fourohfour,
			#"capture" : self.capture,
			#"check stats" : self.checkstats,
			#"check inventory" : self.checkinventory,
			#"examine bestiary" : self.examinebestiary,
			#"feed companion" : self.feedcompanion,
			#"rest companion" : self.restcompanion,
			#"check resting organisms" : self.checkresting,
			#"check nature log" : self.checklog,
			#"explore a new environment" : self.explorenew,
			#"explore my current environment" : self.explorecurrent,
			#"check my exp" : self.checkexp,
			#"toggle flex" : self.toggleflex,
			#"toggle sound" : self.togglesound,
			#"quit game" : self.quitsave
		}

	# Lists the possible environments available
		self.orgenvlist = {
			"meadow" : Meadow,
			"bog" : Bog,
			"swamp" : Swamp,
			"woods" : Woods,
			"plains" : Plain,
			"dark forest" : darkForest
		}
		self.rpgenvlist = {
			"meadow" : classicenvironments.Meadow,
			"bog" : classicenvironments.Bog,
			"swamp" : classicenvironments.Swamp,
			"woods" : classicenvironments.Woods,
			"plains" : classicenvironments.Plain,
			"dark forest" : classicenvironments.darkForest
		}

	# Lists the options available to a player within a given environment
		self.envoptions = {
			"sit patiently and wait to be approached [1]" : self.sit,
			"go out and carefully look for organisms [2]" : self.look,
			"go bounding through the environment [3]" : self.bound,
			"go back [0]" : self.goback
		}

	# Stuff the player has
		self.inventory = [grains]
		self.gold = 1000
		self.equipment = []
		self.bestiary = []
		self.naturelog = []
		self.nursery = []
		self.companion = ""
		self.formercompanion = ""
	
	# Things the player may need to "hold" in order to advance the game
		self.randomnum = 0
		self.mode = "modern"
		self.currentenv = ""
		self.currentoccupants = []
		self.target = []
		self.brokenloop = True
		self.bounded = False
		self.sat = False
		self.looked = False
		self.sitnum = 0
		self.looknum = 0
		self.boundnum = 0
		self.damage = 0
		self.safe = True
		self.previoustarget = ""
		self.tempenemy = self
		self.excludestats = ["Max HP", "Gold", "Exp"]
		self.hotel = []
		self.settlements = []
		self.scavenged = False
		self.correctstr = False
		#self.businesses = []
		self.visiting = ""
		self.switch = False
		self.patron = ""

	# For breeding organisms
		self.dam = ""
		self.sire = ""
	
	# Returns a list containing the current day
	
	def currenttime(self):
		now = int(time.time())
		return now
	### THIS METHOD PRINTS OUT A LIST THAT CONTAINS THE DAY OF THE WEEK, MONTH, DAY, AND YEAR (FOR EXACTNESS)
	def currentday(self):
		date = time.ctime().split(":")[0].split()[0:3]
		year = time.ctime().split(":")[2].split()[1]
		date.append(year)
		return date

	def days_since(self, start_time, finish_time):
		in_seconds = int(finish_time) - int(start_time)
		days = in_seconds // 86400
		return days

	def currenthour(self):
		date = time.ctime().split()[:3]
		hour = time.ctime().split()[3].split(":")[0]
		date.append(hour)
		return date

	def hours_since(self, start_time, finish_time):
		in_seconds = int(finish_time) - int(start_time)
		hours = in_seconds // 3600
		return hours

	def currentmin(self):
		minute = time.ctime().split()[3].split(":")[:2]
		return minute

	def minutes_since(self, start_time, finish_time):
		in_seconds = int(finish_time) - int(start_time)
		minutes = in_seconds // 60
		return minutes

	def currentsec(self):
		second = time.ctime().split()[3].split(":")[:3]
		return second

	def seconds_since(self, start_time, finish_time):
		in_seconds = int(finish_time) - int(start_time)
		return in_seconds


	def addtolog(self):
		if self.target not in self.naturelog:
			print("######################################################################")
			print("{0} (a {1}) added to your nature log!".format(self.target.name.title(), self.target.type.title()))
			self.naturelog.append(self.target)

	def attack(self):
		def setdamage(self):
			self.damage = random.randint(self.stats["Strength"], self.stats["Strength"] + self.stats["Luck"])
		setdamage(self)
		self.target.stats["HP"] -= self.damage
		print("{0} attacks the {1} for {2}!".format(self.name, self.target.name, self.damage))

	def befriend(self):
		targetindex = (self.target.stats["Skittishness"] + self.target.stats["Luck"]) // 2
		playerindex = (self.stats["Naturalism"] + self.stats["Luck"]) // 2
		print("You attempt to befriend the {0}!".format(self.target.name))
		input("")
		if targetindex >= playerindex:
			print("You failed--the {0} isn't having it!".format(self.target.name))
		elif targetindex < playerindex:
			print("You did it--you've befriended the {0}!  It follows you into the bestiary!".format(self.target.name))
			if self.bounded == True:
				randnum = random.randint(1,3)
				if randnum == 1:
					print("Looks like bounding after this thing weakened it...that happens sometimes.")
					for stat in self.target.stats.keys():
						self.target.stats[stat] = self.target.stats[stat] - 2
						if self.target.stats[stat] < 1:
							self.target.stats[stat] = 1
					self.bounded = False
			elif self.sat == True:
				randnum = random.randint(1,10)
				if randnum == 1:
					print("### BOOST ###")
					print("Looks like your caution paid off--because this one didn't panic, it has elevated stats!")
					print("######################################################################")
					for stat in self.target.stats.keys():
						self.target.stats[stat] = self.target.stats[stat] + 3
				self.sat = False
			self.bestiary.append(self.target)
			self.currentenv.occupants.pop(self.currentenv.occupants.index(self.target))
			self.safe = True
			if not self.companion:
				self.companion = self.target
				self.bestiary.pop(self.bestiary.index(self.companion))
				print("{0} has been set as your companion!".format(self.companion.name))

	def bound(self):
		print("\n ### GO BOUNDING AFTER THINGS ### ")
		self.bounded = True
		print("######################################################################")
		print("You go bounding after something!")
		if not self.currentenv.occupants:
			print("There's nothing here...try another environment!")
			return

		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		
		def makeboundnum(self):
			self.boundnum = random.randint(1,self.stats["Luck"])
		
		#Checks whether or not the target gets super-strength as a result of your intrusion
		def checkberserk(self):
			if self.target.stats["Luck"] > self.boundnum:
				self.target.berserk = True

			if self.target.berserk == True:
				self.target.stats["Strength"] = self.target.stats["Strength"] * 2
				print("(And it looks PISSED, which means it's going to be stronger but give more exp!)")
				self.target.stats["Exp"] *= 2

		self.target = ""
		chosen = False
		possible = False
		print("You bound into {0}!".format(self.currentenv.name))
		input("(Press any key to find out what you've crashed into!)")
		makeboundnum(self)
		makerandom(self)
		occupant = self.currentenv.occupants[self.randomnum]
		self.target = occupant
		
		
		

		print("You've crashed into a wild {1}--and it looks like a {0}!".format(self.target.name, self.target.type))
		
		# Assign berserk status of target
		checkberserk(self)
		
		# Add organism to nature log if yet unseen
		self.addtolog()
		self.encounter()
		self.bound = False

	# Attempts to capture the current target
	#def capture(self):
		#self.bestiary.append(organism)
		#print("You've captured a wild {0}--it looks like it might be a {1}!".format(organism.name, organism.type))
		#print(self.bestiary)
		pass

	# Links categories and related activities ("FLEX" version)
	def setactivitydict(self):
		if self.fixed == False:
		# Sets categories to be used (empty) for flex mode for leveling-up
			self.activitydict = {
			"fitness" : {}, 
			"intellect" : {}, 
			"naturalism" : {}, 
			"happiness" : {}
			}
		elif self.fixed == True:
		# Sets activities to be included in "fixed" mode for leveling-up
			self.activitydict = {
			"fitness" : {
				"walked" : 10, 
				"jogged" : 20,
				"swam" : 25,
				"ate healthy" : 10,
				"worked-out": 30,
				"ran a marathon" : 50,
				"slept well" : 10
				},
			"intellect" : {
				"read a paper" : 20, 
				"worked on manuscript" : 30,
				"learned a skill" : 20,
				"taught someone" : 15,
				"learned something interesting" : 5,
				"met with a professor" : 15
			},
			"naturalism" : {
				"hiked" : 25,
				"identified a wild organism" : 10,
				"collected litter" : 5,
				"watered plants" : 10,
				"planted something" : 40,
				"spent time outdoors" : 10
				},
			"happiness" : {
				"gave a compliment" : 20,
				"ate something delicious" : 15,
				"helped someone" : 25,
				"kept my cool" : 30,
				"gave a gift" : 35,
				"offered help" : 5,
				"meditated" : 20,
				"played with a pet" : 25
			},
			}
	
	def breed(self):
		print("### BREED ORGANISMS ###")
		if not self.nursery:
			self.excludestats = ["Max HP", "Gold", "Exp"]

			class Typeholder(object):
				def __init__(self):
					self.type = ""
					self.females = 0
					self.males = 0
					self.ready = False

			breedready = False
			typeset = set()

			typeholderlist = []
			if self.bestiary:
				for org in self.bestiary:
					typeset.add(org.type)
			else:
				print("You don't have anything in your bestiary...yet!")
				print("######################################################################")
				return
			for orgtype in typeset:
				reptype = Typeholder()
				reptype.type = orgtype
				for org in self.bestiary:
					if org.type == reptype.type:
						if org.sex == "female":
							reptype.females += 1
						elif org.sex == "male":
							reptype.males += 1
				print(reptype.type + ":" + str(reptype.males) + " males, " + str(reptype.females) + " females")
				if (reptype.males > 0) and (reptype.females > 0):
					typeholderlist.append(reptype)
					reptype.ready = True
					breedready = True
			if breedready == False:
				print("You don't have enough males and females of a given type who aren't related, yet!")
				print("######################################################################")
				return
			


			readyfemales = []
			readymales = []
			femindex = 0
			mindex = 0
			matingdone = False
			if matingdone == False:
				femalechosen = False
				while femalechosen == False and breedready == True:
					if breedready == True:
						print("######################################################################")
						print("Remember, you can only breed two organisms at a time!")
						print("Which female would you like to breed?")
						for typeholder in typeholderlist:
							if typeholder.ready == True:
								for org in self.bestiary:
									if org.type == typeholder.type:
										if org.sex == "female":
											org.index = femindex
											readyfemales.append(org)
											femindex += 1
											print("Name: " + org.name)
											print("Type: " + org.type)
											print("Index: " + str(org.index))
											if org.damID:
												print("Dam ID: " + str(org.damID))
											if org.babyID:
												print("Baby ID: " + str(org.babyID))
											for stat in org.stats.keys():
												if stat not in self.excludestats:
													print(stat, org.stats[stat])
											print("\n")
								print("\n")
						print("Which female would you like to breed? (Available females are listed above--you can also type 'leave')")
						userfemale = input("")
						if "leave" in userfemale:
							print("Ok--leaving the breeding area.")
							print("######################################################################")
							return
						for org in readyfemales:
							if (userfemale == org.name) or (userfemale == str(org.index)):
								self.dam = org
								femalechosen = True
						if not self.dam:
							print("Ooops--didn't get that!  Try again.")

				malechosen = False
				while malechosen == False:
					print("######################################################################")
					for org in self.bestiary:
						if org.type == self.dam.type:
							if org.sex == "male":
								readymales.append(org)
								org.index = mindex
								mindex += 1
								print("Name: " + org.name)
								print("Type: " + org.type)
								print("Index: " + str(org.index))
								for stat in org.stats.keys():
									if stat not in self.excludestats:
										print(stat, org.stats[stat])
								print("\n")
					while malechosen == False:
						print("Which male would you like to breed? (Available males are listed above--you can also type leave)")
						usermale = input("")
						if "leave" in usermale:
							print("Ok--leaving the breeding area.")
							return
						if usermale:
							for org in readymales:
								if (usermale == org.name) or (usermale == str(org.index)):
									self.sire = org
									malechosen = True
									break
						if malechosen == False:
							print("I didn't get that--can you enter the male's ID again?")


					print("Got it--you want to breed {0} ({1}) with {2} ({3})!".format(self.dam.name, self.dam.sex, self.sire.name, self.sire.sex))
					print("This baby won't be ready until tomorrow--are you sure you want to lose access to these two parents until then?")
					userwait = input("")
					if "y" in userwait:
						print("Ok--check back tomorrow!")
						self.dam.matedtime = self.currenttime()
						self.bestiary.pop(self.bestiary.index(self.dam))
						self.bestiary.pop(self.bestiary.index(self.sire))
						self.nursery.append(self.dam)
						self.nursery.append(self.sire)
						matingdone = True
						
					else:
						print("Leaving the breeding area!")
						return


				if matingdone == False:
					print("I didn't get that--type the index or the name of the individual you're wanting to breed.")

				

			else:
				print("You don't have a male and female pair of any one type, yet!")
				return

		else:
			print("You've already got a pair of parents in the nursery--they'll have to finish-up before you can breed anyone else!")

		print("######################################################################")


		





	# Checks to see how much experience the user has in each area
	def checkexp(self):
		print("\n ### CHECK MY EXP ### ")
		for thing in self.expdict.keys():
			print(thing.capitalize() + ": " + str(self.expdict[thing]))
		print("######################################################################")

	def checkinventory(self):
		print("\n ### CHECK INVENTORY ### ")
		print("Gold: {0}".format(self.gold))
		if self.inventory:
			print("Here's what you have in your inventory right now:")
			for element in self.inventory:
				print("\t" + element.name.capitalize())
		else:
			print("You don't have anything in your inventory right now.")
		print("######################################################################")

	def checknursery(self):
		print("\n ### CHECK NURSERY ### ")
		if not self.nursery:
			print("Your nursery is currently empty--come back after you've bred two adults of the same type!")
			print("######################################################################")
			input("")
			return
		print("######################################################################")
		
	# Splits ctime output to produce an element of the current time (e.g. day, month, hour, etc)
		newtime = self.currenttime()

		gestation = int(self.minutes_since(self.dam.matedtime, newtime))
		
	# Checks to see if the baby is ready, yet
		if gestation > 1:
			newbaby = organisms.Organism()
			print("Congratulations--you've got a new baby!")

		# Sets the new baby's stats
			# New baby gets an "ID" that it then shares with mom and dad to prevent breeding with offspring
			newbaby.babyID = random.randint(1,1000000)
			self.sire.sireID = newbaby.babyID
			self.dam.damID = newbaby.babyID
			
			# Sets the new baby as a standard orgnaism
			newbaby = organisms.Organism()

			# Gives the new baby the same type as its mother
			newbaby.type = self.dam.type

			# Makes newbaby into a list so that it can be processed by "givetype"
			offspring = [newbaby]

			# Gives newbaby a name that's half its mom and half its dad
			if self.mode == "organism":	
				species = self.sire.name.split()
				if len(species) > 1:
					species = species[1]
				else:
					species = species[0]
				genus = self.dam.name.split()
				genus = genus[0]
				organisms.givetype(offspring)
				newbaby = offspring[0]
				newbaby.name = genus.capitalize() + " " + species.lower()
				newbaby.evolvable = False
			if self.mode == "rpg":
				randomnum = random.randint(0,1)
				if randomnum == 1:
					newbaby.name = self.sire.species
					newbaby.species = self.sire.species
				elif randomnum == 0:
					newbaby.name = self.dam.species
					newbaby.species = self.dam.species


			hybridvigor = False
			for stat in self.dam.stats.keys():
				if stat in self.sire.stats.keys():
					if (self.dam.stats[stat] % 2 == 0) and (self.sire.stats[stat] % 2 == 0):
						newbaby.stats[stat] = self.sire.stats[stat] + self.dam.stats[stat]
						hybridvigor = True
					elif (self.dam.stats[stat] % 2 != 0) and (self.sire.stats[stat] % 2 != 0):
						newbaby.stats[stat] = self.sire.stats[stat] + self.dam.stats[stat]
						hybridvigor = True
					else:	
						newbaby.stats[stat] = ((self.sire.stats[stat] + self.dam.stats[stat]) // 2)

			print("\n\tMom:")
			print("\tName: " + self.dam.name) 
			print("\tType: " + self.dam.type)
			print("\tSex: " + self.dam.sex.capitalize())
			for stat in self.dam.stats.keys():
				if stat not in self.excludestats:
					print("\t\t" + stat + " " + str(self.dam.stats[stat]))

			print("\n\tDad:")
			print("\tName: " + self.sire.name) 
			print("\tType: " + self.sire.type)
			print("\tSex: " + self.sire.sex.capitalize())
			for stat in self.sire.stats.keys():
				if stat not in self.excludestats:
					print("\t\t" + stat + " " + str(self.sire.stats[stat]))


			print("\n\tThe new baby is a hybrid of mom and dad:")
			if hybridvigor == True:
				print("\t...and hey--this one's got hybrid vigor (at least one enhanced trait)!")
			print("\tName: " + newbaby.name)
			print("\tType: " + newbaby.type) 
			print("\tSex: " + newbaby.sex.capitalize())
			
			# Assigns specific stats to baby
			for stat in newbaby.stats.keys():
				if stat not in self.excludestats:
					print("\t\t" + stat + " " + str(newbaby.stats[stat]))
			
			# Puts mom and dad back in bestiary
			self.bestiary.append(self.sire)
			self.bestiary.append(self.dam)

			# Clears these variables for use again
			self.sire = ""
			self.dam = ""

			# Empties the nursery
			self.nursery = []

			# Puts baby into bestiary
			self.bestiary.append(newbaby)
		else:
			print("Looks like the baby's not ready yet--the parents are still nesting!  Come back tomorrow.")
			print("######################################################################\n")


	def actexpdump(self):
		for exptype in self.expdict.keys():
			while self.expdict[exptype] > 100:				
				for key in self.statexpdict.keys():
					if exptype.lower() in key.lower():
						self.stats[self.statexpdict[exptype]] += 1
						self.expdict[exptype] -= 100
				



	# Allows for the founding of a new settlement
	def foundnew(self):
		def found(self):
			place = Village()
			place.viscapacity += place.popularity
			self.settlements.append(place)
			location = self.settlements.index(place)
			print("######################################################################")
			print("You've just founded a new village!")
			print("######################################################################")
			print("What would you like to name it? (Note:  It's going to get a 'ville' at the end of it!)")
			print("######################################################################")
			usrinput2 = input("")
			if usrinput2:
				self.settlements[location].name = (usrinput2+"ville").title()
			print("Ok--you've founded {0}!".format(self.settlements[location].name))
			print("######################################################################")

		print("######################################################################")
		print("Would you like to found a new village?  It'll cost {0} gold!".format(Village.cost))
		print("######################################################################")
		usrinput = input("")
		if usrinput:
			if "y" in usrinput and self.gold >= Village.cost:
				found(self)
				self.gold -= Village.cost
			elif "y" in usrinput and self.gold < Village.cost:
				print("You don't have enough gold for that, yet!")
				print("######################################################################")
			else:
				print("No problem.  We can work on this another time.")
				print("######################################################################")
		else:
			print("Whoops--did you want to found a new village?  Type 'yes' or 'no'!")


	def openshop(self):
		if self.gold >= basicShop.cost:
			print("######################################################################")
			print("Are you sure you want to open a shop?  It'll cost you {0} gold!".format(basicShop.cost))
			print("######################################################################")
			usrinput = input("")
			if usrinput:
				if "y" in usrinput:
					newshop = basicShop()
					if not self.visiting.businesses:
						self.visiting.businesses.append(newshop)
						location = self.visiting.businesses.index(newshop)
						print("######################################################################")
						print("Congratulations--you've just opened your very first shop!")
						print("######################################################################")
						print("What would you like to call it?!")
						print("######################################################################")
						usrinput = input("")
						self.visiting.businesses[location].name = usrinput.title()
						print("All right--{0} will be open for business...starting tomorrow!".format(newshop.name))
						self.visiting.businesses[location].firstone = True
						print("######################################################################")

					elif self.visiting.businesses:
						self.visiting.businesses.append(newshop)
						location = self.visiting.businesses.index(newshop)
						print("Congratulations--you've opened a new shop!")
						print("Let's name this one--go ahead:")
						usrinput = input("")
						self.visiting.businesses[location].name = usrinput.title()
						print("All right--{0} will be open for business...starting tomorrow!".format(newshop.name))
						print("######################################################################")
				else:
					print("Ooops--try again!")

	def add_to_sanctuary(self):
		print("Do you want to add an organism to the sanctuary?  Once they go in, they can never come back out (though they might produce offspring that can leave the sanctuary...)!")
		usrinput = input("")
		if "y" in usrinput:
			print("Ok!  Who do you want to add to the sanctuary?")

	def opensanctuary(self):
		if self.gold >= basicSanc.cost:
			print("######################################################################")
			print("Are you sure you want to open a wildlife sanctuary?  It'll cost you {0} gold!".format(basicSanc.cost))
			print("######################################################################")
			usrinput = input("")
			if usrinput:
				if "y" in usrinput:
					newsanc = classicenvironments.basicSanc()
					if not self.visiting.sanctuary:
						self.visiting.sanctuary = newsanc
						print("######################################################################")
						print("Congratulations--you've got yourself a wildlife sanctuary!")
						print("(...it's empty, though.)")
						print("######################################################################")
						print("What would you like to call it?!")
						print("######################################################################")
						usrinput = input("")
						self.visiting.sanctuary.name = usrinput.title() + " " + "Wildlife Sanctuary"
						print("All right--{0} is ready!".format(newsanc.name))
						input("")
						print("######################################################################")
				else:
					print("Ooops--try again!")

	def visitsanctuary(self):
		if self.visiting.sanctuary:
			sancmenu = {
			"release wildlife into sanctuary [1]" : self.add_to_sanctuary,
			"go back [0]" : self.goback
			}

			self.switch = False
			while self.switch == False:
				print("######################################################################")
				print("### MANAGE {0} ### \n".format(self.visiting.sanctuary.name.upper()))
				print("######################################################################")
				for menuitem in sancmenu.keys():
					print(menuitem.title())
				print("\nWhat do you want to do at {0}?".format(self.visiting.sanctuary.name))
				usrinput = input("")
				if usrinput.lower() in "go back":
					break
				for menuitem in sancmenu.keys():
					if usrinput.lower() in menuitem.lower():
						sancmenu[menuitem]()
		else:
			print("You don't have a sanctuary--found one!")


	def pickshop(self):
		if self.visiting.businesses:
			while not self.patron:
				print("######################################################################")
				print("Which shop do you want to visit?")
				print("######################################################################")
				for business in self.visiting.businesses:
					print(business.name.title())
				print("######################################################################")
				print("")
				usrinput = input("")
				for shop in self.visiting.businesses:
					if usrinput.lower() in shop.name.lower():
						self.patron = shop
						break
				else:
					print("Which shop, again?")
			print("You're visiting {0}!".format(self.patron.name))
			print("######################################################################")
			self.checkshop()
			self.patron = ""
		else:
			print("######################################################################")
			print("{0} doesn't have any shops, yet!".format(self.visiting.name))
			print("######################################################################")


	def checkearnings(self):
		if self.patron.sold:
			print("It looks like you've sold:")
			print("")
			for solditem in self.patron.sold:
				print(solditem.name.title() + " " + "for " + str(solditem.price) + " " + "to " + solditem.boughtby.title())
				input("")
			self.gold += self.patron.earnings
			print("######################################################################")
			print("You've earned {0} gold!".format(self.patron.earnings))
			print("######################################################################")
			self.patron.earnings = 0
			self.patron.sold.pop(self.patron.sold.index(solditem))
		else:
			print("######################################################################")
			print("You haven't sold anything, yet!")
			print("######################################################################\n")
			input("")

	def inspectshoppers(self):
		if self.patron.shoppers:
			for shopper in self.patron.shoppers:
				print("Name: " + shopper.name.title())
				print("Preference: " + shopper.likes.title())
				print("Likes this element: " + shopper.element.title())
				print("Is this aloof:" + str(shopper.aloofness))
				print("Had this level of interest in the shop: " + str(shopper.comfort))
				if shopper.targetitem:
					print("Looking at: " + shopper.targetitem.name)
					print("Has {0} interest in buying it...".format(shopper.buyinterest))
				print("Has {0} gold!".format(shopper.gold))
				print("")
		else:
			print("You currently have no shoppers")


	def checkshop(self):
		shopmenu = {
		"put something up for sale [1]" : self.sellatshop,
		"remove something from the market [2]" : self.removefromshop,
		"inspect shoppers [9]" : self.inspectshoppers,
		"view my wares [3]" : self.viewmywares,
		"check earnings [4]" : self.checkearnings,
		"set the shop mascot [5]" : self.setmascot,
		"go back [0]" : self.goback
		}
		self.patron.shoppers = []
		for visitor in self.visiting.peoplepresent:
			visitor.shop(self)

		if self.patron:
			self.switch = False
			while self.switch == False:
				print("######################################################################")
				print("### MANAGE SHOP ({0}) ### \n".format(self.patron.name.upper()))
				print("######################################################################")
				if self.patron.mascot:
					print("")
					print("Current shop mascot:")
					print(self.patron.mascot.name + " ({0})".format(self.patron.mascot.type))
					print("")
				for menuitem in shopmenu.keys():
					print(menuitem.title())
				print("\nWhat do you want to do at {0}?".format(self.patron.name))
				usrinput = input("")
				if usrinput.lower() in "go back":
					break
				for menuitem in shopmenu.keys():
					if usrinput.lower() in menuitem.lower():
						shopmenu[menuitem]()

	def removefromshop(self):
		while True and self.patron.forsale:
			hit = False
			print("######################################################################")
			print("### REMOVE ITEMS FROM MARKET ###")
			print("######################################################################")
			print("")
			i = 0
			for item in self.patron.forsale:
				item.index = i
				print(item.name.title())
				print("Cost: " + str(item.price))
				print("Index: " + str(i))
				i += 1
				print("\n")
			print("")
			print("What do you want to remove from the market? (Type the index or 'leave')")
			usrinput = input("")
			if ('leave' in usrinput) or 'leave' == usrinput:
				print("Leaving!")
				break
			for item in self.patron.forsale:
				if str(item.index) == usrinput:
					self.inventory.append(item)
					print("######################################################################")
					print("You've taken {0} off the market--back into inventory!".format(item.name))
					print("######################################################################")
					input("")
					self.patron.forsale.pop(self.patron.forsale.index(item))
					hit = True
			if hit == True:
				print("Want to remove anything else?")
				usrinput2 = input("")
				if "y" in usrinput2:
					pass
				else:
					break
			else:
				print("I didn't get that--type the index of the item you want to remove!")
		else:
			print("######################################################################")
			print("Your marketplace is empty!")
			print("######################################################################\n")
			input("")


	def viewmywares(self):
		if self.patron.forsale:
			print("######################################################################")
			print("### VIEW MY WARES ###")

			print("")
			print("Here's what you have for sale right now:")
			for item in self.patron.forsale:
				print("\tItem: " + str(item.name.title()))
				print("\tCost: " + str(item.price) + " gold")
				print("")
		else:
			print("######################################################################")
			print("You don't have anything up for sale, right now.")
			print("######################################################################")
			print("")

	def sellatshop(self):
		if self.inventory:
			self.switch = False
			while self.switch == False and self.inventory:
				if self.patron.counterspace > len(self.patron.forsale):
					print("######################################################################")
					print("Available from inventory:")
					for item in self.inventory:
						print("\t" + item.name.title())
					print("")
					print("What would you like to sell? (or you can type 'leave')")
					usrinput = input("")
					if 'leave' in usrinput:
						print("Ok--we'll sell things later.")
						break
					for item in self.inventory:
						if usrinput.lower() in item.name.lower():
							print("######################################################################")
							print("How much do you want to sell it for? (Enter any price in gold above zero--just the number!)")
							usrinput2 = input("")
							print("######################################################################")
							if str.isdigit(usrinput2) and int(usrinput2) != 0:
								self.patron.forsale.append(item)
								itemindex = self.patron.forsale.index(item)
								self.patron.forsale[itemindex].price = int(usrinput2)
								print("Ok--you've put the {0} up for {1} gold!".format(item.name, str(self.patron.forsale[itemindex].price)))
								invindex = self.inventory.index(item)
								self.inventory.pop(invindex)
								print("(Press enter to continue)")
								input("")
								if self.inventory:
									print("Do you want to sell anything else?")
									usrinput3 = input("")
									if "y" in usrinput3:
										pass
									else:
										self.switch = True
										break
							else:
								print("Ooops--enter an integer (a whole number) greater than zero!")

							break
				elif not self.inventory and self.patron.counterspace < len(self.patron.forsale):
					print("You're out of things to sell AND you're out of counter-space!")
				elif not self.inventory:
					print("You don't have anything left to sell!")
				else:
					print("You don't have the space for that--come back when something has sold (or take something off the market)!")
					break
			
		else:
			print("######################################################################")
			print("You don't have anything to sell, yet.")
			print("######################################################################")

	def setmascot(self):
		if self.bestiary:
			if not self.patron.mascot:
				print("Prospective mascots:\n")
				i = 0
				for beast in self.bestiary:
					beast.index = i
					print("\t" + beast.name)
					print("\t" + "Type: " + beast.type)
					print("\tIndex: " + str(beast.index))
					print("\n")
					i += 1
				print("Who would you like to set as the shop's mascot? (Type the organism's index!)")
				print("######################################################################")
				usrinput = input("")
				for beast in self.bestiary:
					if usrinput == str(beast.index):
						self.patron.mascot = beast
						self.bestiary.pop(self.bestiary.index(self.patron.mascot))
						break
				if self.patron.mascot:
					print("You've set {0} as the {1} mascot!".format(self.patron.mascot.name, self.patron.name))
					input("")
					print("######################################################################")
			elif self.patron.mascot:
				print("{0}'s current mascot is {1} (a {2})--do you want to replace it?".format(self.patron.name, self.patron.mascot.name, self.patron.mascot.type))
				usrinput = input("")
				if "y" in usrinput:
					print("Prospective mascots:\n")
					i = 0
					for beast in self.bestiary:
						beast.index = i
						print("\t" + beast.name)
						print("\t" + "Type: " + beast.type)
						print("\tIndex: " + str(beast.index))
						print("\n")
						i += 1
					print("Who would you like to set as the shop's mascot? (Type the organism's index!)")
					print("######################################################################")
					usrinput = input("")
					for beast in self.bestiary:
						if usrinput == str(beast.index):
							self.patron.mascot = beast
							self.bestiary.pop(self.bestiary.index(beast))
							break
				else:
					print("Ok--we'll leave {0} as the mascot for now!".format(self.patron.mascot.name))
		else:
			print("######################################################################")
			print("You don't have anyone in your bestiary to set as a mascot right now!")
			print("######################################################################")


	def genmenagerie(self):
		if self.visiting and (self.visiting.menagerieopen == False) and (self.gold >= self.visiting.menageriecost):
			print("######################################################################")
			print("Would you like to found a menagerie?  This will help you attract visitors who may become residents in your settlement!")
			print("It'll cost you {0} gold!".format(self.visiting.menageriecost))
			print("######################################################################")
			usrinput = input("")
			if "y" in usrinput:
				self.gold -= self.visiting.menageriecost
				print("Ok--you've paid {0} gold and opened your menagerie for business!".format(str(self.visiting.menageriecost)))
				print("######################################################################")
				self.visiting.menagerieopen = True
			else:
				print("No problem--we'll do it another time.")
				print("######################################################################")
		elif self.visiting.menagerieopen == True:
			print("You already have a menagerie here, and you can only have one per settlement!")
			print("If you want to expand your menagerie, upgrade your settlement from a {0} to a {1}!".format(self.visiting.type, self.visiting.upgrade))
			print("######################################################################")

		elif not self.visiting:
			print("You haven't founded a settlement, yet!")
			print("######################################################################")
		elif self.gold < self.visiting.menageriecost:
			print("You can't afford to open a menagerie, yet...")
			print("######################################################################")


	def visitmenagerie(self):
		self.switch = False
		if self.visiting.menagerieopen == True:
			menu = {
			"add someone to the menagerie [1]" : self.addtomenagerie,
			"remove someone from the menagerie [2]" : self.delfrommenagerie,
			"go back [0]" : self.goback
			}

			while self.switch == False:
				if self.visiting.menagerie:
					print("Here's what's currently in your menagerie:")
					for organism in self.visiting.menagerie:
						print("Name: " + organism.name)
						print("Type: " + organism.type + "\n")
				else:
					print("######################################################################")
					print("Your menagerie is currently empty!")
					print("######################################################################")
				for item in menu.keys():
					print(item.title())
				print("######################################################################")
				print("What would you like to do?")
				print("######################################################################")
				usrinput = input("")
				if usrinput.lower() in "go back":
					break
				for item in menu.keys():
					if usrinput and (((usrinput.lower() in item) or (usrinput.lower() == item))):
						menu[item]()
						self.switch = True
				

				if self.switch == False:
					print("######################################################################")
					print("I didn't get that--try again!")
					print("######################################################################")
		elif not self.visiting.menagerie:
			print("######################################################################")
			print("{0} doesn't have a menagerie yet--you'll have to go buy one, first!".format(self.visiting.name))
			print("######################################################################")


	def delfrommenagerie(self):
		while True:
			if self.visiting.menagerie:
				i = 0
				for org in self.visiting.menagerie:
					org.index = i
					print(org.name)
					print("Type: " + org.type)
					print("Index: " + str(org.index))
					i += 1
					print("\n")


				print("Who do you want to remove from the menagerie? (Type the organism's index)")
				usrinput = input("")

				for org in self.visiting.menagerie:
					if usrinput == str(org.index):
						popspot = self.visiting.menagerie.index(org)
						self.bestiary.append(org)
						self.visiting.menagerie.pop(popspot)
						print("{0} has been removed from the menagerie and returned to the bestiary!".format(org.name))
						break
				input("(Press enter to continue)")
				
				print("Do you want to remove anyone else?")
				usrinput2 = input("")
				if "y" in usrinput2:
					pass
				else:
					print("Ok--moving on!")
					input("(Press enter to continue)")
					break

			elif not self.visiting.menagerie:
				print("Your menagerie is empty!")
				break




	def addtomenagerie(self):
		if self.bestiary and len(self.visiting.menagerie) < self.visiting.menageriesize:
			while (len(self.visiting.menagerie) < self.visiting.menageriesize):
				print("######################################################################")
				print("Do you want to add someone to your menagerie?  It's currently holding a total of {0}/{1} organisms!".format(len(self.visiting.menagerie),self.visiting.menageriesize))
				print("######################################################################")
				usrinput = input("")
				if "y" in usrinput and self.bestiary:
					i = 0
					for beast in self.bestiary:
						beast.index = i
						print("Index: {0}".format(beast.index))
						print("Name: {0}".format(beast.name))
						print("Type: {0}".format(beast.type))
						print("Stats: ")
						for stat in beast.stats.keys():
							print(stat + ": " + str(beast.stats[stat]))
						i += 1
						print("\n")
					print("######################################################################")
					print("Who would you like to add to the menagerie? (Type the 'index'!)")
					print("######################################################################")
					usrinput = input("")
					for beast in self.bestiary:
						if usrinput == str(beast.index):
							self.visiting.menagerie.append(beast)
							self.bestiary.pop(self.bestiary.index((beast)))
							print("######################################################################")
							print("You've removed {0} from the bestiary and added it to the menagerie!".format(beast.name))
							print("######################################################################")
							self.visiting.popularity += 1
							break
				else:
					print("Your bestiary is empty!")
					break
		elif not self.bestiary:
			print("######################################################################")
			print("You don't have anyone in your bestiary to add, yet!")
			print("######################################################################")
		if len(self.visiting.menagerie) == self.visiting.menageriesize:
			print("######################################################################")
			print("Your menagerie is currently full ({0}/{1} organisms)!".format(len(self.visiting.menagerie), self.visiting.menageriesize))
			print("######################################################################")

	def genvisitors(self):
		self.visiting.visitors = []
		self.visiting.peoplepresent = self.visiting.residents
		namelist = []
		for person in self.visiting.peoplepresent:
			namelist.append(person.name)
		while len(self.visiting.visitors) < self.visiting.viscapacity:
			newguy = organisms.NPC()
			randpick = random.randint(0,len(newguy.namedict.keys())-1)
			newguy.name = list(newguy.namedict.keys())[randpick]
			if newguy.name not in namelist:
				self.visiting.visitors.append(newguy)
				newguy.visitor = self.visiting
			namelist.append(newguy.name)
			randchoice = random.randint(0, len(newguy.elementslist)-1)
			newguy.element = newguy.elementslist[randchoice]
			randpref = random.randint(0, len(newguy.preflist)-1)
			newguy.likes = newguy.preflist[randpref]
			if newguy.element == self.visiting.element:
				newguy.comfort *= 2
			newguy.gold *= ((self.luck + self.intellect) // 2)
		self.visiting.peoplepresent = self.visiting.visitors + self.visiting.residents
			

	def genresidents(self):
		shortnames = []
		if self.visiting.visitors and len(self.visiting.residents) < self.visiting.rescapacity:
			for visitor in self.visiting.visitors:
				if self.visiting.menagerie:
					for org in self.visiting.menagerie:
						if visitor.likes == org.type:
							visitor.comfort *= 2
			print("\n### RESIDENT UPDATE ###")
			converted = 0
			for visitor in self.visiting.visitors:	
				if (visitor.comfort >= self.visiting.resthreshold) and visitor.name not in shortnames:
					self.visiting.residents.append(visitor)
					shortnames.append(visitor.name)
					print("{0} has decided to become a resident!".format(visitor.name.title()))
					input("")
					converted += 1
			if converted == 0:
				print("######################################################################")
				print("No one moved in to your settlement, today.")
				input("")
				print("######################################################################")
			print("")
			print("\n### END OF RESIDENT UPDATE ###\n")
		elif len(self.visiting.residents) == self.visiting.rescapacity:
			print("Your {0} is currently full on residents!  Upgrade it if you want more people running around!".format(self.visiting.type))


	def meetresidents(self):
		if self.visiting.residents:
			for resident in self.visiting.residents:
				print("\t" + resident.name.title())
				if resident.likes != "Pokemon" or "Fish":
					print("\t" + "Likes: " + resident.likes.title() + "s")
				else:
					print("\t" + "Likes: " + resident.likes.title())
				print("\t" + "Element: " + resident.element.title())
				print("")
		else:
			print("######################################################################")
			print("{0} currently has no residents.".format(self.visiting.name.title()))
			print("######################################################################")

	def greetvisitors(self):
		if self.visiting.visitors:
			for visitor in self.visiting.visitors:
				print("\t" + visitor.name.title())
				print("\t" + "Element: " + visitor.element.title())
				print("")
		else:
			print("######################################################################")
			print("{0} currently has no visitors.".format(self.visiting.name.title()))
			print("######################################################################")

	def checkweather(self):
		print("######################################################################")
		print("{0} is currently {1}!".format(self.visiting.name.title(), self.visiting.weather))
		input("")
		print("######################################################################")

	def scavenge(self):
		scavroll = random.randint(0,len(organisms.masteritems) - 1) 
		youfound = organisms.masteritems[scavroll]()

		if self.visiting and self.scavenged == False:
			if youfound.rarity <= self.luck:
				print("You go looking around {0} and find {1}!".format(self.visiting.name, youfound.name))
				input("")
				self.inventory.append(youfound)
				self.scavenged = True
				print("######################################################################")
			else:
				print("You didn't find anything...")
				self.scavenged = True
				print("######################################################################")
		else:
			print("You've already scavenged on this visit and didn't find anything.")
			print("######################################################################")

	def visitsettlement(self):
		self.brokenloop = False
		choices = {
		"scavenge [1]" : self.scavenge,
		"open a shop [2]" : self.openshop,
		"check on shop [3]" : self.pickshop,
		"open a menagerie [4]" : self.genmenagerie,
		"visit menagerie [5]" : self.visitmenagerie,
		"open sanctuary [6]" : self.opensanctuary,
		"visit sanctuary [7]" : self.visitsanctuary,
		"meet residents [8]" : self.meetresidents,
		"greet visitors [9]" : self.greetvisitors,
		"check weather [10]" : self.checkweather, 
		"go back (leave settlement) [0]" : self.goback
		}

		if self.settlements:
			self.correctstr = False
			while self.brokenloop == False:
				print("### VISIT SETTLEMENTS ###")
				print("######################################################################")
				for settlement in self.settlements:
					print("\t" + settlement.name.title())
				print("")
				print("######################################################################")
				print("Which settlement would you like to visit? (or 'go back')")
				print("######################################################################")
				usrinput = input("")
				if usrinput.lower() in "go back" or usrinput.lower() == "go back":
					self.goback()
					return
				if usrinput != "":
					wham = False
					for settlement in self.settlements:
						if usrinput.lower() in settlement.name.lower() or (usrinput.lower() == settlement.name.lower()):
							settlement.visit(self)
							wham = True
							self.genvisitors()
							print("Current Visitors:")
							for visitor in self.visiting.visitors:
								print(visitor.name.title())
								print("Element: " + visitor.element.title() + "\n")
							print("######################################################################")
					if wham == False:
							print("Ooops--I don't think you have a settlement by that name.  Try again.")
						
					while self.brokenloop == False:
						print("\n")
						print("######################################################################")
						print("### VISITING {0} ###".format(self.visiting.name.upper()))
						print("######################################################################")
						print("\n")
						for choice in choices.keys():
							print(choice.title())
						print("######################################################################")
						print("What would you like to do while in {0}?".format(self.visiting.name))
						print("######################################################################")
						newinput = input("")
						if newinput:
							for choice in choices:
								if newinput.lower() in choice.lower():
									if "go back" in choice:
										print("######################################################################")
										print("Are you sure you want to leave {0}?".format(self.visiting.name))
										lastcall = input("")
										if "y" in lastcall:
											self.genresidents()
											choices[choice]()
											self.correctstr = True
										else:
											print("Ok--sticking around a little longer.")
											print("######################################################################")
											self.correctstr = True
									else:
										choices[choice]()
										self.correctstr = True
										break
							if self.correctstr == False:
								print("I didn't get that--try again!")
						else:
							print("Whoops--enter an option!")
					else:
						self.brokenloop = False
				else:
					print("I didn't get that settlement name--try again!")
		
		else:
			print("You haven't founded any settlements, yet!")



	def gameexpdump(self):
		# Checks to see whether or not you've earned more than ten exp points in game, and if you have, distributes them across types of exp
		if self.expdict["game"] >= 10:
			for exptype in self.expdict.keys():
				if exptype != "game":
					self.expdict[exptype] += 1
			self.expdict["game"] -= 10

	def checklog(self):
		print("\n ### NATURE LOG ### ")
		if self.naturelog:
			for element in self.naturelog:
				print("Shuffled-name: " + "\t" + element.name)
				print("Type: " + element.type + "\n")
			print("\n")
		else:
			print("Your nature log is empty--go find something!")
			input("")
		print("######################################################################")
	
	def checkHP(self):
		print("\n ### HP ### ")
		print("\nYour HP: " + str(self.stats["HP"]))
		if self.companion:
			print("{0}'s HP: ".format(self.companion.name.title()) + str(self.companion.stats["HP"]))
		if self.target:
			print("{0}'s' HP: ".format(self.target.name.title()) + str(self.target.stats["HP"]))
		print("######################################################################")

	def checkstats(self):
		print("\n ### CHECK STATS ### ")
		print("These are your current stats: ")
		for stat in self.stats.keys():
			print(stat+": " + str(self.stats[stat]))
		print("######################################################################")


	def companionattack(self):
		if self.companion and self.companion.stats["HP"] > 0:
			self.companion.orgattack(self.target)
			if self.companion.stats["HP"] > 0 :
				self.tempenemy = self.companion

	def encounter(self):
		self.safe = False
		self.target.safe = False
		self.target.stats["HP"] = self.target.stats["Max HP"]
		self.tempenemy = self
		# Actions the player can take
		encoptions = {
		"attack" : self.attack,
		"flee" : self.flee,
		"befriend" : self.befriend
		#"capture it" : self.capture
		}
		if self.companion:
			encoptions["companion attack"] = self.companionattack

		# Actions the enemy can take

		self.playsound()
		while (self.safe == False) and (self.stats["HP"] > 0) and (self.target.safe == False) and (self.target.stats["HP"] > 0):
			self.checkHP()
			print("######################################################################")
			
			print("You're facing-off against a {1} {0}!  What do you want to do?".format(self.target.species, self.target.sex))
			print("You can: ")
			for option in encoptions.keys():
				print(option.title())
			print("######################################################################")
			userinput = input("")
			choice = ""
			proceed = False
			for key in encoptions.keys():
				if userinput in key and userinput != "":
					choice = key
					encoptions[choice]()
					proceed = True
					print("######################################################################")
					break
			if proceed == False:
				print("Your command wasn't clear--try typing it again!")
			elif choice == "check health":
				pass
			elif self.safe == False:
				if self.companion and self.companion.stats["HP"] < 1:
					print("{0} has collapsed!  {1} turns its attention back to {2}!".format(self.companion.name, self.target.species, self.name))
					self.tempenemy = self	
				self.target.orgchoose(self.tempenemy)
		if self.stats["HP"] < 1:
			print("You were driven off!")
			self.restoreHP()
		elif self.target.stats["HP"] < 1:
			print("You drove the {0} off!".format(self.target.name))
			self.tempenemy = self
			self.target.orgdrop(self)
			self.restoreHP()
			self.expdict["game"] += self.target.stats["Exp"]
			print("You've gained {0} exp!".format(self.target.stats["Exp"]))
			print("You've earned {0} gold!".format(self.target.stats["Gold"]))
			self.gold += self.target.stats["Gold"]
			if self.companion:
				companionexp = self.target.stats["Exp"] // 2
				print("{0} has gained {1} exp!".format(self.companion.name, companionexp))
				self.companion.expgained += companionexp
			self.previoustarget = self.target
			self.target = ""
		self.gameexpdump()
		if self.companion:
			self.companion.evolvecheck()
		self.restoreHP()



	# Allows you to engage with your current environment in different ways!
	def explorecurrent(self):
		self.brokenloop = False
		if self.currentenv:
			while self.brokenloop == False:
				print("You're currently in {0}.  What would you like to do?  You can: ".format(self.currentenv.name))
				print("\n")
				for choice in self.envoptions.keys():
					print("\t" + choice.capitalize())
				print("######################################################################")
				userinput = input("")
				goahead = False
				for choice in self.envoptions.keys():
					if userinput in choice and userinput != "":
						goahead = True
				if "go back" in userinput.lower():
					self.brokenloop == True
					break
				if goahead == True:
					for choice in self.envoptions.keys():
						if userinput in choice:
							self.envoptions[choice]()
							break
				else:
					print("I didn't get that--try writing the choice exactly as it appears!")

				

		else:
			print("Ooops--you haven't chosen an environment to start with, yet!  Better go back and pick a new one, first.")
			input("")

	# Examine bestiary
	def examinebestiary(self):
		print("\n ### EXAMINE BESTIARY ### ")
		self.excludestats = ["Max HP", "Gold", "Exp"]
		if self.bestiary:
			for org in self.bestiary:
				print("\t" + "Name: " + org.name.title())
				print("\t" + "Species: " + org.species.title())
				print("\t" + "Type: " + org.type.title())
				print("\t" + "Sex: " + str(org.sex).title())
				for stat in org.stats.keys():
					if stat not in self.excludestats:
						print("\t\t" + stat + " " + str(org.stats[stat]))
				print("\n")
		else:
			print("You don't have anything in your bestiary, yet--go out and explore!")
		print("######################################################################")

	def examinecompanion(self):
		print("\n ### EXAMINE COMPANION ### ")
		if not self.companion:

			print("You don't have a companion to examine right now!")
			print("######################################################################")
			return
		print("\t" + "Name: " + self.companion.name.title())
		print("\t" + "Species: " + self.companion.species.title())
		print("\t" + "Type: " + self.companion.type.title())
		print("\t" + "Sex: " + str(self.companion.sex).title())
		for stat in self.companion.stats.keys():
			if stat not in self.excludestats:
				print("\t\t" + stat + " " + str(self.companion.stats[stat]))
		print("\n")
		print("######################################################################")
		input("")

	# Go exploring in the world!
	def explorenew(self):
		print("\n ### EXPLORE A NEW ENVIRONMENT ### ")
		print("######################################################################")
		while self.currentenv:
			print("Are you sure you want to leave {0}?".format(self.currentenv.name))
			userinput = input("")
			if "y" in userinput:
				break
			elif "n":
				return
			else:
				print("I didn't get that--try again!")
		
		if self.mode == "organism":
			envlist = self.orgenvlist
		elif self.mode == "rpg":
			envlist = self.rpgenvlist
		
		for env in envlist.keys():
			print(env.title())
		print("######################################################################")
		self.currentenv = ""
		print("Great!  Where would you like to go? It can be anywhere listed above!")
		print("######################################################################")
		while True:
			userinput = input("")
			if userinput.lower() in envlist.keys():
				for env in envlist.keys():
					if userinput.lower() in env.lower() and userinput != "":
						self.currentenv = envlist[env]()
				break
			else:
				print("I didn't get that--could you try again?")
		
		if self.mode == "organism":
			currentlist = self.currentenv.genorgs(self)
		elif self.mode == "rpg":
			currentlist = [value() for value in self.currentenv.creaturedict.values()]
			for org in currentlist:
				org.name = org.name.title()
		self.currentenv.occupants = self.currentenv.assignstats(currentlist)
		creatures.gensex(self.currentenv.occupants)
		print("######################################################################")



		print("######################################################################")
		print("It looks like you've made it to {0}!".format(self.currentenv.name))
		if self.currentenv:
			if self.currentenv.song:
				self.playmusic(self.currentenv.song)
		self.explorecurrent()



	def flee(self):
		print("You attempt to flee from the {0}!".format(self.target.name))
		luckrand = random.randint(1, self.luck)
		enemyrand = random.randint(1, self.target.stats["Luck"])
		if luckrand > enemyrand:
			print("You got away safely!")
			self.safe = True
		else:
			print("You weren't able to escape!")

		

	# General error message
	def fourohfour(self):
		print("Ooops!  That's not working yet!")

	def feedcompanion(self):
		print("\n ### FEED YOUR COMPANION ### ")
		if self.inventory:
			if self.companion:
				print("What would you like to feed your companion?")
				for element in self.inventory:
					print(element.name.capitalize())
				userinput = input("")
				for element in self.inventory:
					if userinput == element.name:
						print("######################################################################")
						print("You fed {0} {1}!".format(self.companion.name, element.name))
						print("{0}'s {1} went up by {2}!".format(self.companion.name, element.affects, element.quality))
						self.companion.stats[element.affects] += element.quality
						self.inventory.pop(self.inventory.index(element))
						print("######################################################################")
						print('\n')
						input("")
						return
				print("######################################################################")
			else:
				print("You don't have a companion to feed!")
				print("######################################################################")
		else:
			print("You don't have anything to feed your companion!")
			print("######################################################################")
		input("")


	# Main method for gaining experience in the game; varies (or will vary) between flexible and fixed modes
	def getactivities(self):
		def fixedactivities(self):
			print("### FIXED MODE ###")
			fullbreak = False
			activitygiven = False
			while True:
				activitycomplete = False
				print("######################################################################")
				greeting = print("What did you do, today? (You can also type 'list' to see the activities available or type 'leave' to move on or 'quit' (to end game)!")
				activity = input("")
				if activity:
					activitygiven = True
				if "quit" in activity:
					self.quitsave()
				if "leave" in activity:
					break
				count = 0
				

				if "list" in activity.lower():
					for category in self.activitydict.keys():
						print(category.capitalize())
						for action in self.activitydict[category].keys():
							print("\t"+action.capitalize()+":"+" " +str(self.activitydict[category][action]))


				# Determines whether or not the activity has been done before
				if activitygiven and activity != "list":
					for category in self.activitydict.keys():
						if activity.lower() in self.activitydict[category]:
							count += 1
							print("######################################################################")
							print("Got it!")
							current = self.activitydict[category][activity]
							print("You've added {0} experience points to {1}!".format(current, category))
							self.expdict[category] += current
							activitycomplete = True
							break
					if activitycomplete == False and "list" not in activity:
						print("######################################################################")
						print("It doesn't look like that one's on the list--try typing it again (exactly as written).")
						print("If you'd prefer to customize your experience more, you can always start a game in 'flex' mode!)")
						print("(Press any key to continue)")
						input("")

				
				if activitycomplete == True:
					print("One more activity?")
					endinput = input("")
					if "quit" in endinput:
						self.quitsave()
				
					if ("n" in endinput and (len(endinput) < 2)) or ("no" in endinput):
						fullbreak = True

						# Prompts user to save the game
						self.save()
						break
					
					# Returns to original question about activities (what did you do, today?)
					else:
						pass

				if fullbreak == True:
					break


		def flexactivities(self):
			print("### FLEX MODE ###")
			fullbreak = False
			while True:
				greeting = print("What did you do, today? (you can also type 'list' (to see previous activities), 'leave' (move on), or 'quit')")
				activity = input("")
				activity = activity.lower()
				activitygiven = False
				if len(activity) > 0:
					activitygiven = True
				if "quit" in activity:
					self.quitsave()
				elif "leave" in activity:
					break
				count = 0
				
				if "list" in activity.lower():
					for category in self.activitydict.keys():
						print(category.capitalize())
						for action in self.activitydict[category].keys():
							print("\t"+action.capitalize()+":"+" " +str(self.activitydict[category][action]))
				# Determines whether or not the activity has been done before
				if (("list" not in activity.lower()) or ("list" != activity.lower())) and (activitygiven == True):
					while True:
						for category in self.activitydict.keys():
							if activity.lower() in self.activitydict[category]:
								count += 1
								print("You've done that one before!")
								current = self.activitydict[category][activity.lower()]
								print("You've added {0} experience points to {1}!".format(current, category))
								self.expdict[category] += current
								break
						
						# Indicates that the activity hasn't been done before
						if count == 0:
							# Assigns a quantity of experience points to your activity
							goodexp = False
							print("That's a new one--how many experience points is it worth?  (Give a number between 1 and 50!)")
							while goodexp == False:
								while True:
									activityexp = input("")
									try:
										activityexpint = int(activityexp)
										break
									except ValueError:
										print("Could not convert data to an integer--give a number between 1 and 50.")
								if (activityexpint > 50) | (activityexpint < 1):
									print("Ooops--that number won't work!  Choose an amount of exp between 1 and 50.")
								else:
									goodexp = True
							while True:
								for category in self.expdict.keys():
									if category.lower() != "game":
										print(category.title())
								print("To which category should I assign that?  You can assign it to any of the above categories:\n")
								catchoice = input("")
								catchoice = catchoice.lower()
								if catchoice in self.expdict.keys():
									self.expdict[catchoice] += activityexpint
									print("{0} exp added to {1}!".format(activityexpint, catchoice))
									self.activitydict[catchoice][activity.lower()] = activityexpint
									break
								else:
									print("Ooops--that one didn't register.  Try entering it again!")
							
							while goodexp == False:
								activityexp = input("")

							self.activitydict[catchoice.lower()][activity] = activityexpint
							
						print("One more activity?")
						endinput = input("")
						if "quit" in endinput:
							self.quitsave()
					
						if ("n" in endinput and (len(endinput) < 2)) or ("no" in endinput):
							fullbreak = True

							# Prompts user to save the game
							self.save()

							break
						
						# Returns to original question about activities (what did you do, today?)
						else:
							break

				if fullbreak == True:
					break
		if self.fixed == True:
			fixedactivities(self)
			self.actexpdump()
		elif self.fixed == False:
			flexactivities(self)
			self.actexpdump()


	def currentday(self):
		date = time.ctime().split(":")[0].split()[0:3]
		year = time.ctime().split(":")[2].split()[1]
		date.append(year)
		return date

	def goback(self):
		self.brokenloop = True
		self.scavenged = False
		self.switch = True

	def look(self):
		print("\n ### GO LOOKING FOR THINGS (REASONABLE) ### ")
		print("You go looking for things in a reasonable way.")
		if not self.currentenv.occupants:
			print("######################################################################")
			print("There's nothing here...try another environment!")
			print("######################################################################")
			return

		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		def makelooknum(self):
			self.looknum = random.randint(1,self.luck)
		self.target = ""
		chosen = False
		possible = False
		print("You advance into {0}!".format(self.currentenv.name))
		input("(Press any key to find out what you've encountered!)")
		makelooknum(self)
		makerandom(self)
		occupant = self.currentenv.occupants[self.randomnum]
		self.target = occupant
		# Checks to see if the player is eligible to have organisms approach
	
		print("You found a {0} ({1})!".format(self.target.name, self.target.type))
		self.addtolog()
		self.encounter()

	def playmusic(self, song):
		if self.musicon:
			pygame.mixer.music.fadeout(5000)
			pygame.mixer.music.stop()
			pygame.mixer.music.load(song)
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play(-1)
			#time.sleep(1)
			#pygame.mixer.music.set_volume(0.2)
			#time.sleep(1)
			#pygame.mixer.music.set_volume(0.3)
			#time.sleep(1)
			#pygame.mixer.music.set_volume(0.5)
			#time.sleep(1)
			#pygame.mixer.music.set_volume(0.8)
			#time.sleep(1)
			#pygame.mixer.music.set_volume(1)
			

	def playsound(self):
		sound = "a"
		if self.soundon:
			if self.target.sound:
				pygame.mixer.init()
				sound = pygame.mixer.Sound(self.target.sound)
				pygame.mixer.Channel(0).play(sound)
				time.sleep(2)
				pygame.mixer.Channel(0).stop()

	def passit(self):
		pass
# Used to print out all animals and their shuffled names for debugging use
	def printanimals(self):
		for animal in self.popmaster:
			print("Current Name:" + animal.name + "\n", "True Name: " + animal.truename + "\n", "Mega-Shuffled Name: " + animal.meganame + "\n","Inter-Shuffled Name: " + animal.intername + "\n", "Type: " + animal.type + "\n")
			for stat in animal.stats.keys():
				print("\t"+stat+":"+ " " + str(animal.stats[stat]))

# Used to strictly save the game (without quitting)
	def save(self, namedfile="newgame1"):
		print("\n ### SAVE GAME ### ")
		save = input("Save game? (y/n)\n")
		if "y" in save:
			while True:
				print("Choose a filename! (Default is '{0}') ".format(namedfile))
				userinput = input("")
				if 'leave' in userinput:
					print("Game not saved!")
					print("######################################################################")
					return
				if not userinput:
					outdir = os.path.join(os.path.curdir, "Saves")
					if not os.path.exists(outdir):
						os.mkdir(outdir)
					# os.makedirs("my_folder1")
					path = "Saves/"
					filelist = []
					if os.path.exists(path):
						for item in os.listdir(path):
								if item.endswith(".pickle"):
									filelist.append(item[:-7])
					userinput = "newgame1"
					if userinput in filelist:
						print("{0} already exists--are you sure you want to overwrite it?".format(userinput))
						newinput = input("")
						if "y" in newinput:
							# os.makedirs("my_folder1")
							path = os.path.join(outdir, namedfile+".pickle")
							with open(path, 'wb') as handle:
								pickle.dump(self, handle)
								print("Game Saved to default!")
								print("######################################################################")
								return
						else:
							print("Phew--dodged a bullet.  Try another filename (or 'leave')!")
	
				elif userinput:
					outdir = os.path.join(os.path.curdir, "Saves")
					if not os.path.exists(outdir):
						os.mkdir(outdir)
					path = "Saves/"
					filelist = []
					if os.path.exists(path):
						for item in os.listdir(path):
								if item.endswith(".pickle"):
									filelist.append(item[:-7])
					if userinput in filelist:
						print("{0} already exists--are you sure you want to overwrite it?".format(userinput))
						newinput = input("")
						if "y" in newinput:
							# os.makedirs("my_folder1")
							path = os.path.join(outdir, userinput+".pickle")
							with open(path, 'wb') as handle:
								pickle.dump(self, handle)
								print("Game Saved!")
								return
						else:
							print("Phew--dodged a bullet.  Try another filename!")
					else:
						path = os.path.join(outdir, userinput+".pickle")
						with open(path, 'wb') as handle:
							pickle.dump(self, handle)
							print("Game Saved!")
							print("######################################################################")
							return
		else:
			print("Game not saved!")
		print("######################################################################")

	def renamecompanion(self):
		if self.companion:
			oldname = self.companion.name
			while True:
				print("Would you like to rename your companion?")
				userinput = input("")
				if "y" in userinput:
					print("What would you like to rename {0}?".format(self.companion.pronoun))
					newname = input("")
					self.companion.name = newname.title()
					print("OK--you've renamed {0} {1}!".format(oldname, self.companion.name))
					break
				elif "n" in userinput:
					print("Ok--no renaming for now!")
					break
				else:
					print("I didn't get that--type 'yes' or 'no'!")


	def setcompanion(self):
		print("\n ### SET YOUR COMPANION ### ")
		i = 0
		self.excludestats = ["Gold", "Exp", "Max HP"]
		if self.bestiary:
			for org in self.bestiary:
				org.index = i
				print("\tName: " + org.name.title())
				print("\tType: " + org.type.title())
				print("\tBestiary Index:" + str(org.index))
				for stat in org.stats.keys():
					if stat not in self.excludestats:
						print("\t\t" + stat + ": " + str(org.stats[stat]))
				print("\n")
				i += 1
			print("######################################################################")
			print("You can currently have one companion traveling alongside you--who would you like it to be?")
			print("(Type the index number!")
			userinput = input("")
			if str.isdigit(userinput):
				for org in self.bestiary:
					if userinput == (str(org.index) or org.name):
						self.formercompanion = self.companion
						self.companion = org
						self.bestiary.pop(self.bestiary.index(self.companion))
						break
				if self.companion != self.formercompanion and self.formercompanion:
					print("Your new companion is {0} ({2}), and {1} ({3}) has gone back into the bestiary!".format(self.companion.name, self.formercompanion.name, self.companion.type, self.formercompanion.type))
					print("######################################################################")
					input("")
					self.bestiary.append(self.formercompanion)
				elif (self.companion == self.formercompanion):
					print("You've decided to keep traveling with {0} for a while.".format(self.companion.name))
				else:
					print("You've chosen to travel with {0} (a {1})!".format(self.companion.name, self.companion.type))
			else:
				print("Ooops--type the index (a number)!")


		else:
			print("You don't have anyone in the bestiary to choose from...yet.")
		print("######################################################################")

	def sit(self):
		print("\n ### SIT AND WAIT ### ")
		if not self.currentenv.occupants:
			print("There's nothing here...try another environment!")
			input("")
			return
		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		def makesitnum(self):
			self.sitnum = random.randint(1,self.luck*2)
		self.target = ""
		chosen = False
		possible = False
		print("\tYou sit and wait for something to approach you.")
		input("(Press any key to find out if something comes near!)")
		makesitnum(self)
		makerandom(self)
		occupant = self.currentenv.occupants[self.randomnum]

		# Checks to see if the player is eligible to have organisms approach
		if (self.stats["Luck"]*2) > self.currentenv.difficulty:
			possible = True

		if possible == True:
			if (occupant.stats["Skittishness"] > self.sitnum):
				chosen = False
			elif (occupant.stats["Skittishness"] < self.sitnum):
				chosen = True
			if chosen == True:
				self.target = occupant
				### ADD THIS IN TO THE ENCOUNTER WITH THE ORGANISM BECAUSE IT WAS ENCOUNTERED SITTING ###

				#for stat in occupant.stats:
				#	occupant.stats[stat] = occupant.stats[stat]//2
				print("\tA wild {0} (a {1}) cautiously appears--it looks like a {2}!".format(self.target.name, self.target.type, self.target.sex))
				self.addtolog()
				self.sat = True
				self.encounter()
			elif chosen == False:
				print("\t...nothing approached you.  Looks like you'll have to try again (or you can increase your luck to improve the chances of something approaching!).")
				print("######################################################################")
				print("(Press any key to continue)")
				input("")
		else:
			print("######################################################################")
			print("\tIt looks like you might need to level-up your \"luck\" stat before anything will approach you in this area!")

	def toggleflex(self):
		if self.fixed == True:
			print("\n ### FIXED MODE ### ")
			print("You're currently on fixed mode.")
			print("Would you like to switch to flex mode?")
			userinput = input("")
			if "y" in userinput:
				print("Ok!  Switched to flex mode!")
				self.fixed = False
				self.setactivitydict()
			else:
				print("Didn't switch modes--still in fixed.")
				return
		elif self.fixed == False:
			print("\n ### FLEX MODE ### ")
			print("You're currently on flex mode.")
			print("Would you like to switch to fixed mode?")
			userinput = input("")
			if "y" in userinput:
				print("If you switch to fixed mode, your existing library of activities will be lost.  Are you sure you want to switch?")
				userinput2 = input("")
				if "y" in userinput2:
					print("Switched from flex to fixed!")
					self.fixed = True
					self.setactivitydict()
		print("######################################################################")


	def togglesound(self):
		print("\n ### TOGGLE SOUND ### ")
		while True:
			print("Would you like sounds on or off?")
			userinput = input("")
			if "f" in userinput:
				self.soundon = False
				print("Sound off!")
				print("######################################################################")
				return
			elif "n" in userinput:
				self.soundon = True
				print("Sound on!")
				print("######################################################################")
				return
			else:
				print("I didn't get that--try again!")
		print("######################################################################")

	def togglemusic(self):
		print("\n ### TOGGLE MUSIC ### ")
		while True:
			print("Would you like music on or off?")
			userinput = input("")
			if "f" in userinput:
				self.musicon = False
				pygame.mixer.music.stop()
				print("Music off!")
				print("######################################################################")
				return
			elif "n" in userinput:
				self.musicon = True
				pygame.mixer.init()
				print("Music on!")
				print("######################################################################")
				return
			else:
				print("I didn't get that--try again!")
		print("######################################################################")

	def restcompanion(self):
		print("\n ### REST YOUR COMPANION ### ")
		if self.companion:
			print("Would you like to rest your companion?  It'll rest for at least one day, but it'll get stronger for every day it rests!")
			userinput = input("")
			if "y" in userinput:
				print("Are you sure?  {0} will be unavailable until tomorrow!".format(self.companion.name))
				userinput2 = input("")
				if "y" in userinput2:
					newguest = self.companion
					self.hotel.append(newguest)
					newguest.beganrest = self.currenttime()
					self.companion = ""
					newguest.resting = True
					print("Ok!  {0} is now resting!".format(newguest.name))
			else:
				print("Ok--no problem.  Another time.")
				input("")
		else:
			print("You don't have a companion to rest right now.")
			input("")
		print("######################################################################")

	def checkresting(self):
		print("\n ### CHECK RESTING ORGANISMS ### ")
		timenow = self.currenttime()
		potential = 0
		print(timenow)
		if self.hotel:
			print("These organisms are currently resting:")
			for org in self.hotel:
				print("\t" + org.name)
				print(org.beganrest)
				print(self.seconds_since(org.beganrest, timenow))
				if (self.seconds_since(org.beganrest, timenow)) >= 1:
					org.resting = False
		someready = False
		for org in self.hotel:
			if org.resting == False:
				someready = True
		if someready == True:
			i = 0
			print("The following organisms are ready for action again (but you can leave them if you want them to keep resting!)")
			for org in self.hotel:
				org.index = i
				if org.resting == False:
					print(org.name)
					print("Type: " + org.type)
					print("Index: " + str(org.index))
					print("Current stats: ")
					if timenow - org.beganrest:
						potential = (timenow - org.beganrest) // org.metric
					else:
						potential = "0"
					for stat in org.stats.keys():
						if stat not in self.excludestats:
							print("\t" + stat + " " + str(org.stats[stat]) + " (+ " + str(potential) + ")")
					print("If you withdraw {0} now, all its stats will be increased by {1}!".format(org.name, str(potential)))
					i += 1
					print("######################################################################")
			print("Who do you want to withdraw? (Type the organism's index or 'leave')")
			userinput3 = input("")
			if 'leave' in userinput3:
				print("Ok--you can check back later!")
				print("######################################################################")
				return
			for org in self.hotel:
				if userinput3 == str(org.index):
					print("You've withdrawn {0}!  It's back in the bestiary!".format(org.name))
					for stat in org.stats.keys():
						org.stats[stat] += potential
					self.bestiary.append(org)
					self.hotel.pop(self.hotel.index(org))
			print("######################################################################")

		else:
			print("No one's ready to wake up, yet--come back later!")
			print("######################################################################")
			input("")


	def restoreHP(self):
		self.stats["HP"] = self.stats["Max HP"]
		if self.companion:
			self.companion.stats["HP"] = self.companion.stats["Max HP"]



# Verifies that the user wants to quit and offers to save the game
	def quitsave(self, namedfile="newgame1"):
			print("\n ### QUIT GAME ### ")
			choice = input("Are you sure you want to quit? ")
			if "y" in choice:
				self.save(namedfile)
				print("Shutting it down!")
				quit()
			else:
				pass
			print("######################################################################")


	
### TO BE USED IN GAMEPLAY ###
popmain = Population()

### TO BE USED IN DEVELOPMENT ###
#debugpop = Population()
#debugpop.popmaster = organisms.dummypop



#startorgs = genorgs(startarea, poppop)

#bogorgs = genorgs(bog, poppop)

#newlist = assignstats(startarea, startorgs)

#biggerlist = assignstats(bog, bogorgs)


