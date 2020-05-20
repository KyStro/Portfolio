
'''
Tests for ISTA 311 Programming HW 1.
Requires scipy, matplotlib.

Runs 3 tests on each of simulate() and set_prob(), 2 tests on each of and_prob(), or_prob(), normalize().
Produces 3 graphs for the results of simulate().

Author: Dylan Murphy
'''

import random
import math
import scipy as sp
from scipy import stats             # We use chi-square goodness-of-fit tests to check that 
import matplotlib.pyplot as plt

plot_tests = True

###############################
# Test Suite
###############################

##  Test Distributions

# Uniform distribution test: Rolling a 10-sided die

unif_dist = {1: 1/10,
             2: 1/10,
             3: 1/10,
             4: 1/10,
             5: 1/10,
             6: 1/10,
             7: 1/10,
             8: 1/10,
             9: 1/10,
             10: 1/10}

# Non-uniform, three options: drawing a colored ball from an urn

rgb =  {"red": 3/18,
        "green": 7/18,
        "blue": 8/18}

# Benford's law distribution for digits 1-9

benford = {1: 0.301,
           2: 0.176,
           3: 0.125,
           4: 0.097,
           5: 0.079,
           6: 0.067,
           7: 0.058,
           8: 0.051,
           9: 0.046}

benford_set_a = {2, 8, 9}
benford_set_b = {1, 3, 7, 8, 9}

# RGB urn problem, but given in terms of natural frequencies

rgb_unscaled = {"red": 3,
                "green": 7,
                "blue": 8}

letters = {"a": 0.0575,
           "b": 0.0128,
           "c": 0.0263,
           "d": 0.0285,
           "e": 0.0913,
           "f": 0.0173,
           "g": 0.0133,
           "h": 0.0313,
           "i": 0.0599,
           "j": 0.0006,
           "k": 0.0084,
           "l": 0.0335,
           "m": 0.0235,
           "n": 0.0596,
           "o": 0.0689,
           "p": 0.0192,
           "q": 0.0008,
           "r": 0.0508,
           "s": 0.0567,
           "t": 0.0706,
           "u": 0.0334,
           "v": 0.0069,
           "w": 0.0119,
           "x": 0.0073,
           "y": 0.0164,
           "z": 0.0006,
           " ": 0.1927}


letters_unscaled = {"a": 575,
                    "b": 128,
                    "c": 263,
                    "d": 285,
                    "e": 913,
                    "f": 173,
                    "g": 133,
                    "h": 313,
                    "i": 599,
                    "j": 6,
                    "k": 84,
                    "l": 335,
                    "m": 235,
                    "n": 596,
                    "o": 689,
                    "p": 192,
                    "q": 8,
                    "r": 508,
                    "s": 567,
                    "t": 706,
                    "u": 334,
                    "v": 69,
                    "w": 119,
                    "x": 73,
                    "y": 164,
                    "z": 6,
                    " ": 1927}

letter_set_a = {'a', 'b', 'c', 'd', 'e'}
letter_set_b = {'b', 'd', 'n', 't', 'x'}

## Testing the set probability

def test_prob(probfunc):
    unif_set = {1, 5, 7, 8}
    rgb_set = {"red", "green"}
    passed_count = 0

    print("Test 1: Uniform distribution on integers 1-10.\nTest set: {1, 5, 7, 8}\nExpected result: 0.4")
    result = probfunc(unif_dist, unif_set)
    print("Result:", result)
    if math.isclose(0.4, result):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")

    print("Test 2: Drawing from an urn with 3 red, 7 green, 8 blue balls.\nTest set: {\"red\", \"green\"}\nExpected result: 10/18")
    result = probfunc(rgb, rgb_set)
    print("Result:", result)
    if math.isclose(10/18, result):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")

    print("Test 3: Benford's law on digits 1-9.\nTest set: {2, 8, 9}\nExpected result: 0.273")
    result = probfunc(benford, benford_set_a)
    print("Result:", result)
    if math.isclose(0.273, result):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")

    '''
    if setbonus:
        print("Test 4: Union of two sets using Benford's law.\nTest sets: {2, 8, 9}, {1, 2, 7, 8}\nExpected result: .632")
        result = probfunc(benford, benford_set_a, benford_set_b)
        print("Result:", result)
        if math.isclose(0.632, result):
            print("Test PASSED")
        else:
            print("Test FAILED")
    '''
    return passed_count

