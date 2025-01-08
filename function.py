def printLine(count=10, symbol='*'):
    for i in range(count):
        print(symbol, end='')
    print()


# def summ(*args):
#     c = 0
#     for el in args:
#         c += el
#     return c


def isEven(a):
    return a % 2 == 0

def isPositive(a):
    return a > 0

def printList(list_):
    for el in list_:
        print(el, end=' ')
    print()

def countSymbol(list_):
    c = 0
    for i in list_:
        c += len(str(i))
    return c

def printArrInLine(list_):
    count = len(list_) - 1 + countSymbol(list_)
    printLine(count)
    printList(list_)
    printLine(count)

def printAll(uniq, *args):
    print(uniq)
    print(args)
    # for i in args:
    #     print(i)


def asc(a, b):
    return a > b

def desc(a, b):
    return a < b

def even_first(a, b):
    if a % 2 == 0 and b % 2 != 0:
        return False
    if a % 2 != 0 and b % 2 == 0:
        return True
    return asc(a, b)

def from_last_number(a, b):
    if a % 10 > b % 10:
        return True
    if a % 10 == b % 10 and a > b:
        return asc(a, b)

def bubble_sort(arr, method=asc):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if method(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


