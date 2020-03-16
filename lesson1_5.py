"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
letters = 'abcdefghijklmnopqrstuvwxyz'
Letters = 'ABCDEFGHIGKLMNOPQRSYUVWXYZ'

letterindex = int(input('Введите номер буквы английского альфавита: '))

print('Буква: ',Letters[letterindex-1],letters[letterindex-1])