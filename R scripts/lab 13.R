# Name: Kyle Strokes
# Date: 4/17/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 13
# Collaborator: Elaine Mancillas

#1
download.file("http://www.openintro.org/stat/data/atheism.RData", destfile = "atheism.RData")
load("atheism.RData")

#2
us_only <- subset(atheism, nationality == "United States")
atheism.us <- table(us_only$response, us_only$year)

#3
prop.atheism.us <- prop.table(atheism.us, margin = 2)
prop.atheism.us["atheist", "2012"]
# This agrees with the table 6 answer of 0.05 because the prop table gives 0.049

#4
atheism_2012_us <- atheism.us[,"2012"]
ci_2012_atheism <- prop.test(as.table(atheism_2012_us), p = 0.13)
#Confidence interval is 0.0376 - 0.0657

#5
ci_2012_atheism <- prop.test(as.table(atheism_2012_us), p = 0.13)
# The percent of atheist in the US is different from 13%, p value is very low.

#6
us_2005v2012 <- prop.test(as.table(atheism.us), alternative = "less")
# No the p-value is very low so we reject the null hypothesis, the proportion of atheist in 2005 is less than 2012.

#7
n <- 1000
p <- seq(0, 1, 0.01)

#8
plot(p, sqrt((p*(1-p))/ n))
# You would get the largest confidence interval with the highest standard error. p = 0.5 will give use the largest of both

#9
atheism.spain <- subset(atheism, nationality == "Spain")
table.spain <- table(atheism.spain$response, atheism.spain$year)
prop.test(as.table(table.spain))
# we cannot reject the null hypothesis because p value is 0.4375

#10
atheism.2012 <- subset(atheism, year = "2012")
atheism.2012 <- table(atheism.2012$nationality, atheism.2012$response)
atheism.2012.new <- atheism.2012[c("Colombia", "Brazil"),]
prop.test(as.table(atheism.2012.new), alternative = "greater")
# The p-value is very small so the proportion of atheists in Colombia was greater than Brazil