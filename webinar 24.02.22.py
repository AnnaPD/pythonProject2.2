# and or not
# True / Folse
# == != < > <= >=
#
#
# age = 23
# weight = 56
# result = age > 24 or weight == 56
# print(result) # True
#
#
# age = 23
# weight = 56
# result = age > 24 and weight == 56
# print(result) # False
#
#
# age = 23
# weight = 56
# result = age > 19 or not weight == 56
# print(result) # True
#
#
# условная конструкция ветления
# if условие:
#     инструкции
# elif условие:
#    инструкции
# else:
#    инструкции
#
#
# language = input('enter your text ')
# if language == 'english':
#     print('изучаешь английский')
# elif language == 'русский':
#     print('изучаешь русский')
# else:
#     print('не верные данные')
#
#
# language = input('enter your text ')
# if language == 'english' or language == 'английский':
#     print('изучаешь английский')
# elif language == 'русский':
#     print('изучаешь русский')
# else:
#     print('не верные данные')
#
#
# letter = input('enter your text ')
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u' or letter == 'o':
#     print('Зта буква гласная')
# elif letter == 'y':
#     print('Зта буква может быть как гласной, так и согласной')
# else:
#     print('Зта буква согласная')
#
#
# num = int(input())
# if num % 2 == 0:
#     print('четное число ')
# else:
#     print('нечётное число ')

# # for <переменная> in range(start, stop, step):
# for count in range(0, 10, 2):
#     print(count, end=' ')

# # for <переменная> in <последовательность>:
# #     <действие>
# languages = ['C', 'C++', 'Perl', 'Python']
# for x in languages:
#     print(x)

# # break - оператор прерывания
# ediblse = ['отбиыные', 'пельмени', 'яйца', 'орехи']
# for food in ediblse:
#     if food == 'пельмени':
#         print('Я не ем пельмени!')
#         break
#     print('Отлично, вкусные ' + food)
# else:
#     print('Хорошо, что не было пельменей!')
# print('Ужин окончен.')

# # continue - оператор пропуска python
# ediblse = ['отбиыные', 'пельмени', 'яйца', 'орехи']
# for food in ediblse:
#     if food == 'пельмени':
#         print('Я не ем пельмени!')
#         continue
#     print('Отлично, вкусные ' + food)
# else:
#     print('Хорошо, что не было пельменей!')
# print('Ужин окончен.')

# # Цикл while
# i = 0
# while i<11:
#     print(i)
#     i  = i + 1
#
#
# a = 8
# b = 1
# while(a>5):
#     a-=2
#     b+=a
# print(b) # 11
#
# a = 1
# b = 3
# while(a!=5):
#     a+=1
#     b+=a
# print(b) # 17
#
# num = int(input())
# data = []
# while num != 0:
#     data.append(num)
#     num = int(input())
# data.sort()
# print(data)

# word = input()
# data = []
# while word != '':
#     if word not in data:
#         data.append(word)
#     word = input()
# for item in data:
#     print(item)
# или
# word = input()
# data = []
# while word:
#      if word not in data:
#          data.append(word)
#      word = input()
# for item in data:
#     print(item)
#
# line = input()
# negatives = []
# positives = []
# zeros = []
# while line != '':
#     num = int(line)
#     if num < 0:
#         negatives.append(num)
#     elif num > 0:
#         positives.append(num)
#     else:
#         zeros.append(num)
#     line = input()
#
# for item in negatives:
#     print(item)
# for item in zeros:
#     print(item)
# for item in positives:
#     print(item)

# num = int(input())
# count = 0
# while num != 0:
#     if num > 0 and num % 2 != 0 and num % 5 == 0:
#         count += 1
#     num = int(input())
# print(count)

# num = int(input())
# pr = 1
# while num != 0:
#     if num % 5 == 0:
#         pr *= num
#         num = int(input())
# print(pr)

# num = int(input())
# sum = 0
# while num != 0:
#     if num % 2 == 0 and  < num < 26:
#         sum += num
#     num = int(input())
# print(num)

# num = int(input())
# sum = 0
# count = 0
# while num != 0:
#     if num > 0 and num % 8 == 0:
#         sum += num
#         count += 1
#     num = int(input())
# print(sum//count)

# def название_функции():
#     return 'hello'
# print(название_функции())

# def multi_table(number):
#     st = str()
#     for x in range(1, 11):
#         z = x * number
#         st += '{} * {} = {}\n'.format(x, number, z)
#     return st
# print(multi_table(5))

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))
print(descending_order(42145)) # 54421