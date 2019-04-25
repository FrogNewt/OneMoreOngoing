#!/usr/bin/env python3

import sys
import re
import os
import pickle
#import activityengine
import gameclasses
#import organisms
#from shufflecipher import *

#Shuffles organisms into unrecognizable names
#megaorglist = [megacipher(organism) for organism in popmaster]
#print(megaorglist)

#newplayer = Player()





newplayer = gameclasses.Player()




def main(player):

	# Prompts the user to choose whether to load an existing game or play a new game.


	
	gameclasses.choosenext(gameclasses.begingame())


	#player.opener()



if __name__ == "__main__":
	main(newplayer)

