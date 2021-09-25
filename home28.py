"""1. Create a python function
factorial and import this 
file in another file and 
print factorial."""
# def fact(x):
# 	if isinstance(x,str):
# 		raise TypeError ("'str' object cannot be interpreted as an integer")
# 	elif isinstance(x,complex):
# 		raise TypeError ("'compex' object cannot be interpreted as an integer")
# 	elif isinstance(x,float):
# 		raise TypeError ("'float' object cannot be interpreted as an integer")
# 	elif x<0:
# 		raise ValueError ("factorial() not defined for negative values")
# 	elif x == 0:
# 		return 
# 	elif isinstance(x,int):
# 		c = 1
# 		for i in range(1,x+1):
# 			c*=1
# 		return c

"""2.Write a Python function to 
calculate surface volume and area of 
a cylinder(Գլան)."""
# from math import pi
# def sur(r,h):
# 	if isinstance(r,str) or isinstance(h,str):
# 		raise TypeError ("'str' object cannot be interpreted as an integer")
# 	elif r < 0 or h < 0:
# 		raise ValueError ("sur() not defined for negative values")
# 	else:
# 		return pi*(r**2)*h
# def area(r,h):
# 	if isinstance(r,str) or isinstance(h,str):
# 		raise TypeError ("'str' object cannot be interpreted as an integer")
# 	elif r < 0 or h < 0:
# 		raise ValueError ("sur() not defined for negative values")
# 	else:
# 		return 2 * pi * r * h + 2 * pi * r**2  
# r = float(input("The range is:"
# 	))
# h = float(input(
# 	"The height is: "
# 	))
# print(f'The surface: {sur(r,h)}') 
# print(f'The area: {area(r,h)}') 

"""3. Write a Python function 
to calculate surface volume 
and area of a sphere(Գունդ)."""
# from math import pi
# def s(r):
# 	if isinstance(r,str):
# 		raise TypeError ("'str' object cannot be interpreted as an integer")
# 	elif r < 0 :
# 		raise ValueError ("sphere() not defined for negative values")
# 	else:
# 		return 4/3*pi*r**3
# def sphere(r):
# 	if isinstance(r,str) :
# 		raise TypeError ("'str' object cannot be interpreted as an integer")
# 	elif r < 0 :
# 		raise ValueError ("sphere() not defined for negative values")
# 	else:
# 		return 4*pi*r**2
# r = float(input("The range is:"
# 	))
# print(f'The surface: {s(r)}') 
# print(f'The sphere: {sphere(r)}')

"""4. Write a Python function 
to convert degree to radian."""
# from math import pi
# def rad(d):
# 	return d*pi/180
# d = float(input("Degree: "))
# print(f'As radian: {rad(d)}')

"""5. Write a Python function to print 
all primes smaller than or equal to a 
specified number."""
# import math
# def primes(number):
# 	if isinstance(number,int):
# 		for i in range(2,number+1):
# 			for j in range(2,number):
# 				if  i % j ==0:
# 					continue
# 			else:
# 				numbers.append(i)
# 	else:
# 		print("Please write a number!")
# 	print(numbers)
# numbers = []
# number = int(input("Number:"))
# print(primes(number))
     """Wrong"""
