"""
Третий вариант кода очень похож на второй, за исключением места ввода данных
number = 500
numbers = number*10
Результаты показались мне интересными :)

В диапазоне натуральных чисел numbers определить,
сколько из них кратны каждому из чисел в диапазоне number.
"""
import cProfile
import timeit
number = 500
numbers = number*10
def f1 (n):
    s1 = [c for c in range (2,numbers) if c%n==0]
    return len(s1)
def f2 (m):
    s2 = {m:f1(m) for m in range (2,m)}
    return s2
#cProfile.run('f2(10000)')

"""
cProfile.run('f2(10)')   
         29 function calls in 0.007 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        8    0.000    0.000    0.006    0.001 l4_1_3.py:5(f1)
        8    0.006    0.001    0.006    0.001 l4_1_3.py:6(<listcomp>)
        1    0.000    0.000    0.007    0.007 l4_1_3.py:8(f2)
        1    0.000    0.000    0.007    0.007 l4_1_3.py:9(<dictcomp>)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('f2(100)')
         299 function calls in 0.041 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.041    0.041 <string>:1(<module>)
       98    0.000    0.000    0.040    0.000 l4_1_3.py:5(f1)
       98    0.040    0.000    0.040    0.000 l4_1_3.py:6(<listcomp>)
        1    0.000    0.000    0.041    0.041 l4_1_3.py:8(f2)
        1    0.000    0.000    0.041    0.041 l4_1_3.py:9(<dictcomp>)
        1    0.000    0.000    0.041    0.041 {built-in method builtins.exec}
       98    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('f2(1000)')        
          2999 function calls in 0.409 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.409    0.409 <string>:1(<module>)
      998    0.002    0.000    0.408    0.000 l4_1_3.py:5(f1)
      998    0.406    0.000    0.406    0.000 l4_1_3.py:6(<listcomp>)
        1    0.000    0.000    0.409    0.409 l4_1_3.py:8(f2)
        1    0.001    0.001    0.409    0.409 l4_1_3.py:9(<dictcomp>)
        1    0.000    0.000    0.409    0.409 {built-in method builtins.exec}
      998    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       
cProfile.run('f2(10000)')
         29999 function calls in 4.674 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    4.674    4.674 <string>:1(<module>)
     9998    0.030    0.000    4.662    0.000 l4_1_3.py:5(f1)
     9998    4.629    0.000    4.629    0.000 l4_1_3.py:6(<listcomp>)
        1    0.000    0.000    4.674    4.674 l4_1_3.py:8(f2)
        1    0.013    0.013    4.674    4.674 l4_1_3.py:9(<dictcomp>)
        1    0.000    0.000    4.674    4.674 {built-in method builtins.exec}
     9998    0.003    0.000    0.003    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

python3 -m timeit -n 100 -s "import l4_1_3" "l4_1_3.f2(100)"
100 loops, best of 5: 36.4 msec per loop

python3 -m timeit -n 100 -s "import l4_1_3" "l4_1_3.f2(250)"
100 loops, best of 5: 91 msec per loop

python3 -m timeit -n 100 -s "import l4_1_3" "l4_1_3.f2(500)"
100 loops, best of 5: 191 msec per loop

python3 -m timeit -n 100 -s "import l4_1_3" "l4_1_3.f2(1000)"
100 loops, best of 5: 401 msec per loop

Кубическая регрессия, коэффициент корреляции 0,999
у = -10**(-8)*x**3+1.5*10**(-4)*x**2+0.318*x+3.13
Строим график функции (lesson4_графики _вывод)

"""

