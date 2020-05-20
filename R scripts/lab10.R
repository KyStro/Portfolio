# Name: Kyle Strokes
# Date: 3/27/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 10
# Collaborator: Elaine Mancillas

download.file("http://www.openintro.org/stat/data/ames.RData", destfile = "ames.RData")
load("ames.RData")

#1
s_liv_area = sample(ames$Gr.Liv.Area, 60, replace = FALSE)
s_liv_mean = mean(s_liv_area)
#1491.567

#2
stand_err = sd(s_liv_area) / (sqrt(60))
# 73.15

#3
rate <- 1.96 * stand_err
upper <- mean(s_liv_area) + rate
lower <- mean(s_liv_area) - rate
range <- c(lower, upper)

#4
true_mean <- mean(ames$Gr.Liv.Area)
#1499.69, yes it falls within 1380 and 1602.

#5
rep_50 <- replicate(50, {samp = sample(ames$Gr.Liv.Area, 60, replace = FALSE); se = sd(samp) / sqrt(60); rate2 = 1.96 * se; upper2 = mean(samp) + qnorm(1-(1-0.95)/2) * se; lower2 = mean(samp) - qnorm(1-(1-0.95)/2) * se; matrix_samp = c(lower2, upper2)})
dim(rep_50)

#6
lower.bounds <- rep_50[1,]
upper.bounds <- rep_50[2,]
len_lower <- length(lower.bounds)
len_lower <- length(upper.bounds)
# both = 50

#7
confid_inter <- plot_ci(lower.bounds, upper.bounds, true_mean)
# 2 do not fall within the range, I believe this is on par with my expectations because 95% confidence sampled 50 times should produce 2.5 outliers

#8
crit <- qnorm(1-(1-0.99)/2)
# 99% confidence yields a 2.575 critical value

#9
new_rep_50 <- replicate(50, {samp = sample(ames$Gr.Liv.Area, 60, replace = FALSE); se = sd(samp) / sqrt(60); rate2 = 1.96 * se; upper2 = mean(samp) + crit * se; lower2 = mean(samp) - crit * se; matrix_samp = c(lower2, upper2)})
lower.bounds2 <- new_rep_50[1,]
upper.bounds2 <- new_rep_50[2,]
confid_inter2 <- plot_ci(lower.bounds2, upper.bounds2, true_mean)

#10
# There is only 1 confidence interval contained in the population mean, this is what I expect with a 99% CI because it theoretically should yield 1.
