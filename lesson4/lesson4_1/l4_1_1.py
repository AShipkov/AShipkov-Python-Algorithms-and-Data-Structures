"""
В диапазоне натуральных чисел numbers определить,
сколько из них кратны каждому из чисел в диапазоне number.
"""
import cProfile
import timeit
count = {}
def f (x, y):
    number = x
    numbers = y
    for a in range(2, numbers):
        for b in range(2, number):
            if (a % b == 0):
                if b not in count:
                    count[b] = 1
                else:
                    count[b] += 1
    return count

#cProfile.run('f(1000,10000)')

"""
 cProfile.run('f(10,100)')
         4 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 l4_1_1.py:4(f)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('f(100,1000)')
         4 function calls in 0.009 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.009    0.009    0.009    0.009 l4_1_1.py:4(f)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('f(1000,10000)')
        4 function calls in 0.827 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.826    0.826 <string>:1(<module>)
        1    0.826    0.826    0.826    0.826 l4_1_1.py:4(f)
        1    0.000    0.000    0.827    0.827 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

python3 -m timeit -n 100 -s "import l4_1_1" "l4_1_1.f(100,1000)"
100 loops, best of 5: 6.74 msec per loop

python3 -m timeit -n 100 -s "import l4_1_1" "l4_1_1.f(250,2500)"
100 loops, best of 5: 39 msec per loop

python3 -m timeit -n 100 -s "import l4_1_1" "l4_1_1.f(500,5000)"
100 loops, best of 5: 176 msec per loop

python3 -m timeit -n 100 -s "import l4_1_1" "l4_1_1.f(1000,10000)"
100 loops, best of 5: 788 msec per loop

Кубическая регрессия, коэффициент корреляции 0,999
у = 10**(-7)*x**3+7.7*10**(-4)*x**2-.06*x+5.08
Строим график функции (lesson4_графики _вывод)
"""

