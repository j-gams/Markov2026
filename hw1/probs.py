### 
import random
import math
import matplotlib.pyplot as plt
import numpy as np

### 1.
### Airplane seat overselling. An airplane has 98 passenger seats. Knowing that passengers miss their flight with
### probability 0.02, the airline overbooks the flight by selling 100 tickets (you can assume that passengers miss their flight
### independently of each other).

### 1a
def p(k, l):
    return (l**k * math.exp(-l)) / math.factorial(k)

poisson100 = p(100, 2)
poisson99 = p(99, 2)

print("1a", poisson100 + poisson99)

### 1b
p100 = math.pow(0.02, 100)
p99 = math.comb(100, 99) * math.pow(0.02, 99) * 0.98
p98 = math.comb(100, 98) * math.pow(0.02, 98) * (0.98 * 0.98)
print("1b:", p100 + p99)

### 1c
print("1c", p98 / (p100 + p99 + p98))

### 2.




### 4. b
### Jill waiting. Jill arrives at a restaurant at 6PM and waits for her three friends Moe, Agnes, and Dorothy. Each one
### of her friends arrives independently at a time uniformly distributed between 6PM and 7PM.

### cdf of T... time when everyone has arrived...

dist = []
for ii in range(10 ** 5):
    m = random.uniform(0, 1) ## moe
    a = random.uniform(0, 1) ## agnes
    d = random.uniform(0, 1) ## dorothy
    final = max(m, a, d)

    ### convert to clockface
    final *= 60
    dist.append(final)

xs = []
samples = []
for i in range(61):
    x = i/60
    xs.append(i)
    ### divide by bin density...
    samples.append(3*x*x / 60)

nph = np.histogram(dist, bins=60)
### need to divide by the number of samples to normalize
nph_b = (nph[0] / len(dist))
plt.bar(np.arange(60), nph_b, label="experimental")
plt.plot(xs, samples, color="orange", label="theoretical")
plt.legend()
plt.title("Problem 4b")
plt.xlabel("minutes waited")
plt.show()