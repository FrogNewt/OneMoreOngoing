#!/usr/bin/env python3


### TURN ALL BACK ON AFTER DEBUGGING ###
#import sys
import re
import random
#import pygame
#pygame.mixer.init()
#import pickle

from shufflecipher import megacipher, intercipher





#truemaster = set()
#typeslist = []




# produces a "set" to become the orglist that'll temporarily contain all organisms



# Opens the scientific names of organisms and reads them in with revisions to help with organization



### TURN BACK ON AFTER DEBUGGING ###
#openitup()
			

# Reads the fifth column in a tab-delimited line
#[print(line.split('\t')[5]) for line in truemaster]

# Class given to all objects to exist in the game.
class gameObject(object):
	def __init__(self):
		self.name = ""
		self.price = 1
		self.index = ""
		self.boughtby = ""

class Food(gameObject):
	def __init__(self):
		super().__init__()
		self.quality = 1
		self.rarity = 1

class hpFood(Food):
	def __init__(self):
		super().__init__()
		self.affects = "HP"
		self.name = "some grains"

class speedFood(Food):
	def __init__(self):
		super().__init__()
		self.affects = "Speed"
		self.name = "some fruit"

class strengthFood(Food):
	def __init__(self):
		super().__init__()
		self.affects = "Strength"
		self.name = "some meat"

class luckFood(Food):
	def __init__(self):
		super().__init__()
		self.affects = "Luck"
		self.name = "some eggs"

### TO BE USED IN SCAVENGING AND QUESTS--ADD TO THIS AS NEW ITEMS ARE ADDED ###
masteritems = [
hpFood,
speedFood,
strengthFood,
luckFood
]



#Class given to any living thing in the game; confers basic stats
class livingThing(gameObject):
	def __init__(self, name="Living Thing", HP = 0):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True
		self.listready = False
		self.truename = ""


# After livingThing, classes narrow into more specific groups that have unique traits, abilities, and roles in the game
class Organism(livingThing):
	def __init__(self):
		super().__init__()
		self.truename = ""
		self.type = ""
		self.listready = False
		self.type = "Creature"
		self.truetype = ""
		self.hasatype = False
		self.power = False
		self.berserk = False
		self.damage = 0
		self.sound = ""
		self.action = ""
		self.index = 0
		self.sex = ""
		self.damID = ""
		self.matedtime = ""
		self.sireID = ""
		self.babyID = ""
		self.resting = False
		self.expgained = 0
		self.evolved = 0

		# Combat Stats
		self.maxHP = 10
		self.HP = self.maxHP
		self.strength = 1
		self.speed = 1
		self.luck = 1
		self.skit = 1
		self.item = ""
		self.evolvable = True
		self.mobile = True
		self.gold = 1
		self.expgiven = 1
		self.beganrest = ""
		self.evthreshold1 = 100
		self.evthreshold2 = 200
		

		self.actions = [
		self.orgattack, 
		self.orgflee
		]


		# Organizes all combat stats into a list
		self.stats = {
		"HP" : self.HP,
		"Max HP" : self.maxHP,
		"Strength" : self.strength,
		"Speed" : self.speed,
		"Skittishness" : self.skit,
		"Luck" : self.luck,
		"Gold" : self.gold,
		"Exp" : self.expgiven
		}

	def orgattack(self, opponent):
		def setdamage(self):
			self.damage = random.randint(self.stats["Strength"], self.stats["Strength"] + self.stats["Luck"])
		setdamage(self)
		opponent.stats["HP"] -= self.damage
		print("{0} attacks {1} for {2} damage!".format(self.name, opponent.name, self.damage))

	def orgflee(self, opponent):
		print("The {0} attempts to flee from {1}!".format(self.name, opponent.name))
		luckrand = random.randint(1, self.stats["Luck"])
		enemyrand = random.randint(1, opponent.stats["Luck"])
		if luckrand > enemyrand:
			print("The {0} got away safely!".format(self.name))
			self.safe = True
		else:
			print("The {0} wasn't able to escape!".format(self.name))

	def orgchoose(self, opponent):
		randchoice = random.randint(0, 3+self.stats["Skittishness"])
		if randchoice <= 3:
			self.action = self.orgattack
		elif randchoice > 3:
			self.action = self.orgflee

		return self.action(opponent)

	def orgdrop(self, opponent):
		keepchance = random.randint(0, self.stats["Luck"])
		dropchance = random.randint(0, opponent.stats["Naturalism"])
		if keepchance > dropchance:
			pass
		elif dropchance > keepchance:
			print("{0} dropped {1}!".format(self.name, self.item.name))
			opponent.inventory.append(self.item)

	def evolvecheck(self):
		exclude = ["Gold", "Exp", "Skittishness"]
		def evolve1(self):
			print("{0} is evolving...into a {1}!".format(self.name, self.intername))
			self.name = self.intername
			self.evolved = 1
			for stat in self.stats.keys():
				if stat not in exclude:
					old = self.stats[stat]
					self.stats[stat] *= 2
					if stat != "HP":
						print(stat + " " + str(old) + "->" + str(self.stats[stat]))
		
		def evolve2(self):
			print("{0} is evolving...into a {1}!".format(self.name, self.truename))
			self.name = self.truename
			self.evolved = 2
			for stat in self.stats.keys():
				if stat not in exclude:
					old = self.stats[stat]
					self.stats[stat] *= 3
					if stat != "HP":
						print(stat + " " + str(old) + "->" + str(self.stats[stat]))
		
		if self.evolvable == True and self.evolved == 0:
			if self.expgained > self.evthreshold1:
				evolve1(self)
				self.expgained -= self.evthreshold1

		elif self.evolvable == True and self.evolved == 1:
			if self.expgained > self.evthreshold2:
				evolve2(self)
				self.expgained -= self.evthreshold2



	def genfood(self):
		fooddict = {
		0: hpFood,
		1: speedFood,
		2: strengthFood,
		3: luckFood
		}
		foodnum = random.randint(0,len(fooddict)-1)
		self.item = fooddict[foodnum]()



