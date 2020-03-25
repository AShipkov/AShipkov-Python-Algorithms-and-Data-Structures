"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Первый - использовать алгоритм решето Эратосфена.
Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

"""
import cProfile
import timeit
def eratosthenes(n):
    sieve = list(range(n*100))
    sieve[1] = 2
    for i in sieve:
        if i > 0:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if sieve[x] != 0]
    return sieve1[n]
#print(eratosthenes(120))
#cProfile.run('eratosthenes(10000)')

"""
cProfile.run('eratosthenes(100)')
         1235 function calls in 0.007 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 lesson4_2_1.py:16(<listcomp>)
        1    0.006    0.006    0.007    0.007 lesson4_2_1.py:9(eratosthenes)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
     1230    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
cProfile.run('eratosthenes(1000)')
         9598 function calls in 0.070 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.070    0.070 <string>:1(<module>)
        1    0.009    0.009    0.009    0.009 lesson4_2_1.py:16(<listcomp>)
        1    0.058    0.058    0.069    0.069 lesson4_2_1.py:9(eratosthenes)
        1    0.000    0.000    0.070    0.070 {built-in method builtins.exec}
     9593    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
cProfile.run('eratosthenes(10000)')        
         78504 function calls in 0.603 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.016    0.016    0.603    0.603 <string>:1(<module>)
        1    0.061    0.061    0.061    0.061 lesson4_2_1.py:16(<listcomp>)
        1    0.518    0.518    0.587    0.587 lesson4_2_1.py:9(eratosthenes)
        1    0.000    0.000    0.603    0.603 {built-in method builtins.exec}
    78499    0.009    0.000    0.009    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}   
        
(venv) MacBook-Air-Andrey:lesson4_2 AShipkov$ python3 -m timeit -n 100 -s "import lesson4_2_1" "lesson4_2_1.eratosthenes(100)"
100 loops, best of 5: 3.5 msec per loop
(venv) MacBook-Air-Andrey:lesson4_2 AShipkov$ python3 -m timeit -n 100 -s "import lesson4_2_1" "lesson4_2_1.eratosthenes(1000)"
100 loops, best of 5: 38.2 msec per loop
(venv) MacBook-Air-Andrey:lesson4_2 AShipkov$ python3 -m timeit -n 100 -s "import lesson4_2_1" "lesson4_2_1.eratosthenes(10000)"
100 loops, best of 5: 540 msec per loop
 
Квадратичная регрессия, коэффициент корреляции 0,999
у = 1.74*10**(-6)*x**2+.0366*x-0.1818
Строим график функции (lesson4_2_графики _вывод)
            
"""