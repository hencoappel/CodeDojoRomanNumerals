#!/usr/bin/env python3
from collections import Counter
from exploderise import exploderise

values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

def sort_num(a, rev=True):
	return "".join(sorted(a, key=lambda c: values[c], reverse=rev))

def subtract(a, b):
	a = exploderise(a)
	b = exploderise(b)
	c = Counter(a)
	c.subtract(Counter(b))
	print(str(c))
	letters = values.keys()
	letters.sort(key=lambda c: values[c])
	for i, l in enumerate(letters):
		if c[l] < 0:
			print(c[l])
			c.subtract(Counter({l:-5, letters[i+1]:1}))
			print(str(c))

	print(str(c))
	print(sort_num(c.elements()))

subtract("M", "IV")
