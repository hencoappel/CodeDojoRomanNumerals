#!/usr/bin/ianb/ptyhon3

import re

def exploderise(roman_numeral):
	
	roman_numeral = roman_numeral.upper()
	
	conversion = {}
	conversion["IV"] = "IIII"
	conversion["IX"] = "VIIII"
	conversion["XL"] = "XXXX"
	conversion["XC"] = "LXXXX"
	conversion["CD"] = "CCCC"
	conversion["CM"] = "DCCCC"
	
	for key in conversion:
		roman_numeral = re.sub(key, conversion[key], roman_numeral)

	return roman_numeral	
