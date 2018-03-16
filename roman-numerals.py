# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 16:37
# @Author  : famu
# @File    : roman-numerals.py
# @Software: PyCharm

def checkioMe(data):
	cnt = [1000, 500, 100, 50, 10, 5, 1]
	chr = ["M", "D", "C", "L", "X", "V", "I"]
	s = ""
	for i, v in enumerate(cnt):
		k, data = divmod(data, v)
		s += chr[i] * k
	s = s.replace("IIII", "IV").replace("XXXX", "XL").replace("CCCC", "CD").replace("DCD", "CM").replace("VIV", "IX").replace("LXL", "XC")
	return s

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(6) == 'VI', '6'
	assert checkio(76) == 'LXXVI', '76'
	assert checkio(499) == 'CDXCIX', '499'
	assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'