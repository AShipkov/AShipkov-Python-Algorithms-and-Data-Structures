import cProfile
import timeit
def simple_number(index):
    number = 3
    simple_numbers = [2]
    numbers = [2]
    while True:
        if len(simple_numbers) == index:
#            print(f'{index} простое число ряда равно {simple_numbers[index-1]}')
            break
        else:
            for i in numbers:
                if number % i == 0:
                    numbers.append(number)
                    break
            else:
                numbers.append(number)
                simple_numbers.append(number)
        number += 1
    return simple_numbers

#print(simple_number(120))
#cProfile.run('simple_number(10000)')

"""
cProfile.run('simple_number(100)')
         1183 function calls in 0.004 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.004    0.004 lesson4_2_2.py:3(simple_number)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      638    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('simple_number(1000)')
         16839 function calls in 0.263 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.263    0.263 <string>:1(<module>)
        1    0.261    0.261    0.263    0.263 lesson4_2_2.py:3(simple_number)
        1    0.000    0.000    0.263    0.263 {built-in method builtins.exec}
     7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     8916    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('simple_number(10000)')
         219459 function calls in 37.720 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002   37.720   37.720 <string>:1(<module>)
        1   37.673   37.673   37.718   37.718 lesson4_2_2.py:3(simple_number)
        1    0.000    0.000   37.720   37.720 {built-in method builtins.exec}
   104728    0.023    0.000    0.023    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   114726    0.022    0.000    0.022    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

(venv) MacBook-Air-Andrey:lesson4_2 AShipkov$ python3 -m timeit -n 100 -s "import lesson4_2_2" "lesson4_2_2.simple_number(100)"
100 loops, best of 5: 1.51 msec per loop
(venv) MacBook-Air-Andrey:lesson4_2 AShipkov$ python3 -m timeit -n 100 -s "import lesson4_2_2" "lesson4_2_2.simple_number(500)"
100 loops, best of 5: 53.1 msec per loop
(venv) MacBook-Air-Andrey:lesson4_2 AShipkov$ python3 -m timeit -n 100 -s "import lesson4_2_2" "lesson4_2_2.simple_number(1000)"
100 loops, best of 5: 247 msec per loop
10000 не дождался :)

Квадратичная регрессия, коэффициент корреляции 0,999
у = 2.8*10**(-4)*x**2-.0436*x+2.992
Строим график функции (lesson4_2_графики _вывод)

"""