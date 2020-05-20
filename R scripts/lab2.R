# Name: Kyle Strokes
# Date: 1/23/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 2
# Collaborator: Elaine Mancillas

source("http://www.openintro.org/stat/data/arbuthnot.R")
source("http://www.openintro.org/stat/data/present.R")

#1
dim(present)
# 63 rows, 3 columns

#2
names(present)
# year, boys, girls

#3
present$year
# 1940-2002

#4
arbuthnot$boys
present$boys
arbuthnot$girls
present$girls
# The number of boys and girls are larger in the present data than in the arbuthnot data

#5
plot(arbuthnot$year, arbuthnot$boys/arbuthnot$girls)
# Boys are more common because the ratio lays over 1 for most years

#6
plot(present$year, present$boys/present$girls)
# Boys are still more common but it is a lower ratio

#7
present[60, "girls"]

#8
# The brackets are asking to "index" like in Python, to get the variable at a given row and column. The first element is the number of the row, and the second element is the name of the column.

#9
?which.max
# Determines the location, i.e., index of the (first) minimum or maximum of a numeric (or logical) vector.

#10
which.max(present$boys + present$girls)
present[22, "year"]
# 1961
