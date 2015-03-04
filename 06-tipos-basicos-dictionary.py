# coding: utf-8

# Tipos

# Dictionary = Map ALTO NÍVEL
# chave -> valor
d = {'a':1, 'b':2, 'c':3}
print d
print d['a']
# print d['b']

# atribuição direta! 
d['d'] = 4
print d

a = (1,2)
b = 10
d = {a:'tupla',b:'integer'}

print d[a]
print d[b]

print d.keys()
print d.values()

# d.clear()
# print d