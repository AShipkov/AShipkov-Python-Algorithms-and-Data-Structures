"""
9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
def f(n, c=0):
    if (n < 10):
        c += n
        return int(c)
    else:
        c += int(n % 10)
        return f(n // 10, c)

a = []
max_sum = 0
max_int = 0
i=0
print('Подсчет большей суммы цифр чисел')
list_numbers = input('Введите числа через запятую в формате x,y,z: ').split(',')
list_numbers = [int(x) for x in list_numbers]
while i<len(list_numbers):
    sum_a = f(list_numbers[i])
    if max_sum < sum_a:
        max_sum = sum_a
        max_int = list_numbers[i]
    i+=1
print(f'Максимальная сумма цифр, входящих в число, из введенных {max_sum}, соответствует числу {max_int}')

