#!/usr/bin/env python

import random

# Simple list of names, could be moved to a txt later on
names = ["Sigurd", "Snorri", "Rollo", "Erik", "Olaf", "Leif"]
lastnames = ["Fairhair", "Snake-in-the-Eye", "Ironside", "Rustbeard", "Stonehand", "Thickskull"]
AGE_MIN = 16
AGE_MAX = 34

class Character(object):
    def __init__(self, name, lastname, stats, age):
        self.name = name
        self.lastname = lastname
        self.stats = stats
        self.age = age
    def __str__(self):
        return "{0} {1} ({2}): {3}".format(
        	self.name,
        	self.lastname,
        	self.age,
        	format_stats(self.stats))

# Stats (in order): diplomacy, military, stewardship, intrigue, learning
def random_stats():
    return [
    	random.randint(1,10),
    	random.randint(1,10),
    	random.randint(1,10),
    	random.randint(1,10),
    	random.randint(1,10)
    ]

def format_stats(stats):
	return """diplomacy: {0}, military: {1}, stewardship: {2}, intrigue: {3}, learning: {4}""".format(*stats)
	
def new_random_character():
	name = random.choice(names)
	lastname = random.choice(lastnames)
	age = random.randint(AGE_MIN, AGE_MAX)
	stats = random_stats()
	return Character(name, lastname, stats, age)

# Create and print the king character
king = new_random_character()
print(king)
