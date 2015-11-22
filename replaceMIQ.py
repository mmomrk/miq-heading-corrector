#!/usr/bin/python
#this will deal with encoding: utf-8

import sys
import random as rand

if len(sys.argv)<2:
	print "A program for enchancing post names.\n Useage: replaceMIQ.py filename\nWill produce a second file with replacements. HF"
	sys.exit()

filename = sys.argv[1]
fle = open(filename,'r')

outName = filename
if len(filename)>5:
	outName = filename[:-5] + "_modified" + filename[-5:]	#hardcoded for html. will work with others too 
else:
	outName = filename+"withABiggerNameThisFileWouldHaveLookedCuter.html"
ofle = open(outName,'w')

huntFor = "Ученые" # изготовили первую в мире оптическую ректенну, способную конвертировать световое излучение в электрический

replacements = ["Мужики", "Коллеги", "Короче,", "Товарищи", "Мы (ну, не совсем)", ""]
replacements+=[huntFor]
print replacements

lines = fle.readlines()

def nextLineIsHeading(line):
#	line = unicode(lineNonU,"UTF-8)
	if "h1 class=\"entry-title\"" in line:
		return True
	return False

def lineHasThatWord(line):
	if 'mark">' + huntFor in line[:10]:	#what a code without a kostyl?
		return True
	return False

def getRandomNewWord():
	return replacements[rand.randint(0,len(replacements) - 1)]

approachFlag = False

for line in lines:
	if approachFlag and lineHasThatWord:
		replacement = line.replace(huntFor,getRandomNewWord())
		ofle.write(replacement)
		print replacement
	else:
		ofle.write(line)
	approachFlag = nextLineIsHeading(line)
	
#let's cosplay an old hardcore programmer:
fle.close()
ofle.close()

