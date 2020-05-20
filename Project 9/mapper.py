#!/usr/bin/python3
import sys
import string

def main():
	for line in sys.stdin:
		line = line.lower()
		for i in range(len(line)):
			if line[i] == '<':
				start = i+1
				tag = ''
				while is_valid(line,start):
					tag += line[start]
					start += 1
				if not '!' in tag and len(tag) != 0:
					print(tag+'\t1')
		

def is_valid(line,start):
	return start+1 < len(line) and line[start] != ' ' and line[start] != '>'

main()
