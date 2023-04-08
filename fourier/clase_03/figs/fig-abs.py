#!/usr/bin/env python3

# import matplotlib
# import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('../../../utils/clases.mplstyle')

def f(x):
    return np.absolute(x)

def F(x, n):
    resultado = np.zeros(x.size)
    for i in range(0, n + 1):
        resultado += np.cos((2 * i + 1) * x) / (2 * i + 1)**2
    return np.pi / 2 - 4/np.pi * resultado

fig, ax = plt.subplots()
plt.axhline(color="gray")
plt.axvline(color="gray")
x = np.linspace(-np.pi, np.pi, 200)
plt.plot(x, f(x), lw=3)
#for n in [0, 1]:
for n in [2, 3]:
# for n in [3]:
    lab = f"$\sum_{{n = 0}}^{{{str(n)}}}$"
    plt.plot(x, F(x, n), label=lab)
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_xticklabels(['$\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'])
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.tight_layout()
plt.savefig("abs-23.pdf")


