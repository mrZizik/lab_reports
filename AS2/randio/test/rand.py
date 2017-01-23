import randio
import random
import time

import struct


start = time.time()
a = randio.Randio()
a.sample()
arr = []
with open("6","wb") as out:
	for i in xrange(100):
		arr.append(a.random())
	out.write(struct.pack('f'*len(arr), *arr))