## Testing union and intersection

def test_op(andfunc, orfunc):
    passed_count = 0

    print("Test 1: Benford's law on digits 1-9.\nTest sets: {2, 8, 9}, {1, 3, 7, 8, 9}")
    andresult = andfunc(benford, benford_set_a, benford_set_b)
    orresult = orfunc(benford, benford_set_a, benford_set_b)
    print("Expected result (and/intersection): 0.097\nResult:", andresult)
    print("Expected result (or/union): 0.757\nResult:", orresult)
    if math.isclose(andresult, 0.097) and math.isclose(orresult, 0.757):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    
    print("Test 2: Letters in English text.\nTest sets: {a, b, c, d, e}, {b, d, n, t, x}")
    andresult = andfunc(letters, letter_set_a, letter_set_b)
    orresult = orfunc(letters, letter_set_a, letter_set_b)
    print("Expected result (and/intersection): 0.0413\nResult:", andresult)
    print("Expected result (or/union): 0.3539\nResult:", orresult)
    if math.isclose(andresult, .0413) and math.isclose(orresult, .3539):
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    return passed_count

## Testing normalization

def test_norm(normfunc):
    passed_count = 0

    print("Test 1: letter frequencies in English text")
    temp_dic = letters_unscaled.copy()
    comp1.normalize(temp_dic)
    passed = True
    for key in letters:
        if not math.isclose(letters[key], temp_dic[key]):
            passed = False
            print("Probability of", key, temp_dic[key], "does not match expected probability", letters[key])
    if passed:
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    print("Test 2: drawing from an urn")
    temp_dic = rgb_unscaled.copy()
    comp1.normalize(temp_dic)
    passed = True
    for key in rgb:
        if not math.isclose(rgb[key], temp_dic[key]):
            passed = False
            print("Probability of", key, temp_dic[key], "does not match expected probability", letters[key])
    if passed:
        print("Test PASSED")
        passed_count += 1
    else:
        print("Test FAILED")
    return passed_count

## Testing the simulation
# Uses a chi-square goodness-of-fit test.

