# # Задание 13.1.4.
#
# def is_leap_year(x):
#     return (x % 400 == 0) or ((x % 4 == 0 and x % 100 !=0))
# print(is_leap_year(int(input())))

# 13.2
# # дано: 123456789. Входит ли цифра 5?
# # Вариант 1
# print(list(str(123456789)))
# # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_digit = list(map(int, list(str(123456789))))
# print(5 in list_digit)
# # True
# # Вариант 2
# print('5' in str(123456789))
# # True

# # 13.3. Условный оператор
# is_rainy = True  # дождь будет
#
# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт")
#

# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")

# # 13.4. Исключения
# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед исключением")
#     # теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b  # здесь может возникнуть исключение деления на ноль
#     print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print(e)  # Выводим информацию об ошибке
#     print("После исключения")
#
# print("После После исключения")

# try:
#     *ваш код*
# except Ошибка:
#     *Код отлова*
# else:
#     *Код, который выполнится, если всё хорошо прошло в блоке try*
# finally:
#     *Код, который выполнится в любом случае*

# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")

# Мы можем вызывать ошибки самостоятельно с помощью конструкции raise
# age = int(input("How old are you?"))
#
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")
#
# print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.
#
# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

# 13.4.8.
# try:
#     i = int(input('Введите число:\t'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print(f'Вы ввели {i}')
# finally:
#     print('Выход из программы')


# Использование логических операторов и операторов сравнения в условном операторе
# #1
# Для последовательностей (строк, списков, кортежей) используйте тот факт,
# что пустая последовательность есть False.
# # Хорошо
# if not seq:
# if seq:
#
# # Плохо
# if len(seq)
# if not len(seq)
#
# # Примеры
#
# if pozitive_num:  # нет смысла проверять len(pozitive_num)
#    # если список не пустой, то печатаем его
#    print("Список положительных чисел равен: ", pozitive_num)
# else:
#    # печатаем, если список оказался пустым
#    print("Список положительных чисел пустой")
#
#
# if not password:  # password строка содержащая пароль, введенный пользователем
#    print("Вы забыли ввести пароль! Повторите попытку ещё раз")

# Не сравнивайте логические типы с True и False с помощью ==, иначе получается «масло масляное».
# # Хорошо
# if greeting:
#
# # Плохо
# if greeting == True:
#
# # Совсем не правильно
# if greeting is True:

#2
# if hour >= 6 and hour < 12:
#     print("Утро!!!")
#
# if 6 <= hour < 12:
#     print("Утро!!!")


# Конструкция if-elif-else
# if a == 10:
#     print('a равно 10')
# elif a < 10:
#     print('a меньше 10')
# else:
#     print('a больше 10')

#3
# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")
#
# def get_wind_class(speed):# Объявление функции
#     if 1 <= speed <= 4:
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return "strong [3]"
#     elif speed > 19:
#         return "hurricane [4]"
# print(get_wind_class(3))

# !!! Список login_list хранит имена пользователей,
# а словарь password_list хранит имена (ключи) и пароли (значения).


# #13.5.4.
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
#
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False


# Тернарный условный оператор — оператор, который записывается в одну строку.
# a = 42
# b = 41
#
# if a > b:
#     result = a
# else:
#     result = b
#
# иначе
# result = a if a > b else b

# Задание 13.5.5
# Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.
# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# Задание 13.5.6
# Запишите логическое выражение, которое определяет,
# что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
# A = int(input('Введите число\n'))
#
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
#     print("Число принадлежит интервалу")

# Задание 13.5.7
# Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.
# n = 15
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# Задание 13.5.8
# Проверьте, все ли элементы в списке являются уникальными.
# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# print(len(list_) == len(set(list_)))

# Задание 13.5.9
# Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).
# num = 12345678
#
# print(str(num) == str(num)[::-1])

# 13.6 Циклы
# Цикл For
# for value in iterator:
#     # Начало блока кода с телом цикла
#     ...
#     ...
#     ...
#     # Конец блока кода с телом цикла
# # Код который будет выполняться после цикла
# - value (название переменной вы выбираете сами)
# - iterator (списка, кортежа, словаря, строки, и так далее)

# C/C++/Java:
# for (int i = 0; i < 10; i++):
#     ...
#
# Python:
# for i in [1, 2, 3, 4, 5]:
#     pass

# Функция range может работать тремя способами:
#
# 1. range(END);
# 2. range(START, END);
# 3. range(START, END, STEP).
#
# print(list(range(5)))
# # [0, 1, 2, 3, 4]

# print(list(range(1, 5)))
# # [1, 2, 3, 4]
#
# print(list(range(1, 10, 2)))
# # [1, 3, 5, 7, 9]
#
# Конструкция list(range(start, end, step)) позволяет получить последовательность (список) целых чисел,
# начинающуюся со start и заканчивающуюся в end-1 с шагом step.


# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     ...
#
S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# Задание 13.6.2
P = 1
N = 5
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение произведения на предыдущем шаге: ", P)
#     print("Текущее число: ", i)
#     P = P * i  # умножаем текущее число i и перезаписываем значение произведения
#     print("Значение произведения после умножения: ", P)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: произведение равно = ", P)

# for i in range(1, N+1):
#     P *= i
#
# print(P)

# Задание 13.6.3
# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)


# Цикл while
# Он выполняется до тех пор, пока истинно его условие.
# Как только оно становится ложным, цикл прерывается.
#
# while условие:
#
#     # Начало блока кода с телом цикла
#     # пока условие истинно, цикл выполняется
#     ...
#     ...
#     ...
#     # Конец блока кода с телом цикла
# # Код, который будет выполняться после цикла


# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)

# Задание 13.6.4
# n = 1
# while n ** 2 < 1000:
#                    n += 1
# print("Количество чисел: ", n)

# Ключевое слово break, которое говорит, что цикл нужно принудительно прервать.
# # хорошо
# n = 1
# while True:  # в данной программе это условие всегда True, цикл будет бесконечным
#    print("Hello World")
#    n += 1
#    if n > 10:  # условие, при достижении которого цикл while будет принудительно завершен
#        break

# Задание 13.6.5
# n = 1
# while True:
#    if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1

# Работа с вложенными циклами
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# N = 2
# M = 3
# # заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
#

# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")
# # 0 1 2 3 4 5
#
# for i in range(N):
#     for j in range(M):
#         print(matrix[i][j], end=" ")
#     print()  # перенос на новую строку
#
# # 0 1 2
# # 3 4 5

# Пример 3.
# Условие задачи. Дана двумерная матрица 3x3. Определите максимум и минимум каждой строки,
# а также их индексы.

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)

# # Задание 13.1.4.
#
# def is_leap_year(x):
#     return (x % 400 == 0) or ((x % 4 == 0 and x % 100 !=0))
# print(is_leap_year(int(input())))

# 13.2
# # дано: 123456789. Входит ли цифра 5?
# # Вариант 1
# print(list(str(123456789)))
# # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_digit = list(map(int, list(str(123456789))))
# print(5 in list_digit)
# # True
# # Вариант 2
# print('5' in str(123456789))
# # True

# # 13.3. Условный оператор
# is_rainy = True  # дождь будет
#
# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт")
#

# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")

# # 13.4. Исключения
# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед исключением")
#     # теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b  # здесь может возникнуть исключение деления на ноль
#     print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print(e)  # Выводим информацию об ошибке
#     print("После исключения")
#
# print("После После исключения")

# try:
#     *ваш код*
# except Ошибка:
#     *Код отлова*
# else:
#     *Код, который выполнится, если всё хорошо прошло в блоке try*
# finally:
#     *Код, который выполнится в любом случае*

# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")

# Мы можем вызывать ошибки самостоятельно с помощью конструкции raise
# age = int(input("How old are you?"))
#
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")
#
# print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.
#
# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

# 13.4.8.
# try:
#     i = int(input('Введите число:\t'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print(f'Вы ввели {i}')
# finally:
#     print('Выход из программы')


# Использование логических операторов и операторов сравнения в условном операторе
# #1
# Для последовательностей (строк, списков, кортежей) используйте тот факт,
# что пустая последовательность есть False.
# # Хорошо
# if not seq:
# if seq:
#
# # Плохо
# if len(seq)
# if not len(seq)
#
# # Примеры
#
# if pozitive_num:  # нет смысла проверять len(pozitive_num)
#    # если список не пустой, то печатаем его
#    print("Список положительных чисел равен: ", pozitive_num)
# else:
#    # печатаем, если список оказался пустым
#    print("Список положительных чисел пустой")
#
#
# if not password:  # password строка содержащая пароль, введенный пользователем
#    print("Вы забыли ввести пароль! Повторите попытку ещё раз")

# Не сравнивайте логические типы с True и False с помощью ==, иначе получается «масло масляное».
# # Хорошо
# if greeting:
#
# # Плохо
# if greeting == True:
#
# # Совсем не правильно
# if greeting is True:

#2
# if hour >= 6 and hour < 12:
#     print("Утро!!!")
#
# if 6 <= hour < 12:
#     print("Утро!!!")


# Конструкция if-elif-else
# if a == 10:
#     print('a равно 10')
# elif a < 10:
#     print('a меньше 10')
# else:
#     print('a больше 10')

#3
# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")
#
# def get_wind_class(speed):# Объявление функции
#     if 1 <= speed <= 4:
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return "strong [3]"
#     elif speed > 19:
#         return "hurricane [4]"
# print(get_wind_class(3))

