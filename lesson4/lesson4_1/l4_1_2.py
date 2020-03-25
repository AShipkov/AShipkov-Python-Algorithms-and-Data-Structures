"""
В диапазоне натуральных чисел numbers определить,
сколько из них кратны каждому из чисел в диапазоне number.
"""
import cProfile
import timeit
def f (n):
    number = n
    numbers = number * 10
    c1 = [c for c in range (2,numbers) if c%n==0]
    return len(c1)
def r (n):
    c2 = {i:f(i) for i in range (2,n)}
    return c2
#cProfile.run('r(10000)')
"""
  cProfile.run('r(10)')
         29 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        8    0.000    0.000    0.000    0.000 l4_1_2.py:3(f)
        8    0.000    0.000    0.000    0.000 l4_1_2.py:6(<listcomp>)
        1    0.000    0.000    0.000    0.000 l4_1_2.py:8(r)
        1    0.000    0.000    0.000    0.000 l4_1_2.py:9(<dictcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
cProfile.run('r(100)')
          299 function calls in 0.005 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
       98    0.000    0.000    0.004    0.000 l4_1_2.py:3(f)
       98    0.004    0.000    0.004    0.000 l4_1_2.py:6(<listcomp>)
        1    0.000    0.000    0.005    0.005 l4_1_2.py:8(r)
        1    0.000    0.000    0.005    0.005 l4_1_2.py:9(<dictcomp>)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
       98    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}       

cProfile.run('r(1000)')
         2999 function calls in 0.429 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.429    0.429 <string>:1(<module>)
      998    0.002    0.000    0.428    0.000 l4_1_2.py:3(f)
      998    0.425    0.000    0.425    0.000 l4_1_2.py:6(<listcomp>)
        1    0.000    0.000    0.429    0.429 l4_1_2.py:8(r)
        1    0.001    0.001    0.429    0.429 l4_1_2.py:9(<dictcomp>)
        1    0.000    0.000    0.429    0.429 {built-in method builtins.exec}
      998    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('r(10000)')
         29999 function calls in 44.382 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   44.382   44.382 <string>:1(<module>)
     9998    0.034    0.000   44.366    0.004 l4_1_2.py:3(f)
     9998   44.328    0.004   44.328    0.004 l4_1_2.py:6(<listcomp>)
        1    0.000    0.000   44.382   44.382 l4_1_2.py:8(r)
        1    0.016    0.016   44.382   44.382 l4_1_2.py:9(<dictcomp>)
        1    0.000    0.000   44.382   44.382 {built-in method builtins.exec}
     9998    0.003    0.000    0.003    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

python3 -m timeit -n 100 -s "import l4_1_2" "l4_1_2.f(100)"
100 loops, best of 5: 71.3 usec per loop

python3 -m timeit -n 100 -s "import l4_1_2" "l4_1_2.f(250)"
100 loops, best of 5: 174 usec per loop

python3 -m timeit -n 100 -s "import l4_1_2" "l4_1_2.f(500)"
100 loops, best of 5: 388 usec per loop

python3 -m timeit -n 100 -s "import l4_1_2" "l4_1_2.f(10000)"
100 loops, best of 5: 8.85 msec per loop

python3 -m timeit -n 100 -s "import l4_1_2" "l4_1_2.f(100000)"
100 loops, best of 5: 86.8 msec per loop

Кубическая регрессия, коэффициент корреляции 0,999
у = .2*10**(-7)*x**3+.19*10**(-4)*x**2+5.2*10**(-3)-.2789
Строим график функции (lesson4_графики _вывод)      
"""