def test_sim(simfunc):
    passed_count = 0

    print("Test 1: Uniform distribution")
    result = sp.zeros(10)
    for i in range(10000):
        out = simfunc(unif_dist)
        result[out-1] += 1
    csr = sp.stats.chisquare(result, 1000 * sp.ones(10))
    print("Observed frequencies:", result)
    print("Expected frequencies:", 1000 * sp.ones(10))
    print("Chi-square statistic:", csr.statistic)
    print("p-value: ", csr.pvalue)
    if csr.pvalue < 0.01:
        print("Test FAILED")
    else:
        print("Test PASSED")
        passed_count += 1

    if plot_tests:
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x = 1 + sp.arange(10), height=result, tick_label = 1 + sp.arange(10))
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x = 1 + sp.arange(10), height=0.1*sp.ones(10), tick_label = 1 + sp.arange(10))
        plt.savefig("uniform.png")

    print("Test 2: Drawing from an urn")
    result = sp.zeros(3)
    picks = []
    for i in range(10000):
        picks.append(simfunc(rgb))
    result[0] = sum([pick == "red" for pick in picks])
    result[1] = sum([pick == "green" for pick in picks])
    result[2] = sum([pick == "blue" for pick in picks])
    csr = sp.stats.chisquare(result, (10000/18) * sp.array([3,7,8]))
    print("Observed frequencies:", result)
    print("Expected frequencies:", (10000/18) * sp.array([3,7,8]))
    print("Chi-square statistic:", csr.statistic)
    print("p-value: ", csr.pvalue)
    if csr.pvalue < 0.01:
        print("Test FAILED")
    else:
        print("Test PASSED")
        passed_count += 1

    if plot_tests:
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x = sp.arange(3), height=result, tick_label = ["red", "green", "blue"])
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x = sp.arange(3), height=(1/18)*sp.array([3,7,8]), tick_label = ["red", "green", "blue"])
        plt.savefig("urn.png")

    print("Test 3: Benford's law")
    result = sp.zeros(9)
    for i in range(10000):
        out = simfunc(benford)
        result[out-1] += 1
    csr = sp.stats.chisquare(result, 10000 * sp.array([0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]))
    print("Observed frequencies:", result)
    print("Expected frequencies:", 10000 * sp.array([0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]))
    print("Chi-square statistic:", csr.statistic)
    print("p-value: ", csr.pvalue)
    if csr.pvalue < 0.01:
        print("Test FAILED")
    else:
        print("Test PASSED")
        passed_count += 1

    if plot_tests:
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x = 1 + sp.arange(9), height=result / 10000, tick_label = 1 + sp.arange(9))
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x = 1 + sp.arange(9), height=sp.array([0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]), tick_label = 1 + sp.arange(9))
        plt.savefig("benford.png")

    '''
    if simbonus:
        print("Test 4: Drawing from an urn, with a non-normalized distribution")
        result = sp.zeros(3)
        picks = []
        for i in range(10000):
            picks.append(simfunc(rgb_unscaled))
        result[0] = sum([pick == "red" for pick in picks])
        result[1] = sum([pick == "green" for pick in picks])
        result[2] = sum([pick == "blue" for pick in picks])
        csr = sp.stats.chisquare(result, (10000/18) * sp.array([3,7,8]))
        print("Observed frequencies:", result)
        print("Expected frequencies:", (10000/18) * sp.array([3,7,8]))
        print("Chi-square statistic:", csr.statistic)
        print("p-value: ", csr.pvalue)
        if csr.pvalue < 0.01:
            print("Test FAILED")
        else:
            print("Test PASSED")

        plt.figure()
        plt.subplot(2, 1, 1)
        plt.bar(x=sp.arange(3), height=result, tick_label = ["red", "green", "blue"])
        plt.title("Uniform distribution: observed (top) vs. expected (bottom)")
        plt.subplot(2, 1, 2)
        plt.bar(x=sp.arange(3), height=(1/18)*sp.array([3,7,8]), tick_label = ["red", "green", "blue"])
        plt.savefig("urnbonus.png")
    '''

    return passed_count

import comp1

def main():

    '''
    setbonus_choice = input("Test bonus functionality for set probability? (y/N) ")

    if setbonus_choice == "y":
        setbonus = True
    else:
        setbonus = False
    
    simbonus_choice = input("Test bonus functionality for simulation? (y/N) ")
    
    if simbonus_choice == "y":
        simbonus = True
    else:
        simbonus = False
    '''

    passed_count = 0

    input("Press Enter to begin set probability test.")
    passed_count += test_prob(comp1.set_prob)
    input("Press Enter to test and/or calculation.")
    passed_count += test_op(comp1.and_prob, comp1.or_prob)
    
    input("Press Enter to test normalization.")
    passed_count += test_norm(comp1.normalize)

    input("Press Enter to begin simulation test.\nNote: There is approximately a 1% chance that a correct algorithm will fail each test.\nIf your code fails consistently, it is probably incorrect; check the plots.")
    passed_count += test_sim(comp1.simulate)

    print("Overall result: ran 10 tests, passed", passed_count)
    return None

if __name__ == "__main__":
    main()
