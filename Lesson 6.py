# Дано целое число в диапазоне 100–999. Вывести строку-описание
# данного числа, например: 256 — «двести пятьдесят шесть», 814 — «во-
# семьсот четырнадцать».

# n = int(input("n = "))
# n3 = n % 10
# n2 = n // 10 % 10
# n1 = n // 100
#
#
# if n1 == 1:
#     print("сто", end=' ')
# elif n1 == 2:
#     print("двісті", end=' ')
# elif n1 == 3:
#     print("триста", end=' ')
# elif n1 == 4:
#     print("чотириста", end=' ')
# elif n1 == 5:
#     print("п'тсот", end=' ')
# elif n1 == 6:
#     print("шістсот", end=' ')
# elif n1 == 7:
#     print("сімсот", end=' ')
# elif n1 == 8:
#     print("вісімсот", end=' ')
# elif n1 == 9:
#     print("дев'ятсот", end=' ')
#
# if n2 == 0:
#     print("", end=' ')
# if n2 == 1:
#     if n3 == 0:
#         print("десять", end=' ')
#     else:
#         if n % 100 == 11:
#             print("одинадцять")
#         elif n % 100 == 12:
#             print("дванадцять")
#         elif n % 100 == 13:
#             print("тринадцять")
#         elif n % 100 == 14:
#             print("чотирнадцять")
#         elif n % 100 == 15:
#             print("п'тнадцять")
#         elif n % 100 == 16:
#             print("шістнадцять")
#         elif n % 100 == 17:
#             print("сімнадцять")
#         elif n % 100 == 18:
#             print("вісімнадцять")
#         elif n % 100 == 19:
#             print("дев'ятнадцять")
# elif n2 == 2:
#     print("двадцять", end=' ')
# elif n2 == 3:
#     print("тридцять", end=' ')
# elif n2 == 4:
#     print("сорок", end=' ')
# elif n2 == 5:
#     print("п'тьдесят", end=' ')
# elif n2 == 6:
#     print("шістьдесят", end=' ')
# elif n2 == 7:
#     print("сімдесят", end=' ')
# elif n2 == 8:
#     print("вісімдесят", end=' ')
# elif n2 == 9:
#     print("дев'яносто", end=' ')
#
# if n2 != 1:
#     if n3 == 0:
#         print("", end=' ')
#     if n3 == 1:
#         print("один", end=' ')
#     elif n3 == 2:
#         print("два", end=' ')
#     elif n3 == 3:
#         print("три", end=' ')
#     elif n3 == 4:
#         print("чотири", end=' ')
#     elif n3 == 5:
#         print("п'ть", end=' ')
#     elif n3 == 6:
#         print("шість", end=' ')
#     elif n3 == 7:
#         print("сім", end=' ')
#     elif n3 == 8:
#         print("вісім", end=' ')
#     elif n3 == 9:
#         print("дев'ять", end=' ')


# Робот может перемещаться в четырех направлениях («С» — север,
# «З» — запад, «Ю» — юг, «В» — восток) и принимать три цифровые ко-
# манды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот на-
# право. Дан символ C — исходное направление робота и целое число N —
# посланная ему команда. Вывести направление робота после выполнения
# полученной команды.

# p = input("p (w,s,n,e) = ")
# com = int(input("com (0, 1, -1) = "))
#
# if p == "n":
#     pos = 0
# elif p == "w":
#     pos = 1
# elif p == "s":
#     pos = 2
# elif p == "e":
#     pos = 3
#
# pos += com
# pos %= 4
#
# if pos == 0:
#     p = 'n'
# elif pos == 1:
#     p = 'w'
# elif pos == 2:
#     p = 's'
# elif pos == 3:
#     p = 'e'
#
# print(p)


# Даны целочисленные координаты трех вершин прямоугольника, стороны
# которого параллельны координатным осям. Найти координаты его четвер-
# той вершины.

# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))
# x3 = int(input("x3 = "))
# y3 = int(input("y3 = "))
#
# x4 = 0
# y4 = 0
#
# if x1 == x2:
#     x4 = x3
# elif x2 == x3:
#     x4 = x1
# elif x1 == x3:
#     x4 = x2
#
# if y1 == y2:
#     y4 = y3
# elif y2 == y3:
#     y4 = y1
# elif y1 == y3:
#     y4 = y2
#
# print(x4, y4)


x1 = int(input('1 = '))
x2 = int(input('2 = '))
oper = input('(+,-,*,/)= ')

# match oper:
#     case '+': res = x1 + x2
#     case '-': res = x1 - x2
#     case '*': res = x1 * x2
#     case '/': res = x1 / x2
#     case _: print("error")

# if oper == '+':
#     res = x1 + x2
# elif oper == '-':
#     res = x1 - x2
# elif oper == '*':
#     res = x1 * x2
# elif oper == '/':
#     res = x1 / x2

if res != None:
    print(res)