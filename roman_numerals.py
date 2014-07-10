#!/usr/bin/env python3

num = "CDMXLICMLCIIVVC"

values = {
		'M':1000,
		'D':500,
		'C':100,
		'L':50,
		'X':10,
		'V':5,
		'I':1
		}
sorter = lambda c: values[c]

print("".join(sorted(num, key=sorter, reverse=True)))

def subtract():
	
