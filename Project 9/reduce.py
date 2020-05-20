#!/usr/bin/python3
import sys
cur = None
total = 0
for line in sys.stdin:
	(word,count) = line.split()
	count = int(count)
	if word == cur:
		total += count
	else:
		if cur is not None:
			print("%s\t%d" % (cur,total))
		cur = word
		total = count
if cur is not None:
	print("%s\t%d" % (cur,total))
