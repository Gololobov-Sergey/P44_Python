import random
from function import *

marks = [["Яромил"],["Горигляд"],["Ярополк"],["Цвітан"],["Наслав"],["Іларіон"],["Йозеф"],["Худан"],["Щастибог"]]
for l in marks:
    l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])

#print(marks)


def print_table(marks):
    width_pib = 0
    for st in marks:
        if len(st[0]) > width_pib:
            width_pib = len(st[0])
    width_pib += 3
    for st in marks:
        print(str(st[0]).ljust(width_pib), end=' ')
        for i in range(1, len(st)):
            print(str(st[i]).rjust(3), end='')
        print()

def max_avg_mark(marks):
    avg_list = [sum(st[1:])/len(st[1:]) for st in marks]
    return marks[avg_list.index(max(avg_list))]


def sort_from_avg_mark(marks):
    avg_list = [sum(st[1:])/len(st[1:]) for st in marks]
    for i in range(len(avg_list) - 1):
        for j in range(len(avg_list) - 1 - i):
            if avg_list[j] < avg_list[j + 1]:
                avg_list[j], avg_list[j + 1] = avg_list[j + 1], avg_list[j]
                marks[j], marks[j+1] = marks[j+1], marks[j]



# print_table(marks)
# #print(max_avg_mark(marks))
# sort_from_avg_mark(marks)
# print()
# print_table(marks)


def hello():
    print("Hello")

def goodbye():
    print("Goodbye")

# func = hello
# func()
# func = goodbye
# func()

f_list = [hello, goodbye]
for f in f_list:
    f()

f_list[1]()

def summ(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(a, b):
    return a**b

# oper = [summ, diff, mult, div, pow]
# a = int(input("a = "))
# b = int(input("b = "))
# op = int(input("1+, 2-, 3*, 4/, 5** : "))
# print(oper[op-1](a, b))



# l = 20 #int(input("Len = "))
# arr = [random.randint(0,20) for i in range(l)]
# print(arr)
# bubble_sort(arr, from_last_number)
# print(arr)


def kopatel():
    print("Копає один працівник з лопатою")

def kopatel3():
    print("Копають три робітника з лопатами і кірками")

def exkawator():
    print("Працює екскаватор, працівник курять в стороні")

def prorab(l):
    if l < 50:
        return kopatel
    if l < 150:
        return kopatel3
    return exkawator


director = prorab(200)
director()