#!/usr/bin/env python3

import sys
import os
import re
import pickle
import organisms
import random
from shufflecipher import *
from environments import *
import pygame
import time





def begingame():
	def start():
		#pygame.mixer.init()
		#pygame.mixer.music.load('woodfrog.wav')
		#pygame.mixer.music.play()

		print("Please hold--we're shuffling all your organisms into the game!\n")
		popmain.shufflebegin()
		newplayer = Player()
		print("Hey--what's your name?")
		userinput = input("")
		newplayer.name = userinput
		print("######################################################################")
		print("Hi {0}!".format(newplayer.name))
		newplayer.popmaster = popmain.popmaster
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
		soundready = False
		while soundready == False:
			print("One last thing--would you like to begin with sound 'on' or 'off'?")
			soundinput = input("")
			if "n" in soundinput:
				print("Sound on!")
				import pygame
				newplayer.soundon = True
				soundready = True
			elif "f" in soundinput:
				print("Sound off!")
				newplayer.soundon = False
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
		print("######################################################################")
		print("So, {0}, what would you like to do next?  You can choose from any of these (or 'quit'):\n".format(self.name))
		for key in self.optionlist.keys():
			print(key.title())
		print("")
		ready = False
		usrinput = input("")
		if 'quit' in usrinput:
			self.quitsave()
		for option in self.optionlist.keys():
			if (usrinput) and (usrinput.lower() in option) or (usrinput == option):
				print("######################################################################")
				print(option.title())
				print("######################################################################")
				while ready == False:
					for key in self.optionlist[option].keys():
						print(key.title())
					print("######################################################################")
					print("What would you like to do?")
					usrinput2 = input("")
					print("######################################################################")
					for key in self.optionlist[option].keys():
						if (usrinput2.lower() in key) or (usrinput2.lower() == key.lower()):
							if usrinput2 and ((usrinput2.lower() == "go back") or ("go back" in usrinput2)):
								ready = True
								break
							else:
								self.optionlist[option][key]()
								break
					
					
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
		self.name = "Population Master"
		self.popmaster = []
	def shufflebegin(self, poplist = ""):
		opened = organisms.openitup()
		self.popmaster = organisms.shuffleboth(organisms.givetype(organisms.scrapetypes(organisms.populatemaster(opened))))




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
		self.luck = 4
		self.fixed = True
		self.soundon = True

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
		"set companion" : self.setcompanion,
		"inspect companion" : self.examinecompanion,
		"feed companion" : self.feedcompanion,
		"rest companion" : self.restcompanion,
		"check resting organisms" : self.checkresting,
		"breed organisms" : self.breed,
		"view nursery" : self.checknursery,
		"bestiary" : self.examinebestiary,
		"go back" : self.goback

		}

		self.playerdict = {
		"add new activities" : self.getactivities,
		"check stats" : self.checkstats,
		"check inventory" : self.checkinventory,
		"check my exp" : self.checkexp,
		"check nature log" : self.checklog,
		"go back" : self.goback
		}

		self.exploredict = {
		"explore a new environment" : self.explorenew,
		"explore my current environment" : self.explorecurrent,
		"go back" : self.goback

		}

		self.settingsmenu = {
		"toggle flex" : self.toggleflex,
		"toggle sound" : self.togglesound,
		"save game" : self.save,
		"go back" : self.goback
		}

		# Creates list of all options for a player to choose
		self.optionlist = {
			#"add new activities" : self.getactivities,
			"explore the world" : self.exploredict,
			"player options" : self.playerdict,
			"care for your organisms" : self.orgsdict,
			
			"settings" : self.settingsmenu
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
		self.envlist = {
			"meadow" : Meadow,
			"bog" : Bog,
			"swamp" : Swamp,
			"woods" : Woods,
			"plains" : Plain,
			"dark forest" : darkForest
		}

	# Lists the options available to a player within a given environment
		self.envoptions = {
			"sit patiently and wait to be approached" : self.sit,
			"go out and carefully look for organisms" : self.look,
			"go bounding through the environment" : self.bound,
			"go back" : self.goback
		}

	# Stuff the player has
		self.inventory = []
		self.gold = 0
		self.equipment = []
		self.bestiary = []
		self.naturelog = []
		self.nursery = []
		self.companion = ""
		self.formercompanion = ""
	
	# Things the player may need to "hold" in order to advance the game
		self.randomnum = 0
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

	# For breeding organisms
		self.dam = ""
		self.sire = ""
	
	def addtolog(self):
		if self.target not in self.naturelog:
			print("######################################################################")
			print("{0} (a {1}) added to your nature log!".format(self.target.name, self.target.type))
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
						self.dam.matedtime = str(time.ctime())
						self.dam.matedtime = self.dam.matedtime.split()[3]
						self.dam.matedtime = self.dam.matedtime.split(":")[1]
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
			return
		print("######################################################################")
		
	# Splits ctime output to produce an element of the current time (e.g. day, month, hour, etc)
		checktime = str(time.ctime())
		checktime = checktime.split()[3]
		checktime = checktime.split(":")[1]
		
	# Checks to see if the baby is ready, yet
		if self.dam.matedtime != checktime:
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
			print("######################################################################")


	def actexpdump(self):
		for exptype in self.expdict.keys():
			while self.expdict[exptype] > 100:				
				for key in self.statexpdict.keys():
					if exptype.lower() in key.lower():
						self.stats[self.statexpdict[exptype]] += 1
						self.expdict[exptype] -= 100
				

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
			print("{0}'s HP: ".format(self.companion.name) + str(self.companion.stats["HP"]))
		if self.target:
			print("Opponent HP: " + str(self.target.stats["HP"]))
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
			
			print("You're facing-off against a {1} {0}!  What do you want to do?".format(self.target.name, self.target.sex))
			print("You can: ")
			for option in encoptions.keys():
				print(option.title())
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
					print("{0} has collapsed!  {1} turns its attention back to {2}!".format(self.companion.name, self.target.name, self.name))
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
				for choice in self.envoptions.keys():
					print("\t" + choice.capitalize())
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
				print("\t" + "Name: " + org.name)
				print("\t" + "Type: " + org.type)
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
		print("\t" + "Name: " + self.companion.name)
		print("\t" + "Type: " + self.companion.type)
		print("\t" + "Sex: " + str(self.companion.sex).title())
		for stat in self.companion.stats.keys():
			if stat not in self.excludestats:
				print("\t\t" + stat + " " + str(self.companion.stats[stat]))
		print("\n")
		print("######################################################################")

	# Go exploring in the world!
	def explorenew(self):
		print("\n ### EXPLORE A NEW ENVIRONMENT ### ")
		while self.currentenv:
			print("Are you sure you want to leave {0}?".format(self.currentenv.name))
			userinput = input("")
			if "y" in userinput:
				break
			elif "n":
				return
			else:
				print("I didn't get that--try again!")
		for env in self.envlist:
			print(env.title())
		self.currentenv = ""
		print("Great!  Where would you like to go? It can be anywhere listed above!")
		while True:
			userinput = input("")
			if userinput.lower() in self.envlist.keys():
				for env in self.envlist.keys():
					if (userinput.lower() in env.lower()) and userinput != "":
						self.currentenv = self.envlist[env]()
				break
			else:
				print("I didn't get that--could you try again?")
		
		currentlist = self.currentenv.genorgs(self)
		self.currentenv.occupants = self.currentenv.assignstats(currentlist)
		print("######################################################################")



		print("######################################################################")
		print("It looks like you've made it to {0}!".format(self.currentenv.name))
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
							print("You fed {0} {1}!".format(self.companion.name, element.name))
							print("{0}'s {1} went up by {2}!".format(self.companion.name, element.affects, element.quality))
							self.companion.stats[element.affects] += element.quality
							self.inventory.pop(self.inventory.index(element))
							print("######################################################################")
							print('\n')
							return
					print("######################################################################")
				else:
					print("You don't have a companion to feed!")
					print("######################################################################")
			else:
				print("You don't have anything to feed your companion!")
				print("######################################################################")


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


	def goback(self):
		self.brokenloop = True

	def look(self):
		print("\n ### GO LOOKING FOR THINGS (REASONABLE) ### ")
		print("You go looking for things in a reasonable way.")
		if not self.currentenv.occupants:
			print("There's nothing here...try another environment!")
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

	def playsound(self):
		sound = "a"
		if self.soundon:
			if self.target.sound:
				pygame.mixer.init()
				sound = pygame.mixer.Sound(self.target.sound)
				pygame.mixer.Channel(0).play(sound)
				time.sleep(2)
				pygame.mixer.Channel(0).stop()
				pygame.mixer.quit()

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

	def setcompanion(self):
		print("\n ### SET YOUR COMPANION ### ")
		i = 0
		self.excludestats = ["Gold", "Exp", "Max HP"]
		if self.bestiary:
			for org in self.bestiary:
				org.index = i
				print("\tName: " + org.name)
				print("\tType: " + org.type)
				print("\tBestiary Index:" + str(org.index))
				for stat in org.stats.keys():
					if stat not in self.excludestats:
						print("\t\t" + stat + ": " + str(org.stats[stat]))
				print("\n")
				i += 1
			print("######################################################################")
			print("You can currently have one companion traveling alongside you--who would you like it to be?")
			print("(You can either type the entire name or just the index number!")
			userinput = input("")
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
			print("You don't have anyone in the bestiary to choose from...yet.")
		print("######################################################################")

	def sit(self):
		print("\n ### SIT AND WAIT ### ")
		if not self.currentenv.occupants:
			print("There's nothing here...try another environment!")
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
					newguest.beganrest = str(time.ctime().split(" ")[3].split(":")[1])
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
		timenow = str(time.ctime().split(" ")[3].split(":")[1])
		if self.hotel:
			print("These organisms are currently resting:")
			for element in self.hotel:
				print("\t" + element.name)
				if element.beganrest != timenow:
					element.resting = False
		someready = False
		for org in self.hotel:
			if org.resting == False:
				someready = True
		if someready == True:
			i = 0
			print("The following organisms are ready for action again (but you can leave them if you want them to keep resting!)")
			for element in self.hotel:
				element.index = i
				if element.resting == False:
					print(element.name)
					print("Index: " + str(element.index))
					print("Current stats: ")
					if abs(int(timenow) - int(element.beganrest)):
						potential = abs(int(timenow) - int(element.beganrest))
					else:
						potential = "0"
					for stat in element.stats.keys():
						if stat not in self.excludestats:
							print("\t" + stat + " " + str(element.stats[stat]) + " (+ " + str(potential) + ")")
					print("If you withdraw {0} now, all its stats will be increased by {1}!".format(element.name, str(potential)))
					i += 1
					print("######################################################################")
			print("Who do you want to withdraw? (Type the organism's index or 'leave')")
			userinput3 = input("")
			if 'leave' in userinput3:
				print("Ok--you can check back later!")
				print("######################################################################")
				return
			for element in self.hotel:
				if userinput3 == str(element.index):
					print("You've withdrawn {0}!  It's back in the bestiary!".format(element.name))
					for stat in element.stats.keys():
						element.stats[stat] += abs(int(timenow) - int(element.beganrest))
					self.bestiary.append(element)
					self.hotel.pop(self.hotel.index(element))
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


	

popmain = Population()





#startorgs = genorgs(startarea, poppop)

#bogorgs = genorgs(bog, poppop)

#newlist = assignstats(startarea, startorgs)

#biggerlist = assignstats(bog, bogorgs)


