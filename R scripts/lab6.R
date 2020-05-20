# Name: Kyle Strokes
# Date: 2/20/19
# ISTA 116 Section C || Jacob Heller
# Lab Assignment 6
# Collaborator: Elaine Mancillas

#1
suits <- c("Spade", "Heart", "Diamond", "Club")
ranks <- c("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
suits
ranks

#2
combos <- expand.grid(Suit=suits, Rank=ranks)
combos

#3
combo_probs <- prop.table(table(combos))
prob_of_spade <- rowSums(combo_probs)
prob_of_spade
prob_of_ace <- colSums(combo_probs)
prob_of_ace
prob_of_ace_spades <- combo_probs["Spade", "Ace"]
prob_of_ace_spades
# The probability of drawing a Spade = 25%, for an Ace = 7.6%, for the Ace of Spades = 1.9%

#4
random_nums <- sample(1:52, 10, replace = FALSE)
cards <- combos[random_nums,]
cards

#5
after <- combos[-(random_nums),]
new_probs <- prop.table(table(after))
prob_of_spade <- rowSums(new_probs)
prob_of_spade
prob_of_ace <- colSums(new_probs)
prob_of_ace
prob_of_ace_spades <- new_probs["Spade", "Ace"]
prob_of_ace_spades
# The numbers are different because 10 cards have been pulled, adjusting probabilities

#6
sequence <- 1:6
three_rolls <- expand.grid(first=sequence, second=sequence, thrid=sequence)
three_rolls

#7
three_rolls$sum = rowSums(three_rolls)
three_rolls

#8
dice_sums <- barplot(table(three_rolls$sum))
dice_sums
# The sums of 10 and 11 are the most common among 3 dice

#9
sim <- replicate(1000, {
  result = sample(1:6, 3, replace = TRUE);
  sum = sum(result)})
freq <- barplot(table(sim))
freq
# You can see that simulation is similar to the expected distribution. 11 was the most frequent and there is a bell curve just like the expected.

#10
simulate <- replicate(1000, {
  samp = sample(1:6, 5, replace = TRUE) ;
  sorted = sort(samp, decreasing = TRUE) ;
  top3 = sum(sorted[1:3])})
graph <- barplot(table(simulate))
graph
# The graph of the top 3 highest die rolls from 5 is skewed left more than just rolling 3 die and summing them up because you have more oppourtunity to get a higher number to boost the sum.