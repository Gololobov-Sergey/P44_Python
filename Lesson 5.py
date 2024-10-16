# m = int(input("M = "))
# x1 = int(input("X1, kg = "))
# x2 = int(input("X2, gr = "))
# x = x1*1000 + x2
# k = m*1000 - x
# if k > x:
#     print("Кролик")
# elif x > k:
#     print("Заяць")
# else:
#     print("=")
#
# print(k)
# print(x)
#
#
# l = int(input("L, l = "))
# if l > 0:
#     p = int(input("P, % = "))
#     if p >= 0 and p <= 100:
#         k1 = l*1000 * p/100
#         k2 = int(input("K2, ml = "))
#         if k2 >= 0 and k2 < l*1000 - k1:
#             k3 = l*1000 - k1 - k2
#             if k1 > k3:
#                 print("K1")
#             elif k3 > k1:
#                 print("K3")
#             else:
#                 print("=")
#         else:
#             print("K2 not correct")
#     else:
#         print("P not correct")
# else:
#     print("L not correct")



# Найти произведение двух наибольших чисел из трёх введённых с клавиатуры.

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a < b and a < c:
#     print(b*c)
# elif b < a and b < c:
#     print(a*c)
# else:
#     print(a*b)

#y % 4 == 0 and y % 100 != 0 or y % 400 == 0

# Даны два целых числа: D (день) и M (месяц), определяющие правиль-
# ную дату невисокосного года. Вывести значения D и M для даты, следую-
# щей за указанной.

d = int(input("d = "))
m = int(input("m = "))

d += 1

if m == 2:
    md = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    md = 30
else:
    md = 31

if d > md:
    d = 1
    m += 1

if m == 13:
    m = 1

print(d, m)