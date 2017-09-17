#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(argv):
	#i is number, and v is the input(digit)
  for i, v in enumerate(argv):
    sv = int(v)
    conwaySequence(sv)

sequ = {
		1: 1,
	}

def conwaySequence(inte):
	global sequ
	if inte == 1: 
		print 1
		return 1
	for i in xrange(2,inte+1):
		nextSequence = conWay(sequ[i-1])
		sequ[i]=nextSequence
	print nextSequence
	return nextSequence

def conWay(num):
	if num == 1: return 11
	numstr = str(num)
	outPut = ""
	repCount = 0
	for digit in numstr:
		if repCount == 0:
			store = digit
			repCount =1
		elif digit == store:
			repCount +=1
		else:
			outPut = outPut+str(repCount)+store
			store = digit
			repCount = 1
	outPut = outPut+str(repCount)+store
	return int(outPut)


#maybe can write the sequence in a file for loading next time
