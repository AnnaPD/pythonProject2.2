# Задание 14.1.1
# def print_2_add_2():
#     result = 2 + 2
#     print(result)
# print_2_add_2()

# Задание 14.1.2
# def hello_world():
#     print('Hello World')
# hello_world()

# Задание 14.1.3
# def num_divid(a, n):
#     if a % n == 0:
#         print(f'Число {n} является делителем числа {a}')
#     else:
#         print(f'Число {n} не является делителем числа {a}')
# num_divid(10, 3)

# Задание 14.1.4
# def print_num(n):
#     for i in range(n, 0, -1):
#         print("*" * i)
#
# print_num(4)

# Задание 14.1.5
# def get_mult(a):
#     count = 0
#     for n in range(1, a +1):
#         if a % n == 0:
#             count += 1
#     return count
# get_mult(5)
# get_mult(4)

# def get_multipliers(a):
#     count = 0
#     for n in range(1, a + 1):
#         if a % n == 0:
#             count += 1
#     print(count)
#
# get_multipliers(5)
# get_multipliers(4)

# 14.6.5
a = ["asd", "bbd", "ddfa", "mcsa"]
print(list(map(lambda x: len(str(x)), a)))
print(list(map(len, a)))

# 14.6.6
a = ["это", "маленький", "текст", "обидно"]
print(list(map(str.upper, a)))
