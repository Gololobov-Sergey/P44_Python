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