# x = 'Язык программирования Python'
# print('python' in x)

# s = 13
# k = -5
# d = s + 2
# s = d
# k = 2 * s
# print(s + k + d)

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)

# a = int(input())
# b = int(input())
# c = (a + b) ** 2
# d = a ** 2 + b ** 2
# print("Квадрат суммы", a, "и", b, "равен", c)
# print("Сумма квадратов", a, "и", b, "равен", d)


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# a1 = a ** b
# b2 = c ** d
# print(a1 + b2)

# a = int(input())
# print(a * 123)

# num = int(input())
# last_digit = num % 10    # последняя цифра числа
# first_digit = num // 10  # первая цифра числа
#
# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')


# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)


# if i % 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')

# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')

# password = input()
# password2 = input()
# if password == password2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# while True:
#     a = int(input())
#     if a % 2 == 0:
#         print('bimbim')
#     else:
#         print('bambam')


# a = int(input())
# a1 = (a // 10 ** 3) % 10
# a2 = (a // 10 ** 2) % 10
# a3 = (a // 10 ** 1) % 10
# a4 = (a // 10 ** 0) % 10
#
# b1 = a1 + a4
# b2 = b1 + 1
# if b2 == a2:
#     print("Да")
# else:
#     print("Нет")

# a = int(input())
# if a >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# b1 = (a2 - a1) + a2
# if b1 != a3:
#     print("NO")
# else:
#     print("Yes")


# a1 = int(input())
# a2 = int(input())
#
# if a1 >= a2:
#     print(a2)
# else:
#     print(a1)

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())
#
# if a1 > a2:
#     a1, a2 = a2, a1
# if a2 > a3:
#     a1, a3 = a3, a2
# if a3 > a4:
#     a3, a4 = a4, a4
#
# print(a1)



# while True:
#
#     a1 = int(input())
#
#     if a1 <= 13:
#         print("детство")
#     if 14 <= a1 <= 24:
#         print("молодость")
#     if 25 <= a1 <= 59:
#         print("зрелость")
#     if a1  >= 60:
#         print("старость")


# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
#
# if a1 > 0:
#     a1 = a1
# else:
#     a1 = 0
#
# if a2 > 0:
#     a2 = a2
# else:
#     a2 = 0
#
# if a3 > 0:
#     a3 = a3
# else:
#     a3 = 0
#
# print(a1 + a2 + a3)


# age = int(input('Сколько вам лет?: '))
# grade = int(input('В каком классе вы учитесь?: '))
#
# if age >= 12 and grade >= 7:
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')

'''
a	b	a and b
False	False	False
False	True	False
True	False	False
True	True	True'''


'''a	b	   a or b
False	False	False
False	True	True
True	False	True
True	True	True'''


# a = 2
#
# b = 4
#
# c = 6
#
# print(a == 2 or b > 2)
# print(6 <= c and a > 3)
# print(1 != b and c != 3)
# print(a >= -1 or a <= b)
# print(not (a > 2))
# print(not (c <= 10))

# a = int(input())
#
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
#
# p = (a + b) * (a + b)
# print(p)
