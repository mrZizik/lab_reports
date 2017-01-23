from randio import Randio
import random
import time

start = time.time()
a = Randio()
b = random.Random()
with open("ou1t.csv","w") as out:
	for i in xrange(100):
		print a.random()