# a = 5
# b = 4
#
# # + , - , * , / , () , ** , % , //
#
# c = a - b
# c = -a
# c = +a
# c = (2 + 2) * 2
# c = a ** b
#
# a = a + b
# a += b



# Найти расстояние между двумя точками с заданными координатами
# x1 и x2 на числовой оси:

# x1 = int(input("X1 = "))
# x2 = int(input("X2 = "))
#
# l = abs(x1-x2)
# print(l)


# Дана длина L окружности. Найти ее радиус R и площадь S круга, ог-
# раниченного этой окружностью.
# В качестве значения π использовать 3.14.

# L = float(input("L = "))
# P = 3.14
# R = L / (P * 2)
# S = P * R**2
# print(R)
# print(S)
# # L = 2 * P * R
# # S = P * R**2



# Даны три точки A, B, C на числовой оси. Найти длины отрезков AC
# и BC и их сумму.

# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
#
# AC = abs(A - C)
# BC = abs(B - C)
# S = AC + BC



# Даны три точки A, B, C на числовой оси. Точка C расположена между
# точками A и B. Найти произведение длин отрезков AC и BC.

# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
#
# AC = abs(A - C)
# BC = abs(B - C)
# S = AC * BC



# Даны целые положительные числа A и B (A > B). На отрезке длины A
# размещено максимально возможное количество отрезков длины B (без на-
# ложений). найти количество отрезков B, размещенных на отрезке A.

# K = A // B
# N = A % B


# Дано двузначное число. Вывести вначале его левую цифру (десятки),
# а затем — его правую цифру (единицы).

# A = int(input("A = "))
# print(A // 10)
# print(A % 10)


# Дано трехзначное число. Найти сумму цифр.
# A = int(input("A = "))
# a1 = A % 10
# a2 = A // 10 % 10  # A % 100 // 10
# a3 = A // 100
# print(a1 + a2 + a3)


# Дано трехзначное число. В нем зачеркнули первую справа цифру и
# приписали ее слева. Вывести полученное число.
# A = int(input("A = "))
# a1 = A % 10
# a2 = A // 10 % 10  # A % 100 // 10
# a3 = A // 100
# m = a1*100 + a3*10 + a2
# print(m)


# С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала суток.
# m = s // 60

# С начала суток прошло N секунд (N — целое). Найти количество
# полных часов, прошедших с начала суток.

# h = s // 3600