### TO BE USED IN PRODUCING ALL NON-PLAYER, HUMAN/HUMANOID CHARACTERS WHO CAN SPEAK TO/INTERACT WITH THE PLAYER ###
class NPC(Organism):
	def __init__(self):
		super().__init__()
		
		self.elementslist = ["fire", "water", "earth", "air"]

		self.preflist = [
			"Reptile",
			"Amphibian",
			"Fish",
			"Bird",
			"Roundworm",
			"Flatworm",
			"Dragon",
			"Monster",
			"Pokemon",
			"Insect"
			]

		self.namedict = {
		"jim" : "m",
		"jenny" : "f",
		"jamal" : "m",
		"jess" : "f",
		"echo" : "f",
		"rick" : "m",
		"mortimer" : "m",
		"jerry" : "m",
		"jocelyn" : "f",
		"eric" : "m",
		"horace" : "m",
		"malik" : "m",
		"leslie" : "f",
		"farrah" : "f",
		"sarah" : "f",
		"amanda" : "f",
		"courtney" : "f",
		"barbara" : "f"
		}
		
		self.sex = ""
		self.comfort = random.randint(0,50)
		self.aloofness = random.randint(0,100)
		self.gold = random.randint(0,100)
		self.name = "Stranger"
		self.merchant = 0
		self.targetitem = ""
		self.buyinterest = random.randint(0,100)
		self.likes = ""
		self.items = []
		self.hired = ""
		self.shopping = ""
		self.resident = ""
		self.visitor = ""
		self.element = ""

	def shop(self, player):
		# Check to see if this NPC is visiting the town the user is currently in
		if self.visitor == player.visiting:
			# If the visitor is in the town, checks to see if the user likes the mascot
			if player.patron.mascot:
				if self.likes == player.patron.mascot.type:
					self.comfort *= 2
			# Check to see whether or not the visitor chooses to shop
			if self.comfort > self.aloofness:
				self.shopping = player.patron
				player.patron.shoppers.append(self)
				self.buy(player)
			# Check to see if there are things to buy in the shop
			


	def buy(self, player):
		if (self.shopping == player.patron) and player.patron.forsale:
			choice = random.randint(0, len(player.patron.forsale)-1)
			self.targetitem = player.patron.forsale[choice]
			self.aloofness += (self.targetitem.price // 5)
			buyboost = random.randint(0, player.luck+player.intellect+(self.comfort // 2))
			if self.targetitem in player.patron.forsale:
				self.buyinterest += buyboost
				if self.buyinterest > self.aloofness:
					if self.targetitem.price < self.gold:
						self.targetitem.boughtby = self.name
						player.patron.sold.append(self.targetitem)
						player.patron.forsale.pop(player.patron.forsale.index(self.targetitem))
						self.gold -= self.targetitem.price
						player.patron.earnings += self.targetitem.price
						self.targetitem = ""
						player.patron.shoppers.pop(player.patron.shoppers.index((self)))
				elif self.buyinterest < self.aloofness:
					player.patron.shoppers.pop(player.patron.shoppers.index((self)))









class Reptile(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "ecto"
		self.type = "Reptile"
		self.power = True
		self.sound = "Sounds/Reptile.ogg"
	def poweron(self):
		self.stats["Strength"] = self.stats["Strength"] * 2
	def printdemo(self):
		print("Printing a demo")

class Amphibian(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "ecto"
		self.type = "Amphibian"
		self.power = True
		self.sound = "Sounds/Amphibian.ogg"
	def poweron(self):
		self.stats["Luck"] = self.stats["Luck"] * 2

class Bird(Organism):
	def __init__(self):
		super().__init__()
		self.sound = "Sounds/Bird.ogg"
		self.therm = "endo"
		self.type = "Bird"
	def poweron(self):
		self.stats["Speed"] = self.stats["Speed"] * 2

class Mammal(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "endo"
		self.power = ""
		self.type = "Mammal"
		self.sound = "Sounds/Mammal.ogg"
		self.power = True
	def poweron(self):
		self.stats["HP"] = self.stats["HP"] * 5
		self.stats["Max HP"] = self.stats["Max HP"] * 5

class Fungus(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Fungus"
		self.mobile = False

class Ascomycetes(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.mobile = False
		self.type = "Ascomycetes"

class Fish(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.sound = "Sounds/Fish.ogg"
		self.type = "Fish"

class Insect(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Insect"
		self.sound = "Sounds/Insect.ogg"
		self.power = True
	def poweron(self):
		self.stats["Skittishness"] = self.stats["Skittishness"] * 5
		self.stats["Gold"] = self.stats["Gold"] * 10
		self.stats["Luck"] = self.stats["Luck"] * 3

class Plant(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Plant"
		self.mobile = False

class Protist(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Protist"
		self.mobile = False

class Dragon(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Dragon"
		self.sound = "Sounds/Dragon.ogg"
		self.power = True
	def poweron(self):
		self.stats["Strength"] = self.stats["Strength"] * 10
		self.stats["HP"] = self.stats["HP"] * 10
		self.stats["Speed"] = self.stats["Speed"] * 10
		self.stats["Gold"] = self.stats["Gold"] * 100

class Kinetoplast(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Kinetoplast"
		self.mobile = False

class Basidiomycetes(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Basidiomycetes"
		self.mobile = False

class Apicomplexan(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Apicomplexan"
		self.mobile = False

class greenAlgae(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Green Alga"
		self.mobile = False

class Flatworm(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Flatworm"

class Roundworm(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Roundworm"

class Monster(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Monster"
		self.sound = "Sounds/Monster.ogg"

class Pokemon(Organism):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Pokemon"

# Populates master list of organisms to be used in the game; can be later sorted
def populatemaster(masterlist):
	poptotal = []
	i = 0
	for element in masterlist:
		organism = Organism()
		organism.name = element
		organism.truename = organism.name
		poptotal.append(organism)

	


	#[print(element.name) for element in popmaster]
	return poptotal


def shuffleboth(poplist):
	templist = []
	for org in poplist:
		megaorg = megacipher(org)
		interorg = intercipher(org)
		
	return poplist

def sortorglist(orglist):
	orglist = sorted(orglist)
	return orglist









### DUMMY LIST TO BE USED IN DEBUGGING; CAN BE SUBSTITUTED FOR LARGER DATASET ###
somereptile = Reptile()
somereptile.type = "Reptiles"
somereptile.name = "Some Reptile"

somefrog = Amphibian()
somefrog.type = "Amphibians"
somefrog.name = "Some frog"

somefungus = Fungus()
somefungus.type = "Fungi"
somefungus.name = "Some Fungus"

secondfrog = Amphibian()
secondfrog.type = "Amphibians"
secondfrog.name = "Second Frog"

thirdfrog = Amphibian()
thirdfrog.type = "Amphibians"
thirdfrog.name = "Third Frog"

secondfungus = Fungus()
secondfungus.type = "Fungi"
secondfungus.name = "Second Fungus"

dummypop = [somereptile, somefrog, somefungus, secondfrog, thirdfrog, secondfungus]






