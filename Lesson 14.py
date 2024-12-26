import random
from function import *



# print(printLine())
# print("Hello")
# printLine(45, '$')
# print("Hello")
# printLine()




##print(summ(2,6, 6))

# m = summ(2,5)
# print(m)
# print(summ(2,5))


print(random.choice("knb"))

# size = int(input("size : "))
# list_ = [random.randint(-100,1900)*0.91 for i in range(size)]

# c = 0
# for el in list_:
#     if(isEven(el) and isPositive(el)):
#         c += 1
# print(c)
#
# print(list_)



#printList(list_)


#printArrInLine(list_)

# *******************
# 3 5 8 8 1 6 0 6 8 1
# *******************


a = 5
print(a)

def increment():
    global a
    a += 10
    print(a)

increment()
print(a)

print(summ())
print(summ(3))
print(summ(3, 6,3,54,87,32))

printLine()
printLine(30)
printLine(20,'#')

printAll(12,2345,456,a,"gerg",True)