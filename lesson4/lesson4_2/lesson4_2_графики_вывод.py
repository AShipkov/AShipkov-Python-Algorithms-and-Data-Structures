import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(100, 1000, 250)
y1 = 1.74*10**(-6)*x**2+.0366*x-0.1818
y2 = 2.8*10**(-4)*x**2-.0436*x+2.992


fig, ax = plt.subplots()
ax.plot(x, y1, color="blue", label="1 вариант")
ax.plot(x, y2, color="red", label="2 авариант")
ax.set_xlabel("Позиция натурального числа")
ax.set_ylabel("время t")
ax.legend()

plt.show()
fig.savefig('1.png')

"""
Вывод:
    Алгоритмы выполняются со сложностью близкой к O(N**2)
    Лучший из приведенных алгоритмов содержится в коде lesson4_2_1(Вариант Эратосфена)
    Графики приведены в файле 1.png
"""