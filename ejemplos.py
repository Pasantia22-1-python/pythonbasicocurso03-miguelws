import copy
import random

"""
#LISTAS
countries = ['Mexico', 'Guatemala', 'Colombia', 'Venezuela']

#Lista mutable
print(countries)
countries[0] = 'Ecuador'
print(countries)

#alias
global_countries = countries
countries[0] = 'Belice'
print(countries)
print(global_countries)

#funcion Copy
global_countries = None
global_countries = copy.copy(countries)
print(global_countries)
countries[0] = 'Honduras'
print(global_countries)
print(countries)

#bucle for
for country in countries:
    print(country)

a = list(range(0, 100, 2))
b =list(range(0, 10))

#solo aplica con + y *
print(a)
print(b)
print(b*2)
print(a+b)

#metodo append()
fruits = []
fruits.append('apple')
print(fruits)
fruits.append('banana')
print(fruits)
fruits.append('kiwi')
print(fruits)

#metodo pop()
some_fruits = fruits.pop()
print(some_fruits)
print(fruits)
some_fruits2 = fruits.pop(0)
print(some_fruits2)
print(fruits)

#metodo del
del fruits[0]
print(fruits)

#modulo random
list_random = []
for i in range(10):
    list_random.append(random.randint(0,15))
print(list_random)

#metodo sorted
order_list = sorted(list_random)
print(order_list)

#metodo sort
list_random.sort()
print(list_random)

#DICCIONARIOS
rae = {}
rae['pizza'] = 'La comida mas deliciosa del mundo'
rae['pasta'] = 'La comida mas sabrosa de italia'

#acceso al valor
print(rae['pizza'])
print(rae['pasta'])

#metodo get
a = rae.get('helado', None)
print(a)

#lista de llaves
print(rae.keys())

#lista de los valores
print(rae.values())

#lista de tuplas de los valor
print(rae.items())

for key in rae.keys():
    print(key)

for value in rae.values():
    print(value)

for key, value in rae.items():
    print(key, value)


#TUPLAS
a = 1, 2, 3
print(a[1])

#metodo count()
a = (1, 1, 1, 2, 3, 4)
print(a.count(1))
print(a.count(2))

#metodo index()
print(a.index(1))
print(a.index(3))

#metodo set()
a = set([1, 2, 3])
b = {3, 4, 5}
print(type(a))
print(type(b))

#metodo add(), no duplica
a.add(3)
print(a)
a.add(20)
print(a)

#metodo intersection()
print(a.intersection(b))

#metodo union()
print(a.union(b))

#metodo difference()
print(a.difference(b))
print(b.difference(a))

#metodo remove()
a.remove(20)
print(a)
"""

#COMPREHENSIONS
lista_numeros = list(range(100))

pares = [numero for numero in lista_numeros if numero%2 == 0]
print(pares)

student_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Larsen']

students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print(students_with_uid)

random_numbers = []
for i in range(10):
	random_numbers.append(random.randint(1, 3))
print(random_numbers)

no_repeated = {number for number in random_numbers}
print(no_repeated)
