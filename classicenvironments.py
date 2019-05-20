#!/usr/bin/env python3

import sys
import re
import pickle
import random
import creatures
#from gameclasses import popmain











class basicEnv(object):
	def __init__(self):
		self.name = "A basic environment"
		self.difficulty = 1
		self.animalnum = 10
		self.occupants = []
		self.hasaquatics = False
		self.song = "Music/Riding_Night.ogg"

	def genorgs(self, player):
		templist = []
		pickedlist = []
		newnum = 0
		# You'll want to use "choice" here from the builtin random module; choose(sequence) will pick something randomly from a list
		# This can be amended to operate within a range.
		for org in player.popmaster:
			if org.mobile == True:
				if (self.hasaquatics == False) and ((org.type == "Amphibian") or (org.type == "Fish")):
					pass
				else:
					templist.append(org)
		for i in range(self.animalnum):
			newchoice = random.choice(templist)
			newchoice.evthreshold1 *= player.currentenv.difficulty
			newchoice.evthreshold2 *= player.currentenv.difficulty
			pickedlist.append(newchoice)
				
		return pickedlist

	def assignstats(self, genlist):
		statorgs = []
		for org in genlist:
			if org not in statorgs:
				statorgs.append(org)
				for stat in org.stats.keys():
					org.stats[stat] = org.stats[stat] * (random.randint((self.difficulty-3 if (self.difficulty-2 > 0) else 1), self.difficulty))
			if org.power:
				org.poweron()
		return statorgs

class aquaEnv(basicEnv):
	def __init__(self):
		self.name = "a basic aquatic environment"
		self.difficulty = 1
		self.animalnum = 10
		self.hasaquatics = True


class Meadow(basicEnv):
	creaturedict = {
	"snail" : creatures.Snail,
	"tiny turtle" : creatures.tinyTurtle,
	"chick" : creatures.Chick,
	"duckling" : creatures.Duckling,
	"slug" : creatures.Slug,
	"spider" : creatures.Spider,
	"roach" : creatures.Roach,
	"frog" : creatures.Frog,
	"mouse" : creatures.Mouse,
	"salamander" : creatures.Salamander
	}

	def __init__(self):
		super().__init__()
		self.name = "an inviting meadow"


class Bog(aquaEnv):
	def __init__(self):
		super().__init__()
		self.animalnum = 15
		self.difficulty = 5
		self.name = "a bog"

class Swamp(aquaEnv):
	def __init__(self):
		super().__init__()
		self.animalnum = 20
		self.difficulty = 7
		self.name = "a swamp"

class Woods(basicEnv):
	def __init__(self):
		super().__init__()
		self.name = "a wooded expanse"
		self.difficulty = 10
		self.animalnum = 25

class Plain(basicEnv):
	def __init__(self):
		super().__init__()
		self.name = "rolling plains"
		self.difficulty = 12
		self.animalnum = 30

class darkForest(basicEnv):
	def __init__(self):
		super().__init__()
		self.name = "a dark and ominous forest"
		self.difficulty = 20
		self.animalnum = 40

### TYPES OF SANCTUARIES ###
class basicSanc(object):
	cost = 100
	def __init__(self):
		self.name = "basic sanctuary"
		self.type = "undefined type"
		self.animalnum = 10
		self.weather = ""
		self.residents = []


### TYPES OF SHOPS ###
class basicShop(basicEnv):
	cost = 50
	def __init__(self):
		super().__init__()
		self.element = ""
		self.shoppers = []
		self.name = ""
		self.cost = 50
		self.firstone = False
		self.mascot = ""
		self.forsale = []
		self.counterspace = 3
		self.earnings = 0
		self.sold = []


### VILLAGES, TOWNS, AND CITIES ###

class Village(basicEnv):
	cost = 100
	def __init__(self):
		super().__init__()
		self.weather = ""
		self.element = ""
		self.rescapacity = 5
		self.resthreshold = 50
		self.viscapacity = 10
		self.shopcost = 1000
		self.name = "A small village"
		self.cost = 100
		self.type = "village"
		self.sanctuary = ""
		self.upgrade = "town"
		self.upgrade2 = "city"
		self.visitors = []
		self.residents = []
		self.peoplepresent = []
		self.popularity = 1
		self.businesses = []

		self.menageriecost = 100
		self.menagerie = []
		self.menageriesize = 3
		self.menagerieopen = False

	def setweather(self):
		weatherdict = {
		"sunny" : "Fire",
		"cloudy" : "Air",
		"rainy" : "Water",
		"stormy" : "Water",
		"overcast" : "Air",
		"dry" : "Fire",
		"lush" : "Earth",
		"green" : "Earth"
		}

		weatherlist = []
		[weatherlist.append(weathertype) for weathertype in weatherdict.keys()]

		weatherroll = random.randint(0,len(weatherlist)-1)
		self.weather = weatherlist[weatherroll]
		self.element = weatherdict[self.weather]



	def visit(self, player):
		self.setweather()
		print("######################################################################")
		print("You've arrived in {0} {1}!".format(self.weather, self.name))
		print("######################################################################")
		print("(Press Enter to Continue)")
		input("")
		player.visiting = self




