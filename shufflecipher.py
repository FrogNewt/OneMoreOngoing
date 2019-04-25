#!/usr/bin/env python3

import re


#f = open('scientificnames.txt', 'r')

# names = f.read()

def megacipher(organism):
	megadict = {
	"a" : "e",
	"e" : "i",
	"o" : "a",
	"i" : "u",
	"u" : "e",
	"y" : "o",
	"b" : "v",
	"c" : "d",
	"d" : "f",
	"f" : "g",
	"g" : "h",
	"h" : "j",
	"j" : "k",
	"k" : "l",
	"l" : "m",
	"m" : "n",
	"n" : "p",
	"p" : "q",
	"q" : "r",
	"r" : "l",
	"s" : "t",
	"t" : "c",
	"w" : "x",
	"x" : "z",
	"z" : "b"
	}

	shortname = ""
	genus = ""
	species = ""

	temptemp = organism.truename.split(" ")
	if len(temptemp) > 1:
		genus = temptemp[0]
		species = temptemp[1]
	else:
		shortname = temptemp[0]


	if len(genus) > 6:
		genus = genus[:6]
	if len(species) > 6:
		species = species[:6]
	if genus and species:
		shortname = genus + " " + species


	megaorg = ""
	for i in shortname.lower():
		if i.lower() in megadict.keys():
			megaorg += megadict[i]
		else:
			megaorg += i
	megaorg = megaorg.capitalize()
	organism.meganame = megaorg
	organism.name = megaorg
	return megaorg


def intercipher(organism):
	interdict = {
	"a" : "e",
	"e" : "i",
	"o" : "a",
	"i" : "u",
	"u" : "e",
	"y" : "o",
	}
	interorg = ""
	for i in organism.truename.lower():
		if i in interdict.keys():
			interorg += interdict[i]
		else:
			interorg += i
	interorg = interorg.capitalize()
	organism.intername = interorg
	return interorg


#orglist = []

# Note that sets only add things that are new!
orglist = set()

cleanup = r"^[A-Z].*$"

compiledclean = re.compile(cleanup)


#temporglist = []
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








orglist = sorted(orglist)

#print(orglist)


# Shuffles all newly-cleaned organisms in orglist

# By megacipher
#megaorglist = [megacipher(organism) for organism in orglist]
#print(megaorglist)


# By intercipher
#interorglist = [intercipher(organism) for organism in orglist]

#print(interorglist)

#print(orglist)

#f.close()


#testwords = ["sparrow", "terrapin", "frog", "bbomb", "ramen", "Jamie", "Scott"]


#for word in testwords:
#	print(megacipher(word), intercipher(word))


# Going forward, be explicit about splitting on "tab" (which is, in quotes, \t)
# so .split("\t")
# Check to see if the first element (element zero) is in orgnames list
# If it is, you can do whatever it is with list element two
# Note, every line is made into its own list if you do the with open thing


# When you're looking at the first element, it might help to split those into a list so that you can sort through THOSE and take a look to see who's what



