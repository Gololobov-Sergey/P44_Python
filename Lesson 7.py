
# while condition:
#     oper1
#     oper2
#     oper3

# a = 3
# b = 8
# if a < b:
#     while a <= b:
#         print(a, end=' ')
#         a += 1
# else:
#     while a >= b:
#         print(a, end=' ')
#         a -= 1


# a = int(input('a = '))
# b = int(input('b = '))
# c = 0
# while a >= b:
#     a -= b
#     c += 1
# print(a)
# print(c)


# Дано целое число N (> 0). Если оно является степенью числа 3, то вы-
# вести True, если не является — вывести False.

# n = 1
# k = 1
# while k < n:
#     k *= 3
#
# print(k == n)


count = 1
many = 0
nott = 0
while count < 50000:
    e = count % 10
    d = (count // 10) % 10
    c = (count // 100) % 10
    b = (count // 1000) % 10
    a = (count // 10000) % 10
    if a == 4 or b == 4 or c == 4 or d == 4 or e == 4 or (a == 1 and b == 3) or (b == 1 and c == 3) or (c == 1 and d == 3) or (d == 1 and e == 3):
        nott += 1
        print(count)
    count += 1

many = 50000 - nott
print(nott)
