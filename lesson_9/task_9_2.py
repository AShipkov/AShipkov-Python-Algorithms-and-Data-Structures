"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter,OrderedDict

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def build_tree(st):
    rate = [(key, value) for key, value in OrderedDict(sorted(Counter(st).items(), key=lambda w: w[1])).items()]
    while len(rate) > 1:
        key_l, value_l = rate.pop()
        key_r, value_r = rate.pop()
        sum = value_l + value_r
        node = (Node(key_l, key_r), sum)
        rate.append(node)
        rate = [(key, value) for key, value in (sorted(rate, key=lambda w: w[1]))]
    tree, s = rate.pop()
    return tree

def fill_dict(tree, d, ch=''):
    if type(tree.left) is Node:
        fill_dict(tree.left, d, ch + '0')
    else:
        d[tree.left] = ch + '0'
    if type(tree.right) is Node:
        fill_dict(tree.right, d, ch + '1')
    else:
        d[tree.right] = ch + '1'
    return d

line = input('Введите строку: ')

d = fill_dict(build_tree(line),{})
code_line = ''.join([d[s] for s in line])
print(code_line.encode('ASCII'))
