# hw 7

import math
import matplotlib.pyplot as plt
import numpy as np
import random

### 1a - numerical estimation:
l_a = 2
l_b = 1.5
xb_sum = 0 ### this is going to be a running total of p(x_b < a) for quicker computation...?
result = 0
for i in range(1, 100):
    xb_sum += ((l_b ** (i-1)) * math.exp(-l_b))/math.factorial(i-1) ### update sub for p(x_b < a)
    #print("xb", xb_sum)
    xa = ((l_a ** (i)) * math.exp(-l_a))/math.factorial(i) ### compute p(x_a = a)
    result += xa
    #print("xa", xa)

print("estimation", result)

### 1b - numerical estimation:
l_a = 1/45
l_b = 1/60

timeresult = []
for t in range(91):
    result = 0
    for k in range(100):
        result += ((((l_a * (90-t)) ** k) * (math.exp(-(l_a * (90-t)))))/(math.factorial(k))) * ((((l_b * (90-t)) ** k) * (math.exp(-(l_b * (90-t)))))/(math.factorial(k)))
    timeresult.append(result)

plt.plot([ii for ii in range(91)], timeresult)
plt.xlabel("Game time")
plt.ylabel("Probability of game ending in tie")
plt.show()


### 1c - numerical estimation:
l_a = 1/45
l_b = 1/60

for t in range(60, 91):
    result = 0
    for k in range(100):
        result += ((((l_a * (90-t)) ** k) * (math.exp(-(l_a * (90-t)))))/(math.factorial(k))) * ((((l_b * (90-t)) ** (k+1)) * (math.exp(-(l_b * (90-t)))))/(math.factorial(k+1)))
    timeresult[t] = result

plt.plot([ii for ii in range(91)], timeresult)
plt.xlabel("Game time")
plt.ylabel("Probability of game ending in tie")
plt.show()


### 2c
maxt = 48
### idea...sample interarrival times and add 2 until we go past 48 mins
### with lambda = 3/min... 1/3... we need to sample 48*3 times on average. Add extra 20 for buffer
lam = 1/3
sampleA = np.random.exponential(3, (48*3 + 20,))
sAsum = [sampleA[0]]
sApts = 0
for i in range(1, len(sampleA)):
    sAsum.append(sampleA[i] + sAsum[i-1])
    sApts += 2
    if sAsum[i] + sampleA[i+1] > 48:
        break

sampleB = np.random.exponential(3, (48*3 + 20,))
sBsum = [sampleB[0]]
sBpts = 0
for i in range(1, len(sampleB)):
    sBsum.append(sampleB[i] + sBsum[i-1])
    sBpts += 2
    if sBsum[i] + sampleB[i+1] > 48:
        break

print(sApts, sBpts)
plt.vlines(sAsum, 0, 2, colors='r', linewidth=0.5, label="team A scores")
plt.vlines(sBsum, 0, 2, colors='b', linewidth=0.5, label="team B scores")

plt.title("Scoring times within game")
plt.xlabel("Time (minutes)")
plt.ylabel("")
plt.show()

### 2d
sample2 = np.random.exponential(3/2, (48*6 + 40,))
sAsum = []
sBsum = []
timect = 0
sApts = 0
sBpts = 0
for i in range(len(sample2)):
    timect += sample2[i]
    u = random.random()
    if u < 0.5:
        ### wp 1/2, this is a team-A score
        sAsum.append(timect)
        sApts += 2
    else:
        sBsum.append(timect)
        sBpts += 2
    if timect + sample2[i+1] > 48:
        break

print(sApts, sBpts)
plt.vlines(sAsum, 0, 2, colors='r', linewidth=0.5, label="team A scores")
plt.vlines(sBsum, 0, 2, colors='b', linewidth=0.5, label="team B scores")

plt.title("Scoring times within game")
plt.xlabel("Time (minutes)")
plt.ylabel("")
plt.show()

### 2e
dt = []
for i in range(10**5):
    n = np.random.poisson((2/3)*48)
    na = np.random.binomial(n, 0.5)
    dt.append(2*(2*na - n))

print("expectation:", np.mean(dt))
print("variance:", np.var(dt))
print("prob D(t) = 0:", len(np.where(np.array(dt) == 0)[0])/(10**5))


### 3a
tsum = 0
ptlist = []
result = []
while(tsum < 120):
    sample = np.random.poisson(1/8.5)
    if tsum + sample < 120:
        tsum += sample
        ptlist.append(tsum)
    else:
        break

for i in range(len(ptlist)):
    u = random.random()
    if u < (0.5 * (1  + (ptlist[i] ** 2)/900)) / (8.5):
        result.append(ptlist[i])

print(len(result))
plt.hist(result, bins=120)
plt.xlabel("Day")
plt.ylabel("Cases Reported")
plt.show()