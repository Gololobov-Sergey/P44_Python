def printLine(count=10, symbol='*'):
    for i in range(count):
        print(symbol, end='')
    print()


def summ(*args):
    c = 0
    for el in args:
        c += el
    return c


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