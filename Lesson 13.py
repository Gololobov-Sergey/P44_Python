import random
#
# row = 4
# col = 4
#
# arr = [[random.randint(0, 9) for i in range(col)] for j in range(row)]
#
# for l in arr:
#     for elem in l:
#         print(elem, end=" ")
#     print()
#
# for i in range(len(arr) - 1):
#     for j in range(len(arr) - 1 - i):
#         if arr[j][col-1] > arr[j+1][col-1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#
# print()
# for l in arr:
#     for elem in l:
#         print(elem, end=" ")
#     print()




# st = "hello pYTHON"
# for s in st:
#     print(s)

#print(st[50])

# list_ = [1, 2, 3]
# print(list_)
#
# print(st.count("N"))
# st1 = st.split("o")
# print(st1)
# print(st.title())
# print(st.capitalize())
# print(st.replace("l", "a", 1))
# print(st.startswith("hello"))
# print(st.endswith("ON"))
# print(st.index("lo"))
# print(", ".join([str(i) for i in list_]))
# print(st.upper())
# print(st.lower())
# print(st.ljust(20))
# print(st.rjust(20))
# print(st.center(20))
# print(st.find("l"))
# print(st.rfind("l"))
#
#
# st = "Sergiy Gololobov"
# print(" ".join(reversed(st.split())))


# Користувач вводить із клавіатури рядок.
# Порахуйте кількість букв, цифр у рядку.
# Виведіть обидва результати на екран.

# cb = 0
# cc = 0
# st = "werw33erwer"
# for el in st:
#     if el.isalpha():
#         cb += 1
#     if el.isdigit():
#         cc += 1
# print(cb, cc)


# Дана строка, изображающая целое положительное число. Вывести
# сумму цифр этого числа.

# st = "1234"
# c = 0
# for i in st:
#     c += int(i)
#
# print(c)

import string


# print(string.digits)
# print(string.ascii_letters)
# print(string.hexdigits)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.ascii_lowercase)

st = "Py C++, C#! SQL? C++. C# Ja"
st1 = "C++"
# print(st.replace(",", ""))
# print(max([len(s) for s in st.split()]))

for s in ".,:;!?-":
    if s in st:
        st = st.replace(s, "")
print(st)
print(max([len(s) for s in st.split()]))


# "Python  C# SQL  C# Java"


