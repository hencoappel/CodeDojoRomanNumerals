#!/usr/bin/env python3
import re
import sys

from collections import Counter
from exploderise import exploderise
from compressurise import compressurise


values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

#multi_table = {}
#multi_table["I":{"I":"I","V":"V","X":"X","L":"L","C":"C","D":"D"}]
#multi_table["V":{"I":"V","V":"XXV","X":"L","L":"CCL","C":"D","D":"MMD"}]
#multi_table["X":{"I":"X","V":"L","X":"C","L":"D","C":"M","D":"MMMMM"}]
#multi_table["L":{"I":"L","V":"CCL","X":"D","L":"MMD","C":"MMMMM"}]
#multi_table["C":{"I":"C","V":"D","X":"M","L":"MMMMM"}]
#multi_table["D":{"I":"D","V":"MMD","X":"MMMMM"}]

def sorter(c): return values[c]

def sort_num(a, rev=True):
	return "".join(sorted(a, key=sorter, reverse=rev))

def combine(string):
	string = string[::-1]
	replaces = [
		['IIIII', 'V'],
		['VV', 'X'],
		['XXXXX', 'L'],
		['LL', 'C'],
		['CCCCC', 'D'],
		['DD', 'M']
	]
	previous_length = 0
	for replace in replaces:
		while previous_length != len(string):
			previous_length = len(string)
			string = string.replace(*replace)
		previous_length = 0
	return string[::-1]

class RomanNumeral():

	def __init__(self, num):
		self.num = num

	def __sub__(self, other):
		num1 = exploderise(self.num)
		num2 = exploderise(other.num)
		c = Counter(num1)
		c.subtract(Counter(num2))
		letters = sorted(values.keys(), key=sorter)
		for i, l in enumerate(letters):
			if c[l] < 0:
				if l == 'V':
					c.subtract(Counter({l:-2, letters[i+1]:1}))
				else:
					c.subtract(Counter({l:-5, letters[i+1]:1}))
		expanded_number = sort_num(c.elements())
		corrected_number = compressurise(combine(expanded_number))
		return RomanNumeral(corrected_number)

	def multiply(a, b):
		a = exploderise(a)
		b = exploderise(b)
		for c1 in a:
			for c2 in b:
				c.append(multitable[a][b])


	def __add__(self, other):
		num1 = exploderise(self.num)
		num2 = exploderise(other.num)
		combination = num1 + num2
		reversed_sorted_combination = sort_num(combination, rev=False)
		combined = combine(reversed_sorted_combination)
		combined[::-1]
		return RomanNumeral(compressurise(combined))

	def __str__(self):
		return self.num

if __name__ == "__main__":
	if not len(sys.argv) == 4:
		print("Put the equation as arguments to the program.")
	a = RomanNumeral(sys.argv[1])
	b = RomanNumeral(sys.argv[3])
	op = sys.argv[2]
	val = eval("a " + op + " b")
	print(val)
