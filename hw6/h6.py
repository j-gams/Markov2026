### h6
import numpy as np
import random

import matplotlib.pyplot as plt


### p1

mat = np.array([[0, 1, 0, 0, 0],
                [1/3, 0, 2/3, 0, 0],
                [0, 1/2, 0, 1/2, 0],
                [0, 0, 2/3, 0, 1/3],
                [0, 0, 0, 1, 0]])


mat50 = mat.copy()
for i in range(49):
    mat50 @= mat

print(mat50)

plt.bar(np.arange(5) + 0.1, np.array([1/12, 1/4, 1/3, 1/4, 1/12]) , width=0.2, color="orange", label="theoretical stationary")
plt.bar(np.arange(5) - 0.1, mat50[2].flatten(), width=0.2, label="q50")
#plt.bar(np.arange(5), np.array([1/12, 1/4, 1/3, 1/4, 1/12]) + 0.5, width=0.48, color="orange", label="theoretical stationary")

plt.xlabel("state")
plt.ylabel("probability")
plt.legend()

plt.show()

print("*", sum([1/12, 1/4, 1/3, 1/4, 1/12]))
### p4 simulation

### Simulate at least 10^3 avalanches for a = 0.49 and estimate the probability of extinction by
### calculating the fraction of avalanches that go extinct before 200 generations. Compare this
### probability with what you find in part (a). Hint: You can efficiently simulate the avalanches
### by noting that, given Xn, the number of particles that reproduce is a binomial random variable
### Zn = Binomial(Xn, 1−a), and each reproducing particle produces two particles, so Xn+1 = 2Zn.

a = 0.49
extinct = 0
for j in range(10 ** 3):
    x_n = 1
    for i in range(200):
        z_n = np.random.binomial(x_n, 1-a)
        #print(z_n)
        x_n = 2 * z_n
        if x_n == 0:
            extinct += 1
            break
print("problem ")
print(extinct / (10 ** 3))


### Simulate 103 avalanches and estimate the probability that an avalanche has size X = 3. Compare
### this probability with p3 found in part (b).

### simulate this many particles
### avalanche size S is sum(X_n)
### X_n is the number of particles at step n
### in this binary process we can only get 3 total particles by going 1 -> 2 -> 0
### so if we have survival at step 2, we don't have S = 3
av_3_count = 0
for j in range(10 ** 3):
    ### start at 1
    x_0 = random.random()
    ### 1/2 of time we get 2 offspring
    if x_0 < 0.5: 
        ### now each child is independent, so the probability they each have 0 children is 1/4
        x_1 = random.random()
        if x_1 < 0.25:
            av_3_count += 1
print(av_3_count)
print(av_3_count / (10 ** 3))

### 