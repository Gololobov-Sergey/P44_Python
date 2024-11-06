# Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км.
# Каждый следующий день он увеличивал длину пробега на P процентов от
# пробега предыдущего дня (P — ціле, 0 < P < 50). По данному P
# определить, после какого дня суммарный пробег лыжника за все дни пре-
# высит 200 км, и вывести найденное количество дней K (целое) и суммар-
# ный пробег S (вещественное число).
from itertools import count

# s0 = 10
# s = 10
# p = 25
# d = 1
# while s <= 200:
#     n = s0 + s0*p/100
#     s += n
#     d += 1
#     s0 = n
# print(d, s)


# lmax = 11
# d = 0
# ld = 4
# ln = 2
# l = 0
# while l < lmax:
#     l += ld
#     d += 1
#     if l < lmax:
#         l -= ln
#
# print(d)


# n = int(input("n = "))
# s = 0
# while n > 0:
#     r = n % 10
#     s += r
#     n = n // 10
#
# print(s)

# n = int(input("n = "))
# m = 0
# k = 0
# while n > 0:
#     r = n % 10
#     if r != 6 and r != 3:
#         m += r * 10 ** k
#         k += 1
#     n //= 10
# print(m)

# n = int(input("n = "))
# m = 0
# while n > 0:
#     r = n % 10
#     m = m * 10 + r
#     n //= 10

# 1 1 2 3 5 8 13 21 34 55 89 .......

# n = int(input("n = "))
# f1 = 1
# f2 = 1
# #Fn = Fn-1 + Fn-2
# k = 2
# fn = 1
# while fn < n:
#     fn = f1 + f2
#     f1 = f2
#     f2 = fn
#     k += 1
# print(k)


m = 10000
k = 0
while m < 99999:
    count = 0
    n = m
    while n > 0:
        r = n % 10
        if r == 5:
            count += 1
        n //=10
    if count == 3 and m % 9 == 0:
        print(m)
        k += 1
    m += 1
print(k)