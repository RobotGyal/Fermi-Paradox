from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1000 # num of locations to place civilations
MAX_CIVS = 5000 # max num of advanced civilations
TRIALS = 1000 # num of times to model a given number of civilations
CIV_STEP_SIZE = 100 # civilations count step size

x = []
y = []

for num_civs in range(2, MAX_CIVS + 2, CIV_STEP_SIZE):
    civs_per_vol = num_civs / MAX_CIVS
    num_single_civs = 0
    for trial in range(TRIALS):
        locations = []
        while len(locations) < num_civs:
            location = randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)
        overlap_count = Counter(locations)
        overlap_rollup = Counter(overlap_count.values())
        num_single_civs += overlap_rollup[1]

    prob = 1 - (num_single_civs / (num_civs * TRIALS))

    print("{:.4f}   {:.4f}".format(civs_per_vol, prob))
    x.append(civs_per_vol)
    y.append(prob)