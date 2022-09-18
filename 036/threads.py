from threading import Thread
import os
import math

def calc():
	for i in range(0, 4000000):
		math.sqrt(i)

'''
# -----------------------------------------------------------
I think this WRONG:
WHY: for each cpu a new thread will be started to perform calc.
that's why threads.py script takes much extra time then
processes.py script. 
# -----------------------------------------------------------
	
threads = []

for i in range(os.cpu_count()):
	print('registering thread %d' % i)
	threads.append(Thread(target=calc))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()
'''

thread = Thread(target=calc)
thread.start()
thread.join()
