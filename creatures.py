#!/usr/bin/env python3


### TURN ALL BACK ON AFTER DEBUGGING ###
#import sys
import re
import random
#import pygame
#pygame.mixer.init()
#import pickle

from shufflecipher import megacipher, intercipher

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
		self.type = "Organism"
		self.truetype = ""
		self.hasatype = False
		self.power = False
		self.berserk = False
		self.damage = 0
		self.sound = ""
		self.action = ""
		self.metric = 60
		self.index = 0
		self.sex = ""
		self.damID = ""
		self.matedtime = ""
		self.sireID = ""
		self.babyID = ""
		self.pronoun = ""
		self.species = ""
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

def gensex(poplist):
	i = 0
	holderlist = []
	for org in poplist:
		holderlist.append(org)
		holderlist[i].sex = random.randint(0,1)
		holderlist[i].genfood()
		if holderlist[i].sex == 1:
			holderlist[i].sex = "male"
			holderlist[i].pronoun = "him"
		elif holderlist[i].sex == 0:
			holderlist[i].sex = "female"
			holderlist[i].pronoun = "her"
		holderlist[i].species = holderlist[i].name
				#print(holderlist[i], holderlist[i].type)
		i+=1



class tinyTurtle(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 2
		self.strength = 1
		self.skittishness = 1
		self.luck = 1
		self.type = "reptile"
		self.name = "tiny turtle"

class Snail(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 1
		self.strength = 1
		self.skittishness = 1
		self.luck = 1
		self.type = "gastropod"
		self.name = "snail"

class Chick(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 1
		self.strength = 1
		self.skittishness = 1
		self.luck = 1
		self.type = "bird"
		self.name = "chick"

class Duckling(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 2
		self.strength = 1
		self.skittishness = 1
		self.luck = 1
		self.type = "bird"
		self.name = "duckling"

class Slug(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 2
		self.strength = 2
		self.skittishness = 1
		self.luck = 1
		self.type = "gastropod"
		self.name = "slug"

class Spider(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 2
		self.strength = 3
		self.skittishness = 2
		self.luck = 1
		self.type = "arachnid"
		self.name = "spider"

class Roach(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 3
		self.strength = 2
		self.skittishness = 2
		self.luck = 1
		self.type = "insect"
		self.name = "roach"

class Frog(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 4
		self.strength = 2
		self.skittishness = 2
		self.luck = 1
		self.type = "amphibian"
		self.name = "frog"

class Mouse(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 5
		self.strength = 1
		self.skittishness = 2
		self.luck = 1
		self.type = "mammal"
		self.name = "mouse"

class Salamander(Organism):
	def __init__(self):
		super().__init__()
		self.HP = 5
		self.strength = 2
		self.skittishness = 2
		self.luck = 1
		self.type = "amphibian"
		self.name = "salamander"




