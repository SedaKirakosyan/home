"""1. Odd
Write a recursive function to determine whether all 
digits of the number are odd or not. """
# def test(num):
# 	if int(num[-1]) % 2 == 0:
# 		return False
# 	elif len(num) == 1:
# 		return True
# 	else:
# 		return test(num[:-1])
# num = input("number:")
# print(test(num))

"""2.Write a python function all even number in 
10.000 use threading and print time. """
# import threading
# import time
# def even():
# 	for i in range(1,10001):
# 		if i % 2 == 0:
# 			 print(i)
# start = time.time()
# t1 = threading.Thread(target=even, args=(1,2500))
# t2 = threading.Thread(target=even, args=(2500,5000))
# t3 = threading.Thread(target=even, args=(5000,7500))
# t4 = threading.Thread(target=even, args=(7500,10000))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# even()
# print(time.time()-start)

"""3. Numbers
Given N number. Write a recursive function that 
should print from 1 to N numbers."""
# def num(number):
# 	if number == 1:
# 		return print(number)
# 	else:
# 		print(number)
# 	num(number-1)
# number = int(input("Write a number: "))
# num(number)












