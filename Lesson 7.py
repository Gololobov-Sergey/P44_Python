
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

n = 1
k = 1
while k < n:
    k *= 3

print(k == n)
