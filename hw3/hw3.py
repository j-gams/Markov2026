### Markov - hw3.py
import numpy as np
import matplotlib.pyplot as plt
import math


def matrixpow(M, p):
    result = np.copy(M)
    for i in range(p-1):
        result @= M
    return result


### problem 1

def f_of_x(x):
    e_x = np.exp(-x)
    t1 = (x * (x+1))/3

    return t1 * e_x

def cagax(x):
    astar = math.sqrt(3) / 1
    castar = (1/(42 - (24 * math.sqrt(3)))) * math.exp(1-math.sqrt(3))
    e_x = np.exp(-astar * x)
    t1 = (astar ** 2) * x 

    return castar * t1 * e_x
    

x_samples = np.arange(200) / 4

plt.plot(x_samples, f_of_x(x_samples), label="f(x)")
plt.plot(x_samples, cagax(x_samples), color="orange", label="c(a*)g_a*(x)")
plt.xlabel("x")
plt.legend()
plt.show()

### problem 2
p1_transition = np.array([[0.9, 0.1,    0],
                          [0,   7/8,    1/8],
                          [0.4, 0,      0.6]])

print("** problem 2e")
print(matrixpow(p1_transition, 50))

states = np.arange(3)
inst_1 = [0, 0, 0]
pos = 0
for t in range(10000):
    pos = np.random.choice(states, p=p1_transition[pos,:])
    inst_1[pos] += 1
print("** problem 2f")
print([inst_1[ii] / 10000 for ii in range(3)] )


### problem 3

p3_transition = np.array([[1,   0,      0,      0,      0],
                          [1/3, 0,      2/3,    0,      0],
                          [0,   1/3,    0,      2/3,    0],
                          [0,   0,      1/3,    0,    2/3],
                          [0,   0,      0,      0,      1]])

print("** problem 3c")
print(matrixpow(p3_transition, 4))

### problem 4

p4_transition = np.array([[0.5, 0.5,    0,      0,      0,      0],
                          [0,   0.5,    0.5,    0,      0,      0],
                          [1/3, 0,      1/3,    1/3,    0,      0],
                          [0,   0,      0,      0.5,    0.5,    0],
                          [0,   0,      0,      0,      0,      1],
                          [0,   0,      0,      0,      1,      0]])

### part b: P[X5 = 4 | X0 = 1]
print("** problem 4b")
print(matrixpow(p4_transition, 5))

### part c: simulate markov chain starting at X0 = 1 for 5 time steps 10000 times.

### note - these states are offset by 1 to account for 0-indexing.
states = np.arange(6)
freq_4 = 0
for sim in range(10000):
    pos = 0
    for t in range(5):
        pos = np.random.choice(states, p=p4_transition[pos,:])
    ### this is position 4, but 0-indexed
    if pos == 3:
        freq_4 += 1
print("** problem 4c")
print(freq_4 / 10000)
