import random

# a = [1,3,45,"6",87.22,True]
#
# a[3] = "mama"
#
# for i in a:
#     print(i)
#
#
# for i in range(6):
#     print(a[i])
#
# arr = [0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
# print(arr)
# c0 = 0
# for elem in arr:
#     if elem == 0:
#         c0 += 1
#
# i = 0
# c1 = 0
# while arr[i] != 1:
#     c1 += 1
#     i += 1
#
# for i in range(len(arr)):
#     arr[i]

# l = int(input("Len = "))
# arr = [random.randint(0,20) for i in range(l)]
# print(arr)

# arr = [i for i in range(l)]

# maxElem = arr[0]
# for elem in arr:
#     if elem > maxElem:
#         maxElem = elem
# print(maxElem)

# maxElem = arr[0]
# iMax = 0
# for i in range(len(arr)):
#     if arr[i] > maxElem:
#         maxElem = arr[i]
#         iMax = i
# print(maxElem, iMax)

# s = 0
# for elem in arr:
#     s += elem
# print(s)


# maxElem = arr[0]
# iMax = 0
# for i in range(len(arr)):
#     if arr[i] > maxElem:
#         maxElem = arr[i]
#         iMax = i
#
# minElem = arr[0]
# iMin = 0
# for i in range(len(arr)):
#     if arr[i] < minElem:
#         minElem = arr[i]
#         iMin = i
#
# s = 0
# if iMin < iMax:
#     a = iMin
#     b = iMax
# else:
#     a = iMax
#     b = iMin
# for i in range(a+1, b):
#     s += arr[i]
# print(s)


# arr = [1,5,9,13,17]
# a0 = arr[0]
# d = arr[1] - arr[0]
# flag = True
# for i in range(1, len(arr)-1):
#     if arr[i+1] - arr[i] != d:
#         flag = False
#         break
# print(flag)

# a0 = 5
# d = 3
# l = int(input("Len= "))
# arr = [a0 + d*i for i in range(l)]
# print(arr)

l = int(input("Len = "))
arr = [random.randint(0,20) for i in range(l)]
print(arr)

