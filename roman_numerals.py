#!/usr/bin/env python3
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
def sort_num(a, rev=True):
	return "".join(sorted(a, key=lambda c: values[c], reverse=rev))

sorter = lambda c: values[c]

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


def subtract(a, b):
	a = exploderise(a)
	b = exploderise(b)
	c = Counter(a)
	c.subtract(Counter(b))
	letters = values.keys()
	letters.sort(key=lambda c: values[c])
	for i, l in enumerate(letters):
		if c[l] < 0:
			if letters[i] == 'V':
				c.subtract(Counter({l:-2, letters[i+1]:1}))
			else:
				c.subtract(Counter({l:-5, letters[i+1]:1}))
	print(sort_num(c.elements()))
	return compressurise(combine(sort_num(c.elements())))
a = raw_input("Num one:")
b = raw_input("Num two:")
print(subtract(a, b))

def multiply(a, b):
	a = exploderise(a)
	b = exploderise(b)
	for c1 in a:
		for c2 in b:
			c.append(multitable[a][b])
#	print(c)


def add(a, b):
	a = exploderise(a)
	b = exploderise(b)
	combination = a + b

	reversed_sorted_combination = "".join(sorted(combination, key=sorter, reverse=False))

#	print(reversed_sorted_combination)

	combined = combine(reversed_sorted_combination)

	comine.reverse()
	return compressurise(combined)

print(add("CCCLXVIIII", "DCCCXXXXV"))
