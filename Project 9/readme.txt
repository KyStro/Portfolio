- My program goes through a directory of html files and finds all the tags in the source code. It then counts all the occurences of the starting and closing tags.

- The mapper sets the source code to lowercase. It then goes through each line and checks if the character is a '<'. If so, it scans the rest of the line until it reaches a ' ' or '>'. The program disregards tags with a '!' and assumes they are comments. A 1 is added with a tab to each tag found and printed.

- Example format would be:
	
/u	1
/u	1
/ul	1
/ul	1
hr	1
html	1
img	1
img	1
li	1
li	1

This shows the opening or closing tag name and a 1 when it is found.

- The reducer I took from the example Russ gave. It takes the output from mapper.py and unpacks it into word and count. Because the output is sorted it checks a new word and while that word is still on the next line it will increment the count. The tag with the total times it appears in the job is printed like:

Ex:

/u	11
/ul	12
a	86
b	16
body	1
br	11	
