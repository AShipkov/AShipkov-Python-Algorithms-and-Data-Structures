import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(100, 1000, 250)
y1 = 10**(-7)*x**3+7.7*10**(-4)*x**2-.06*x+5.08
y2 = .2*10**(-7)*x**3+.19*10**(-4)*x**2+5.2*10**(-3)-.2789
y3 = -10**(-8)*x**3+1.5*10**(-4)*x**2+0.318*x+3.13

fig, ax = plt.subplots()
ax.plot(x, y1, color="blue", label="1 вариант")
ax.plot(x, y2, color="red", label="2 авариант")
ax.plot(x, y3, color="green", label="3 вариант")
ax.set_xlabel("количество кратных делителей")
ax.set_ylabel("время t")
ax.legend()

plt.show()
fig.savefig('1.png')

"""
Вывод:
    Алгоритмы выполняются со сложностью близкой к O(N**3)
    Лучший из приведенных алгоритмов содержится в коде l4_1_2(второй вариант)
    Графики приведены в файле 1.png
"""