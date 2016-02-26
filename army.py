#!/usr/bin/env python
import random

class Army(object):
	def __init__(self, size):
		self.size = size
	
	def __str__(self):
		return "size = ({0})".format(self.size)
		
# In order, Light Inf, Heavy Inf, Archers, Light Cav, Heavy Cav, Pikemen


armyTypes = {"Light Infantry" : random.randint(1000, 3000) * 3,
			 "Heavy Infantry" : random.randint(300, 800),
			 "Archers" : random.randint(400, 900),
			 "Light Cavalry" : random.randint(400, 900),
			 "Heavy Cavalry" : random.randint(200, 600),
			 "Pikemen" : random.randint(100, 400)
			}

print("LI: {0}, HI: {1}, AR: {2}, LC: {3}, HC: {4}, PI: {5}".format(
armyTypes["Light Infantry"], armyTypes["Heavy Infantry"], armyTypes["Archers"],
armyTypes["Light Cavalry"], armyTypes["Heavy Cavalry"], armyTypes["Pikemen"]))



print("TOTAL: {0}".format(sum(armyTypes.values())))
