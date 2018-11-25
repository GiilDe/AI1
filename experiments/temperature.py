import numpy as np
from matplotlib import pyplot as plt

X = np.array([400, 450, 900, 390, 550])


alpha = min(X)

//
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

for i in range(len(X)):
    P = []
    for z in T:
        P.append(get_probability(i, z))
    plt.plot(T, P, label=str(X[i]))

plt.xlabel("T")
plt.ylabel("P")
plt.title("Probability as a function of the temperature")
plt.legend()
plt.grid()
plt.show()
exit()
