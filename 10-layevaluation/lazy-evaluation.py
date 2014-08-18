#!/usr/bin/env python
#coding: utf-8
#Filename: lazy-evaluation.py

from itertools import islice

def fib():
''''''
	a, b = 0 ,1
	while True:
		yield a 
		# yield, 返回一个生成器。生成器可以在需要的时候一次便利集合中的一个元素。从而避免因为将集合中的元素一次性加入内存而导致的内存不足
		a, b = b, a + b

print list(islice(fib(), 10))