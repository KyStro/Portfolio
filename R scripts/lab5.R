# Name: Kyle Strokes
# Date: 2/13/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 5
# Collaborator: Elaine Mancillas

download.file("http://www.openintro.org/stat/data/kobe.RData", destfile = "kobe.RData")
load("kobe.RData")

#1
kobe.basket.prob <- prop.table(table(kobe$basket))
kobe.basket.prob

#2
kobe.basket.prob[1]

#3
first.13.shots <- kobe$basket[1:13]
first.13.shots
calc_streak(first.13.shots)
# It calculates how many hits Kobe has in a row if he misses, there is a 0 each time and the streak restarts when he has a hit

#4
streak.graph <- barplot(table(calc_streak(kobe$basket)))

#5
sample.kobe <- sample(c("H", "M"), size = nrow(kobe),prob = kobe.basket.prob, replace = TRUE)

#6
prop.table(table(sample.kobe))
# The probability of the sample with the real life data is similar. The sample was 1% higher to get a hit. It should be similar because we use his probability of making the shot in a sample that is independent from shot to shot, excluding "hotstreaks" or "coldstreaks"

#7
sample.streak <- calc_streak(sample.kobe)
sample.streak.graph <- barplot(table(sample.streak))
# The barplots are almost identical, the sample was able to make some 5 hit streaks, while Kobe was not

#8
streak.probs <- prop.table(table(calc_streak(kobe$basket)))
sample.streak.probs <- prop.table(table(sample.streak))
streak.probs
sample.streak.probs
# The sample seemed to have similar miss rate, lower single hit, higher two hits in a row, lower 3 in a row, similar 4 in a row and it made a 5 hits in a row while Kobe did not.

#9
summary(replicate(100, 
          {s = sample(c("H", "M"), size = nrow(kobe),prob = kobe.basket.prob, replace = TRUE);
          s.streak <- calc_streak(s);
          probs = prop.table(table(s.streak));
          prob.of.miss <- probs["0"]}))
# It is a little atypical because the iterations of the samples show that the probability of a miss is about 56% for both mean and median while Kobe actually averaged 51% for misses.

#10
summary(replicate(100, 
                  {s = sample(c("H", "M"), size = nrow(kobe),prob = kobe.basket.prob, replace = TRUE);
                  s.streak <- calc_streak(s);
                  probs = prop.table(table(s.streak));
                  prob.of.miss <- probs["3"]}))
# It seems that Kobe is able to get 3 hits in a row more often than the sample distribution, but other streaks (2 and 4) a little lower percent than the sample. 
