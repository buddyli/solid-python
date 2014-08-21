#!/usr/bin/env python
#coding: utf-8
#Filename: quicksort.py

"""quicksort in python"""

def qsort(arr):
	print arr
	'''pivot选取每个子分区的第一个元素，然后递归遍历剩余的元素'''
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		return qsort([x for x in arr[1:] if x < pivot]) + \
			[pivot] + \
			qsort([x for x in arr[1:] if x >= pivot])

if __name__ == '__main__':
	arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50]
	print 'Source: ', arr

	arr  = qsort(arr)
	print 'Target: ', arr