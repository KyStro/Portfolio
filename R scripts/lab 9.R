# Name: Kyle Strokes
# Date: 3/20/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 9
# Collaborator: Sami Robbins

download.file("http://www.openintro.org/stat/data/ames.RData", destfile = "ames.RData")
load("ames.RData")

#1
gmean = ames$Gr.Liv.Area
avg = mean(gmean)
#1499.69

#2
sample = sample(gmean, size = 50)
sample_mean = mean(ames.gr.liv.area.sample)
#Yes, the sample mean 1485.06 is a good estimation of the total population of 1499.69

#3
par(mfrow = c(2,1))
area_lim = range(gmean)
#334 5642

#4
hist(gmean, xlim = area.xlim)
abline(v = avg, col = "blue")

#5
hist(sample, xlim = area.xlim)
abline(v = sample_mean, col = "red")
#The two plots are closely identical. The sample mean had a lower size so the number for each category is smaller.

#6
mean_area = replicate(5000, {s = sample(gmean, size = 10) ; s_mean = mean(s)})
hist(mean_area)
#The distribution still has a similar mean, but the data resembles a normal distribution more than less

#7
s_gmean = sample(gmean, size = 50)
s_gmean_mean = mean(s_gmean)
sample_means = replicate(5000, {s_gmean = sample(gmean, size = 50) ; s_gmean_mean = mean(s_gmean) })
samp = sample(gmean, size = 100)
samp_mean = mean(samp)
area.means.100 = replicate(5000, {samp = sample(gmean, size = 100) ; samp_mean = mean(samp) })

#8
par(mfrow = c(3,1))
mean_area_range = range(mean_area)
#num [1:2] 1038 2223

#9
hist(area.means.10, breaks = 20, xlim = mean_area_range)
hist(area.means.50, breaks = 20, xlim = mean_area_range)
hist(area.means.100, breaks = 20, xlim = mean_area_range)
#The largest sample has the highest frequency, I estimate 100

#10
samp1 = sample(gmean, size = 1)
mean_samp1 = mean(samp1)
samp2 = sample(gmean, size = 2930)
mean_samp2 = mean(samp2)
hist(replicate(4000, samp2))
mean(sample(gmean))
#The sample size with 1 would produce more 10, 50, and 100 columns, while 2930 would have 1 column with due to the larger sample size.
