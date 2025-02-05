# a = 10
# f = open("text.txt", mode="w", encoding="utf-8")
# f.write("Слава Україні!")
# f.close()
import random

# f = open("text.txt", mode="r", encoding="utf-8")
# # s = f.read(6)
# # s = f.readline()
# s = f.readlines()
# # s1 = f.read()
# f.close()
# print(s)
# # print(s1)


# f = open("text.txt", mode="r", encoding="utf-8")
# st = [int(i) for i in f.read().split()]
# out = open("text1.txt", mode="w", encoding="utf-8")
# even = [i for i in st if i%2 == 0]
# out.write(" ".join([str(i) for i in even]))
# f.close()
# out.close()


# marks = [["Яромил"],["Горигляд"],["Ярополк"],["Цвітан"],["Наслав"],["Іларіон"],["Йозеф"],["Худан"],["Щастибог"]]
# for l in marks:
#     l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])
# print(marks)

# f = open('students.txt', mode='w', encoding='utf-8')
# for st in marks:
#     stud_str = [str(el) for el in st]
#     f.write(" ".join(stud_str) + "\n")
# f.close()

# f = open('students.txt', mode='r', encoding='utf-8')
# marks = []
# stud = f.readlines()
# for st in stud:
#     st = st.replace("\n", "").split()
#     mark = [int(i) for i in st[1:]]
#     s = []
#     s.append(st[0])
#     s.extend(mark)
#     marks.append(s)
#
# print(marks)


# week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
# f = open("log.txt", "w")
# for i in range(10000):
#     f.write("192.168.0." + str(random.randint(100, 255)) + " " + week[random.randint(0,6)] + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + "\n")


f = open('log.txt', mode='r', encoding='utf-8')
log = f.readlines()
ip = []
for l in log:
    ip.append(l.split()[0])
ip_uniq = set(ip)


import datetime

d = datetime.datetime.time()
print(d)