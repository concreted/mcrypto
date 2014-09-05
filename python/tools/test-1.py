import os

for i in range(8):
	i = i + 1
	print "==========1-%i==========" % i
	os.system('python 1-%i.py' % i)