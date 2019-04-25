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

# Backup to be turned back on if things don't work
norglist = set()


# Opens the scientific names of organisms and reads them in with revisions to help with organization
def openitup():
	orglist = set()
	# Creates the regular expression to be used in identifying proper scientific names in the database being scraped
	cleanup = r"^[A-Z].+$"

	# Compiles the regex
	compiledclean = re.compile(cleanup)
	with open('scientificnames.txt', 'r') as file_stream:
		for line in file_stream:
			org_line = line.strip()
			org_name = org_line.split('\t')[0]
			#org_type = org_line.split('\t')[5]
			#temporglist.append(org_name)
			org_name = org_name.replace('[', '')
			org_name = org_name.replace(']', '')
			org_name = org_name.replace(' sp.', '')
			m = compiledclean.match(org_name)
			# You could also use if !m: effectively
			if m:
				#print(line)
				orglist.add(org_name)
	return orglist


### TURN BACK ON AFTER DEBUGGING ###
#openitup()
			

# Reads the fifth column in a tab-delimited line
#[print(line.split('\t')[5]) for line in truemaster]

# Class given to all objects to exist in the game.
class gameObject(object):
	def __init__(self):
		self.name = name

class Food(gameObject):
	def __init__(self):
		self.quality = 1

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

### TURN BACK ON AFTER DEBUGGING ###
#orglist = sorted(orglist)

#print(orglist)


### TURN BACK ON AFTER DEBUGGING ###
#popmaster = populatemaster(orglist)






def scrapetypes(poplist):
	with open ('eukaryotes.txt', 'r') as file_stream:
		for line in file_stream:
			for organism in poplist:
				if organism.truename in line:
					organism.type = line.split('\t')[5]
	return poplist





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


# Assigns each organism a game class based on the Linnaean taxonomic group to which it belongs
# (And is most recognizable; e.g. "Reptile" over simply "Organism")
def givetype(poplist):
	typedict = {
	"Reptiles" : Reptile,
	"Amphibians" : Amphibian,
	"Birds" : Bird,
	"Mammals" : Mammal,
	"Fungi" : Fungus,
	"Ascomycetes" : Ascomycetes,
	"Insects" : Insect,
	"Fishes" : Fish,
	"Plant" : Plant,
	"Protist" : Protist,
	"Kinetoplasts" : Kinetoplast,
	"Other Animals" : Dragon,
	"Other" : Monster,
	"Organism" : Pokemon,
	"Basidiomycetes" : Basidiomycetes,
	"Apicomplexans" : Apicomplexan,
	"Flatworms" : Flatworm,
	"Roundworms" : Roundworm,
	"Green Algae" : greenAlgae
	}
	

	holderlist = []
	tempnames = []
	i = 0



	### THIS WORKS NOW BECAUSE I'M INSTANTIATING EACH CLASS IN THE FOR LOOP INSTEAD OF ABOVE IN THE DICTIONARY--
	### I.E. IF YOU PUT () PARENTHESES IN THE DICTIONARY VALUES, IT ONLY INSTANTIATES EACH CLASS ONCE INSTEAD OF EACH TIME
	for org in poplist:
		holderlist.append(org)
		tempnames.append(org.name)
		for key in typedict.keys():
			if (key.lower() in holderlist[i].type.lower()):
				holderlist[i] = typedict[key]()
				holderlist[i].truename = tempnames[i]
				holderlist[i].name = tempnames[i]
				holderlist[i].sex = random.randint(0,1)
				holderlist[i].genfood()
				if holderlist[i].sex == 1:
					holderlist[i].sex = "male"
				elif holderlist[i].sex == 0:
					holderlist[i].sex = "female"
				#print(holderlist[i], holderlist[i].type)
		i+=1

	return holderlist




