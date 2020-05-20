# Name: Kyle Strokes
# Date: 2/27/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 7
# Collaborator: Elaine Mancillas

#1
data_frame <- data.frame(num = 1:6, score = c(100, 0, 0, 0, 50, 0), prob = rep(1/6, 6))
data_frame

#2
sample_rolls <- sample(data_frame$score, size = 10000, prob = data_frame$prob, replace = TRUE)
sample_rolls_hist <- hist(sample_rolls)
sample_rolls_hist
# The shape shows that a score of 0 is about 4 times more likely to occur than a 50 or 100. The possible scores are 0, 50, 100. A 0 occurs about 6,800 times, 50 and 100 occur 1,900 times respectfully.

#3
mean_sample <- mean(sample_rolls)
mean_sample
data_frame$expected = data_frame$score * data_frame$prob
total_expected = sum(data_frame$expected)
total_expected
# The sample mean and the excepted value of the random variable are similar because of the law of the large numbers says when probabilities are repeated many times they will approach the expected value. 24.24 and 25.

#4
sd_sample = sd(sample_rolls)
sd_sample
sd_expected <- sqrt(sum((data_frame$score - total_expected)^2 * data_frame$prob))
sd_expected
# The expected standard deviation is similar but different from the sample stand deviation because it was a random sample

#5
loaded_frame <- data.frame(num = 1:6, score = c(100, 0, 0, 0, 50, 0), prob = c(5/50,5/50,5/50,5/50,0.5,5/50))
loaded_frame

#6
loaded_rolls <- sample(loaded_frame$score, size = 10000, prob = loaded_frame$prob, replace = TRUE)
loaded_rolls_hist <- hist(loaded_rolls)
loaded_rolls_hist
# The shape shows that a score of 0 and 50 are most frequent. The score available are 0, 50, 100. 50 is the most common about 5000 times, 0 had 4000, and 0 had 1000 occurances.

#7
loaded_mean <- mean(loaded_rolls)
loaded_mean
loaded_frame$expected = loaded_frame$score * loaded_frame$prob
total_loaded_expect <- sum(loaded_frame$expected)
total_loaded_expect - total_expected
# You are expected to score 10 more points on average with a loaded die

#8
sample_both <- replicate(10000, {s = sample(date_frame$score, size = 1, prob = data_frame$prob, replace = TRUE) ; s2 = sample(loaded_frame$score, size = 1, prob = loaded_frame$prob, replace = TRUE) ; sum = s+s2})
sample_both
sample_both_hist <- hist(sample_both)
sample_both_hist
# There are now values 150 and 200 available to be scored, though they are lower than a 0, 50, and 100. 50 has surpassed 0 as the most common roll by alot more than the loaded die

#9
mean_both <- mean(sample_both)
mean_both
expected_both <- total_expected + total_loaded_expect
expected_both
# You are rolling a normal dice with 1/3 probability of scoring and a loaded die with a 0.6 chance of scoring. These produce higher numbers skewing the mean.

#10
sample_all <- replicate(10000, {sam = sample(data_frame$score, size = 2, prob = data_frame$prob, replace = TRUE) ; sam2 = sample(loaded_frame$score, size = 3, prob = loaded_frame$prob, replace = TRUE) ; total = (sum(sam) + sum(sam2))/5})
sample_all
all_mean <- mean(sample_all)
all_mean
net_gamefair <- total_expected - 5
net_gameloaded <- total_loaded_expect - 15
net_5die <- (total_expected * 2 + total_loaded_expect * 3)/5 - 10
net_gamefair
net_gameloaded
net_5die
# You should play the 5 die game because the expected net point you should have is 21; compared to 20 from the fair and loaded die games.