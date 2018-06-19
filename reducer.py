import sys
import re


for line in sys.stdin:  # standard input from the output file of mapper2

	cont = line.split("\t")	# split the input line
	iid = cont[4]	# 5th filed of the array be iid
	recievers = cont[1].split(',')

	for row in recievers:   # get the required fields in the required format
		print '%s\t%s\t%s\t%s' % (cont[2], cont[0], r, iid)

