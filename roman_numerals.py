#!/usr/bin/env python3
import Counter from collections

num = "CDMXLICMLCIIVVC"


def sort_num(a):
	values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
	return "".join(sorted(a, key=lambda c: values[c], reverse=True))

def subtract(a, b):
	a = exploderise(a)
	b = exploderise(b)
	c = Counter(a)
	c.subtract(Counter(b))
	print(c)

