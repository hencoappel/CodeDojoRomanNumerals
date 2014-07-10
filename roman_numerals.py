#!/usr/bin/env python3
import Counter from collections

num = "CDMXLICMLCIIVVC"

multi_table = {}
multi_table["I":{"I":"I","V":"V","X":"X","L":"L","C":"C","D":"D"}]
multi_table["V":{"I":"V","V":"XXV","X":"L","L":"CCL","C":"D","D":"MMD"}]
multi_table["X":{"I":"X","V":"L","X":"C","L":"D","C":"M","D":"MMMMM"}]
multi_table["L":{"I":"L","V":"CCL","X":"D","L":"MMD","C":"MMMMM"}]
multi_table["C":{"I":"C","V":"D","X":"M","L":"MMMMM"}]
multi_table["D":{"I":"D","V":"MMD","X":"MMMMM"}]

def sort_num(a):
	values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
	return "".join(sorted(a, key=lambda c: values[c], reverse=True))

def subtract(a, b):
	a = exploderise(a)
	b = exploderise(b)
	c = Counter(a)
	c.subtract(Counter(b))
	print(c)

def multiply(a, b):
	a = exploderise(a)
	b = exploderise(b)
	for(c1 in a):
		for(c2 in b):
			c.append(multitable[a][b])
	print(c)
