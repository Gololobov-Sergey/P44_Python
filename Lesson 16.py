def fact(num):
    res = 1
    for i in range(2,num+1):
        res = res * i
    return res
#print(fact(5))


def fakt_r(n):
    if n == 1:
        return 1
    return n * fakt_r(n-1)

#print(fakt_r(5))

def number(n):
    if n == 0:
        return
    print(n, end=" ")
    number(n-1)

# number(5)

def num1(n):
    if n > 1:
        num1(n-1)
    print(n, end=" ")

# num1(5)


def summ(a, b):
    if a == b: return b
    return a + summ(a+1, b)

print(summ(3,8))


def stepen(a, b):
    if b == 1: return a
    elif b == 0: return 1
    elif b < 0: return 1 / a * stepen(a, b+1)
    else: return a * stepen(a, b-1)


def summ1(a):
    if a < 10: return a
    return a%10 + summ1(a//10)

print(summ1(1234))


def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(6))