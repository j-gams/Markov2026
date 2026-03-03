### homework 4

import math
import numpy as np
np.set_printoptions(suppress=True)
import scipy.linalg as lin
import random


### problem 1

q = 0.4
p = 0.35
s = 0.25
moneysum = 0
nsims = 100000
for i in range(nsims):
    state = 10
    while(True):
        sample = random.random()
        if sample < q:
            state -= 1
        elif sample < p+q:
            state += 1
        else:
            ### retire
            moneysum += state
            break
        if state == 0:
            break

print("problem 1c: expected money at end of game:")
print(moneysum / nsims)


### problem 2a

coffeep = 0.9
t2 = np.zeros((6, 6), dtype=float)
t2[0, 5] = 1
for i in range(1, 6):
    for j in range(i+1):
        t2[i, j] = math.comb(i, j) * (coffeep ** j) * ((1-coffeep) ** (i-j))
        print(i, j, (coffeep ** j) * ((1-coffeep) ** (i-j)))

print(t2)

for i in range(6):
    print(sum(t2[i]))

### problem 2b

ei = [0 for ii in range(6)]

for i in range(1, 6):
    ### compute ei
    #temp = 
    ei[i] = (sum([ei[jj]*t2[i, jj] for jj in range(1, i)]) + 1) / (1 - t2[i, i])
print(ei)

### problem 2c

solvearr = t2.copy()
for i in range(len(t2)):
    solvearr[i, i] = solvearr[i, i] - 1

#solvearr[0, 0] = (t2[5, 0] / (1 - t2[5, 5]))
consts = np.ones(6)
consts[5] = 1
solvearr = solvearr.transpose() + 1
#for i in range(6):
#    solvearr[5, i] = 1
#solvearr = np.vstack([solvearr, np.ones((1, 6))])
print(solvearr)
res = np.linalg.solve(solvearr, consts)
print(res)

print(res @ t2)