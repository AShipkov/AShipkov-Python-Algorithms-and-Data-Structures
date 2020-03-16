"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
letters = 'abcdefghijklmnopqrstuvwxyz'

letter_range = input('Введите диапазон символов от a до z через запятую: ').split(',')
print(letter_range)

a = letters.index(letter_range[0]) + 1
b = letters.index(letter_range[1]) + 1
c = b - a

print('Первая буква: {} - находится на {} позиции \nВторая буква: {} - находится на {} позиции\nРасстояние между ними {}'.format(letter_range[0], a, letter_range[1], b, c))