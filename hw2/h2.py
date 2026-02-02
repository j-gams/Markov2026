import matplotlib.pyplot as plt

import numpy as np
import math
import random
import scipy
import time
### 1d
### implement a code to generate samples from X for γ = 4 and x0 = 10. Generate N = 100, 1000, and
### 10000 samples from X and plot histograms of the samples together with the theoretical distribution.
### Normalize your histograms so that they have area 1, and set the horizontal plot range to be [0, 60].

"""def f_inv(u):
    return math.pow(1-u, -1/3) * 10 ### gamma = 4, x0 = 10

def sample_X():
    u = random.random() ### random float in [0, 1)
    return f_inv(u)

samples = [np.zeros(100), np.zeros(1000), np.zeros(10000)]
theoretical = [3 * math.pow(10, 3) * math.pow(ii, -4) for ii in range(10, 61)] 

for i in range(100):
    samples[0][i] = sample_X()

for i in range(1000):
    samples[1][i] = sample_X()

for i in range(10000):
    samples[2][i] = sample_X()


for i in range(3):
    #nph = np.histogram(samples[i], bins=60)
    #nph_b = (nph[0] / len(samples[i])) ### normalize
    #print(len(nph[0]), len(nph[1]))
    plt.hist(samples[i], bins=60, density=True, range=(0,60), label="sampled")##bar(nph[1], nph_b, label="experimental")
    plt.plot(np.arange(10, 61), theoretical, color="orange", label="theoretical")
    plt.xlabel("Sampled value of X")
    plt.ylabel("Experimental Frequency")
    plt.title("N = " + str(len(samples[i])))
    plt.legend()
    plt.show()"""

### 2b
def f(x):
    return x * math.exp(-x)

data = []

### time code
inittime = time.time()
for i in range(10 ** 6):
    u = random.random()
    x_root = scipy.optimize.root(f, u)
    if x_root.x < 0:
        print("uh oh")
    #data.append(x_root.x)

print("2b) time taken to find roots:", time.time() - inittime)

### 2c

def g_inv(u):
    return -2 * math.log(2*u)


inittime = time.time()
while(len(data) < 10 ** 6):
    u = random.random()
    scipyx = scipy.stats.expon.rvs(scale=1, size=1)
    comp = (math.e * scipyx)
    if u <= comp:
        data.append(scipyx)

print("2c) time taken to accept 10^6 samples:", time.time() - inittime)
    

    

inittime = time.time()
data = []
for i in range(10 ** 6):
    data.append(scipy.stats.expon.rvs(scale=1, size=1) + scipy.stats.expon.rvs(scale=1, size=1))
print("2d) time taken to compute 10^6 samples:", time.time() - inittime)