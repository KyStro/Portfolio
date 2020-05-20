'''
Kyle Strokes
Computational Homework 1
2/4/19
'''
import random

def set_prob(dictionary, collection):
    total_probability = 0.0
    for element in collection:
        total_probability += dictionary[element]
    return total_probability

def and_prob(dictionary, collection1, collection2):
    total = 0.0
    for element in collection1 & collection2:
        total += dictionary[element]
    return total

def or_prob(dictionary, collection1, collection2):
    total = 0.0
    for element in collection1 | collection2:
        total += dictionary[element]
    return total

def simulate(dictionary):
    num = random.random()

    vals_keys = []
    for key in dictionary.keys():
        vals_keys.append((dictionary[key], key))
    low = 0
    high = 0
    for val in sorted(vals_keys):
        high += val[0]
        if num >= low and num < high:
            return val[1]
        else:
            low = high

def normalize(dictionary):
    old_total = sum(dictionary.values())
    factor = 1 / old_total
    for key in dictionary.keys():
        dictionary[key] = dictionary[key] * factor