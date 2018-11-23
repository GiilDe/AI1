import numpy as np
from matplotlib import pyplot as plt

X = np.array([400, 450, 900, 390, 550])

# TODO: Write the code as explained in the instructions

T_vals = np.linspace(0.01, 5, 100)

print(P)


def get_probability(i_, T):
    min_x = min(X)
    sum_ = 0
    for x in X:
        sum_ += (x / min_x) ^ (-1/T)
    return (X[i_] ^ (-1/T))/sum_


for i in range(len(X)):
    plt.plot(T, P[:, i], label=str(X[i]))

plt.xlabel("T")
plt.ylabel("P")
plt.title("Probability as a function of the temperature")
plt.legend()
plt.grid()
plt.show()
exit()
