import math
import numpy as np
np.set_printoptions(suppress=True)
import scipy.linalg as lin
import random
import matplotlib.pyplot as plt


def norm(vec):
    mag = 0
    for i in range(len(vec)):
        mag += vec[i] ** 2
    mag = math.sqrt(mag)
    return [vec[ii] / mag for ii in range(len(vec))]

def scale(vec):
    return vec / np.sum(vec)

### PROBLEM 2 b

### COMPUTE pi, qi
K = 0.1
a = 0.04
b = 0.16
p2 = np.zeros((5, 5))
comp_p = [0 for ii in range(7)]
comp_q = [0 for ii in range(7)]
for i in range(1, 5):
    comp_p[i] = K * math.exp(a * i)
for i in range(2, 6):
    comp_q[i] = K * math.exp(b * (i - 1))

print(comp_p)
print(comp_q)

### SET values of the transition matrix
#p2[0, 0] = 1 - comp_p[1]
p2[4, 4] = 1 - comp_q[5]

for i in range(4):
    p2[i, i] = 1 - comp_p[i+1] - comp_q[i+1]
    p2[i, i+1] = comp_p[i+1]
    p2[i+1, i] = comp_q[i+2]

print(p2)

### double check.
for i in range(5):
    print(np.sum(p2[i]))

lambdas, us = lin.eig(p2.T)
#l1 = np.argwhere(lambdas==1.0)
### ^ this isn't working, hard code observed position 4
print(lambdas[3])
### normalize: 
print(scale(us[:,3]))

print(scale(us[:,3]) @ p2)

### PROBLEM 2 c

### simulate markov chain:
hits = [0 for ii in range(5)]
### i am going to start at random uniformly over [1, 5]
pos = random.randint(0, 4)
sample = np.arange(5)
for i in range(10 ** 6):
    pos = np.random.choice(sample, p=p2[pos])
    hits[pos] += 1
hits  = [hits[ii] / (10 ** 6) for ii in range(5)]
print(hits)

plt.title('Markov Chain Simulation')
plt.bar(sample + 1, hits, width=0.9)
plt.xlabel("State")
plt.ylabel("Fraction of time in state")
plt.show()



pi_i = [math.exp((((ii ** 2) - ii) / 2) * (a - b)) for ii in range(1, 6)]
pi_i_sum = sum(pi_i)
pi_i = [pi_i[ii] / pi_i_sum for ii in range(5)]
print(pi_i)
 
plt.title('Simulation versus Computed Stationary Distributions')
plt.bar(sample + 1, hits, width=0.3, label='c) simulation')
plt.bar(sample + 1 + 0.3, pi_i, width=0.3, color='orange', label='a) balance condition')
plt.bar(sample + 1 + 0.6, scale(us[:,3]), width=0.3, color='green', label='b) eigenvector')
plt.legend()
plt.xlabel("State")
plt.ylabel("Fraction of time in state")
plt.show()


### PROBLEM 3 c

a3 = 0.99

u1 = [1, 1, 1]
l1 = 1

u2 = [-((2*a3) - 1 + math.sqrt(1 - (3*a3) + 3 * (a3 ** 2)))/(a3-1), (a3 + math.sqrt(1 - (3*a3) + 3 * (a3 ** 2)))/(a3-1), 1]
l2 = - math.sqrt(3 * (a3 ** 2) - (3 * a3) + 1)


u3 = [-((2*a3) - 1 - math.sqrt(1 - (3*a3) + 3 * (a3 ** 2)))/(a3-1), (a3 - math.sqrt(1 - (3*a3) + 3 * (a3 ** 2)))/(a3-1), 1]
l3 = math.sqrt(3 * (a3 ** 2) - (3 * a3) + 1)

print(u1)
print(u2)
print(u3)


print(norm(u1))
print(norm(u2))
print(norm(u3))

print(l1, l2, l3)

p3 = np.array([[1-a3, a3, 0],
               [a3, 0, 1-a3],
               [0, 1-a3, a3]])

littlen = 200

nu2 = norm(u2)
nu3 = norm(u3)

v_stk = np.array([1, 0, 0]) @ np.array([u1, nu2, nu3]).transpose()
print("**", v_stk)
 
for N in [100, 1000, 10000]:
    
    fracs3 = [0 for ii in range(littlen)]
    for i in range(N):
        pos = 0
        for j in range(littlen):
            pos = np.random.choice(np.array([0, 1, 2]), p=p3[pos])
            #fracs3[pos] += 1
            if pos == 0:
                fracs3[j] += 1
    fracs3 = [fracs3[ii] / N for ii in range(littlen)]

    alpha1 = v_stk[1]
    alpha2 = v_stk[2]
    print(alpha1, alpha2)
    fracscomp = [(1/3) + (alpha1 * (l2 ** ii) * nu2[0]) + (alpha2 * (l3 ** ii) * nu3[0]) for ii in range(littlen)]
    plt.plot(np.arange(littlen) + 1, fracs3, label="simulated")
    plt.plot(np.arange(littlen) + 1, fracscomp, color="orange", label="theoretical")
    plt.xlabel("Number of timesteps")
    plt.ylabel("Fraction of time in state 1")
    plt.title("N=" + str(N))
    plt.legend()
    plt.show()

