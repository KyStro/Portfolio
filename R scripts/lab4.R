# Name: Kyle Strokes
# Date: 2/6/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 4
# Collaborator: Elaine Mancillas

#1
boxplot(heartTr$survtime)
# There are about 9 outliers

#2
boxplot(log(heartTr$survtime))
# I do not see any outliers

#3
# It changes because the log() function "squashes" data to fit on graphs

#4
surv_vs_transplant <- table(heartTr$survived, heartTr$transplant)
# 34 people in the control group survived

#5
prop.table(surv_vs_transplant, margin = 2)
# treatment patients were more likely to survive

#6
prop.table(surv_vs_transplant, margin = 1)
# "Out of the alive people: 14% were control and 85% were treatment. Out of the dead people: 40% were control and 60% were treatment". They are different because #5 gave percentages out of control and treatment groups.

#7
year_vs_surv <- table(heartTr$survived, heartTr$acceptyear)
barplot(year_vs_surv)
# The percentage people surviving seems to be increasing

#8
barplot(year_vs_surv, legend.text = TRUE)
# Less people seem to die as years progress

#9
year_vs_propcontrol <- prop.table(table(heartTr$transplant, heartTr$acceptyear), margin = 2)
barplot(year_vs_propcontrol, legend.text = TRUE)
# It looks like less people are recieved control transplant as years advanced

#10
mosaicplot(table(heartTr$acceptyear, heartTr$transplant))
# It is hard to find a trend with this graph, but it is able to show you the magnitude of the population of a certain you and the split correlates to the percentage of the treatment and control groups