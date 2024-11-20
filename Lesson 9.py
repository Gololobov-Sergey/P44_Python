
import random

# a = int(input('a = '))
# b = int(input('b = '))
# for i in range(a, b+1):
#     if i % 2 == 1:
#         continue
#     print(i, end=" ")


# for j in range(2, 11):
#     print(j)
#     for i in range(1, 11):
#         print(i, "x", j, "=", j*i)
#     print()


# Дано целое число N (> 0). Найти значение выражения
# 1.1 – 1.2 + 1.3 – ... 1.N
# (N слагаемых, знаки чередуются). Условный оператор не использовать.

# res = 0
# for a in range(1, 1659):
#     k = 0
#     m = a
#     while m > 0:
#         k += 1
#         m //= 10
#     r = ((-1) ** (a+1)) * round(1 + a / (10**k), k)
#     print(r)
#     res += r
#
# print(res)


# q = 0
# for a in range(1001, 1000000):
#     a1 = a // 100000
#     a2 = a // 10000 % 10
#     a3 = a // 1000 % 10
#     a4 = a // 100 % 10
#     a5 = a // 10 % 10
#     a6 = a % 10
#     if a1 + a2 + a3 == a4 + a5 + a6:
#         q += 1
# print(q)

c = 0
for h in range(24):
    for m in range(60):
        for s in range(60):
            h1 = h // 10
            h2 = h % 10
            m1 = m // 10
            m2 = m % 10
            s1 = s // 10
            s2 = s % 10
            if h1 == s2 and h2 == s1 and m1 == m2:
                print(f"{h1}{h2}:{m1}{m2}:{s1}{s2}")
                c += 1
print(c)

a = random.randint(1, 5)



# 56
# 000056

# 2594
# 002594

# .2 ...
# 5
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 10
# 2 x 5 = 10
# 2 x 5 = 10
# 2 x 5 = 10
# 2 x 5 = 10
# 2 x 5 = 10

# 6
# 1 x 6 = 5
# 2 x 6 = 10
# 3 x 6 = 10
# 2 x 6 = 10
# 2 x 5 = 10
# 2 x 5 = 10
# 2 x 5 = 10
# 2 x 5 = 10

# ... 10

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

