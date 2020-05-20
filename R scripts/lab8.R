# Name: Kyle Strokes
# Date: 3/13/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 8
# Collaborator: Elaine Mancillas

download.file("http://www.openintro.org/stat/data/bdims.RData", destfile = "bdims.RData")
load("bdims.RData")

#1
fdims <- subset(bdims, sex == 0)
f.hgt.hist <- hist(fdims$hgt, probability = TRUE, breaks = 20)
# Yes, the data looks more than less normally distributed because most of the data would be under the bell curve.

#2
xs <- seq(min(fdims$hgt), max(fdims$hgt), 0.10)

#3
ys <- dnorm(xs, mean(fdims$hgt), sd(fdims$hgt))

#4
hist(fdims$hgt, probability = TRUE, ylim = c(0, 0.07), breaks = 20)
lines(xs, ys)
# Every bar of the histogram should be intersected by the normal distribution line. The histogram bars and the normal distribution line are very close to a normal distribution.

#5
qqnorm(fdims$hgt)
qqline(fdims$hgt)
# If the qq plot observations lie along the qqline, the data is considered normally distributed. Most of the observations of the female heights fall on the qqline which means it is normally distributed.

#6
f.hgt.sample <- rnorm(nrow(fdims), mean(fdims$hgt), sd(fdims$hgt))
qqnorm(f.hgt.sample)
qqline(f.hgt.sample)
# The random sample data lies very closely to the qqline on the qqplot. The deviations of the outliers are due to random numbers in the sample

#7
qqnormsim(fdims$hgt)
# The simulated qqplots show the variance of observations due to random variables. Since the female heights do not deviate much from the qqline meaning the observations are normally distributed.

#8
qqnorm(fdims$age)
qqline(fdims$age)
qqnormsim(fdims$age)
qqnorm(fdims$wgt)
qqline(fdims$wgt)
qqnormsim(fdims$wgt)
# After random simulations of age and weight of females besides just looking at the data alone. Age seems to be more than less normally distributed. Weight varies too much for me to conclude it is normally distributed.

#9
pnorm(182, mean(fdims$hgt), sd(fdims$hgt), lower.tail = FALSE)
nrow(subset(fdims, hgt > 182)) / nrow(fdims)
# The prediction prediction is close to the observations, difference maybe due to random sampling or because the female heights are not prefectly normal distributed

#10
f.ninith.percentile <- qnorm(0.9, mean(fdims$hgt), sd(fdims$hgt), lower.tail = FALSE)
nrow(subset(fdims, hgt > f.ninith.percentile)) / nrow(fdims)
#Yes, the proportion got from the qnorm (156 cm) over the total number of female is the dataset matches very closely to the 90th precentile (0.907).