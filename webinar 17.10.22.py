# условные выражения
# операции сравнения
# == равно
# != не равно
# > < больше, меньше
# >= <= больше или рано, меньше или рано
#
# a = 5
# b = 6
# result = a == b
# print(result)

# оператор in
# значение in набор_значений

# massage = 'hello world'
# hello = 'hello'
# print(hello in massage)

# условная конструкция
# if логическое_выражение:
#     инструкции
# elif логическое выражение:
#      инструкции
# else:
#     инструкции

# language = input('введите язык ')
# if language == 'english' or language == 'английский':
#     print('ты учишь английский язык')
# elif language == 'русский':
#     print('ты учишь русский язык')
# elif language == 'germany':
#     print('ты учишь немецкий язык')
# else:
#     print('ты что-то ввёл не так...')


# Вебинар от 08.09.2022
# Функции в Python
# синтаксис функции
# def имя_функции(аргументы):
#     инструкции
#     return список_выражений
# имя_функции()

# def greet(name):
#     print('привет ' + name + '. Доброе утро')
# greet('Анна') # привет Анна. Доброе утро

# возвращаемое значение - return
# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(absolute_value(2))
# print(absolute_value(-4))

# область видимости (scope) и время жизни переменной
# def my_func():
#     x = 10
#     print('значение внутри функции', x)
# x = 20
# my_func()
# print('значение вне функции', x)

# аргументы функции
# фиксированное количество аргументов

# def greet(name, age):
#     print('привет ' + name + '. Доброе утро!' + 'Мне ' + age + ' лет')
# greet('Анна', '23')

# аргументы по умолчанию

# def greet(name, age = '23'):
#     print('привет ' + name + '. Доброе утро!' + 'Мне ' + age + ' лет')
# greet('Анна')

# именнованный аргумент
#
# def greet(name, age):
#     print('привет ' + name + '. Доброе утро!' + 'Мне ' + age + ' лет')
# greet(name='Анна', age='23')
# greet(name = 'Ivan', age = '54')

# произвольный список аргументов
# *
#
# def greet(*names):
#     for name in names:
#         print('hello', name)
# greet('Kate', 'John', 'Boris')

# def adder(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#     print('sum = ', sum)
# adder(3, 5, 6, 7, 8)

# x = 'глобальная переменная'
# def foo():
#     print('x внутри функции', x)
# foo()
# print('x вне функции', x)

# локальные переменные

# def foo():
#     y = 'локальная переменная'
#     print(y)
# foo()

# x = 'global variable'
# def foo():
#     global x
#     y = 'local variable'
#     x = x * 2
#     print(x)
#     print(y)
# foo()

# x = 5
# def foo():
#     x = 10
#     print('local variable x:', x)
# foo()
# print('global variable x:', x)

# нелокальные переменные nonlocal

# def outer():
#     x = 'локальная переменная'
#     def inner():
#         nonlocal x
#         x = 'нелокальная переменная'
#         print('вложенная функция:', x)
#     inner()
#     print('внешняя функция:', x)
# outer()

# Нелокальные переменные используются во вложенных функциях,
# локальная область видимости которых не определена

# замыкания
# def say():
#     greeting = 'привет'
#     def display():
#         print(greeting)
#     display()
# say()

# вернуть функцию из функции
# def say():
#     greeting = 'привет'
#     print(hex(id(greeting)))
#     def display():
#         print(hex(id(greeting)))
#         print(greeting)
#     return display
# fn = say()
# fn()
# print(fn.__closure__)

# 1. функции say()
# 2. замыкание

# декораторы
# def net_price(price, tax):
#     return price * (1 + tax)
# # $ 100
#
# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'${result}'
#     return wrapper
# net_price = currency(net_price)
# print(net_price(100, 0.05))

#  декоратор синтаксис
#  функция = декоратор(функция)

# @декоратор
# def функция():
# тело функции

# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'${result}'
#     return wrapper
#
# @currency
# def net_price(price, tax):
#     return price * (1 + tax)
# $ 100

# lambda аргументы: выражение

# double = lambda x: x * 2
# print(double(5))

# filter(), map() - функции

my_list = [2,5,56,7,8,9,6]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)