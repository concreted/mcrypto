import os

for i in range(8):
	i = i + 9
	if i != 14:
		print "==========2-%i==========" % i
		os.system('python 2-%i.py' % i)