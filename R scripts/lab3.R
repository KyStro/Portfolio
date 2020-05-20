# Name: Kyle Strokes
# Date: 1/30/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 3
# Collaborator: Elaine Mancillas

source("http://www.openintro.org/stat/data/cdc.R")

#1
plot(cdc$weight, cdc$wtdesire)
# There is a positive correlation between weight and weight desired; the more someone weighs, the more their desired weight

#2
wdiff <- cdc$weight - cdc$wtdesire
# If wdiff = 0 then they are at desired weight, if wdiff > 0 then they have to lose that number to be at the weigth desired, if wdiff < 0 then they want to gain weight

#3
summary(wdiff)
# median is 10, I used it beause looking at the scatterplot there seems to be some outliers to inflate the mean.

#4
hist(wdiff)
boxplot(wdiff)
# I used hist() to see that the skew is hard to see then I looked at the summary() to see that the mean > median so the data is right skewed. Finally I used a boxplot to see that more point laid to the right than the left of the quartiles

#5
# By the summary and boxplot I see that more people want to lose weight rather than gain weight. Most people want lose between 0-21 lbs.

#6
boxplot(cdc$weight - cdc$wtdesire ~ cdc$gender)
# More men would like to gain weight compared to women, both have a significant number trying to lose weight

#7
summary(wdiff)
View(cdc$wtdesire)
# One person wants to gain 500 lbs that is unreasonable. Another person wants to gain 300 lbs. There are high weight loss desires but I like to think those are pausible

#8
mean_weight <- mean(cdc$weight)
sd_weight <- sd(cdc$weight)
sd_below <- mean_weight - sd_weight
sd_above <- mean_weight + sd_weight
sd_belowx2 <- mean_weight - (2*sd_weight)
sd_abovex2 <- mean_weight + (2*sd_weight)
sd_below
sd_above
sd_belowx2
sd_abovex2
# One standard deviation below the mean = 129.602, 1 standard deviation above the mean = 209.7639, 2 standard deviation below the mean = 89.52101, 2 standard deviation above the mean = 249.8449

#9
nrow(subset(cdc, cdc$weight <= sd_above & cdc$weight >= sd_below))
nrow(subset(cdc, cdc$weight <= sd_abovex2 & cdc$weight >= sd_belowx2))
# 14152/20000 observations are within 1 standard deviation of the mean, while 19126/20000 are within 2 standard deviations.

#10
mean_height <- mean(cdc$height)
sd_height <- sd(cdc$height)
sd_height_below1 <- mean_height - sd_height
sd_height_above1 <- mean_height + sd_height
sd_height_below2 <- mean_height - (2*sd_height)
sd_height_above2 <- mean_height + (2*sd_height)
nrow(subset(cdc, cdc$height <= sd_height_above1 & cdc$height >= sd_height_below1))
nrow(subset(cdc, cdc$height <= sd_height_above2 & cdc$height >= sd_height_below2))
mean_age <- mean(cdc$age)
sd_age <- sd(cdc$age)
sd_age_below1 <- mean_age - sd_age
sd_age_above1 <- mean_age + sd_age
sd_age_below2 <- mean_age - (2*sd_age)
sd_age_above2 <- mean_age + (2*sd_age)
nrow(subset(cdc, cdc$age <= sd_age_above1 & cdc$age >= sd_age_below1))
nrow(subset(cdc, cdc$age <= sd_age_above2 & cdc$age >= sd_age_below2))
# 12425/20000 of heights are within 1 standard deviation of the mean. 19545/20000 of heights are within 2 standard deviations of the mean. 12806/20000 of ages are within 1 standard deviation of the mean. 19386/20000 of ages are within 2 standard deviations of the mean?
  
