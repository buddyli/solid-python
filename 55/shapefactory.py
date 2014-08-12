#!/usr/bin/env python
#coding: utf-8
#Filename: shapefactory.py

'''
Object.__new__()是实例化对象时调用的方法。一般改方法会返回一个改对象的instance。
Object.__init__()是初始化对象属性时调用的方法。

__new()__返回的实例对象如果不为空，那么会默认调用__init__()方法，因此__init__()总是会默认执行。
'''

class Shape(object):
	"""docstring for Shape"""
	def __init__(object):
		pass

	def draw(self):
		pass

class Triangle(Shape):
	""""""
	def __init__(self):
		print 'i am a Triangle'

	def draw(self):
		print 'i am drawing a Triangle'

class Rectangle(Shape):
	""""""
	def __init__(self):
		print 'i am a Rectangle'

	def draw(self):
		print 'i am drawing a Rectangle'

class Trapezoid(Shape):
	""""""
	def __init__(self):
		print 'i am a Trapezoid'

	def draw(self):
		print 'i am drawing a Trapezoid'

class Diamond(Shape):
	""""""
	def __init__(self):
		print 'i am a Diamond'

	def draw(self):
		print 'i am drawing a Diamond'

# object factory
class ShapeFactory(object):
	shapes = {"triangle": Triangle, "rectangle": Rectangle, "trapezoid": Trapezoid, 
				"diamond": Diamond}

	# static method
	def __new__(klass, name):
		if name in ShapeFactory.shapes.keys():
			print 'creating a new shape %s' % name
			return ShapeFactory.shapes[name]()
		else:
			print 'creating a new shape %s' % name
			return Shape()

if __name__ == '__main__':
	ShapeFactory('diamond').draw()
	ShapeFactory('shape').draw()

