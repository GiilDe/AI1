import numpy as np
from matplotlib import pyplot as plt

X = np.array([400, 450, 900, 390, 550])


alpha = min(X)


def get_sum(t):
    sum = 0
    for x in X:
        sum = sum + pow((x / alpha), (-1 / t))
    return sum


def get_probability(i, t):
    sum = get_sum(t)
    current = X[i]/alpha
    return pow(current, (-1/t))/sum


T = np.linspace(0.01, 5, 100)
#TODO
#TODO check what about print(p) that you deleted
w, h = 100, 5
P = [[0 for x in range(w)] for y in range(h)]
k = 0
for i in range(len(X)):
    m = 0
    for z in T:
        P[k][m] = get_probability(i, z)

    plt.plot(T, P[i], label=str(X[i]))

print(P)
plt.xlabel("T")
plt.ylabel("P")
plt.title("Probability as a function of the temperature")
plt.legend()
plt.grid()
plt.show()


exit()