# !!! Список login_list хранит имена пользователей,
# а словарь password_list хранит имена (ключи) и пароли (значения).


# #13.5.4.
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
#
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False


# Тернарный условный оператор — оператор, который записывается в одну строку.
# a = 42
# b = 41
#
# if a > b:
#     result = a
# else:
#     result = b
#
# иначе
# result = a if a > b else b

# Задание 13.5.5
# Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.
# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# Задание 13.5.6
# Запишите логическое выражение, которое определяет,
# что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
# A = int(input('Введите число\n'))
#
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
#     print("Число принадлежит интервалу")

# Задание 13.5.7
# Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.
# n = 15
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# Задание 13.5.8
# Проверьте, все ли элементы в списке являются уникальными.
# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# print(len(list_) == len(set(list_)))

# Задание 13.5.9
# Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).
# num = 12345678
#
# print(str(num) == str(num)[::-1])

# 13.6 Циклы
# Цикл For
# for value in iterator:
#     # Начало блока кода с телом цикла
#     ...
#     ...
#     ...
#     # Конец блока кода с телом цикла
# # Код который будет выполняться после цикла
# - value (название переменной вы выбираете сами)
# - iterator (списка, кортежа, словаря, строки, и так далее)

# C/C++/Java:
# for (int i = 0; i < 10; i++):
#     ...
#
# Python:
# for i in [1, 2, 3, 4, 5]:
#     pass

# Функция range может работать тремя способами:
#
# 1. range(END);
# 2. range(START, END);
# 3. range(START, END, STEP).
#
# print(list(range(5)))
# # [0, 1, 2, 3, 4]

# print(list(range(1, 5)))
# # [1, 2, 3, 4]
#
# print(list(range(1, 10, 2)))
# # [1, 3, 5, 7, 9]
#
# Конструкция list(range(start, end, step)) позволяет получить последовательность (список) целых чисел,
# начинающуюся со start и заканчивающуюся в end-1 с шагом step.


# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     ...
#
S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# Задание 13.6.2
P = 1
N = 5
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение произведения на предыдущем шаге: ", P)
#     print("Текущее число: ", i)
#     P = P * i  # умножаем текущее число i и перезаписываем значение произведения
#     print("Значение произведения после умножения: ", P)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: произведение равно = ", P)

# for i in range(1, N+1):
#     P *= i
#
# print(P)

# Задание 13.6.3
# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)


# Цикл while
# Он выполняется до тех пор, пока истинно его условие.
# Как только оно становится ложным, цикл прерывается.
#
# while условие:
#
#     # Начало блока кода с телом цикла
#     # пока условие истинно, цикл выполняется
#     ...
#     ...
#     ...
#     # Конец блока кода с телом цикла
# # Код, который будет выполняться после цикла


# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)

# Задание 13.6.4
# n = 1
# while n ** 2 < 1000:
#                    n += 1
# print("Количество чисел: ", n)

# Ключевое слово break, которое говорит, что цикл нужно принудительно прервать.
# # хорошо
# n = 1
# while True:  # в данной программе это условие всегда True, цикл будет бесконечным
#    print("Hello World")
#    n += 1
#    if n > 10:  # условие, при достижении которого цикл while будет принудительно завершен
#        break

# Задание 13.6.5
# n = 1
# while True:
#    if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1

# Работа с вложенными циклами
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# N = 2
# M = 3
# # заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
#

# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")
# # 0 1 2 3 4 5
#
# for i in range(N):
#     for j in range(M):
#         print(matrix[i][j], end=" ")
#     print()  # перенос на новую строку
#
# # 0 1 2
# # 3 4 5

# Пример 3.
# Условие задачи. Дана двумерная матрица 3x3. Определите максимум и минимум каждой строки,
# а также их индексы.

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)


# 13.7 Практические примеры
# Enumerate - возвращает кортежи, где на первом месте стоит индекс элемента, а на втором — его значение.
#
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# или
#
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# Задание 13.7.1
#
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i in range(len(list_)):
#     if list_[i] < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", value)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# Цикл for со строками и словарями
# С помощью словаря в заданном тексте посчитать количество вхождения каждого символа.
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
#
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
#
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
#
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# Приведем примеры:
#
# Обычная строка:  print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# Строка с форматированием %: print("Меня зовут %(name)s. Мне %(age)d лет." % {"name": name, "age": age})
# Использование f-строк последней версии: print(f"Меня зовут {name} Мне {age} лет.")


# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")

# a = '' # пустая строка
# b = a or 1
# print(b)
#
# a = "foo"
# b = "bar"
#
# print(1 and a or b)

# a = ""
# b = "bar"
#
# print(1 and a or b)

text = input()  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == first:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += first + str(count)  # иначе - записываем в результат
        first = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)

