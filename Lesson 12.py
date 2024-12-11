import datetime
import random

# l = int(input("Len = "))
# arr = [random.randint(-20,20) for i in range(l)]
# arr = [1,3,4,5,3,6,3]
# print(arr)

# arr1 = []
# for elem in arr:
#     if elem > 0:
#         arr1.append(elem)
#
# print(arr1)

# arr.insert(12, 999)
# print(arr)
# arr.remove(3)
# print(arr)
# print(arr.count(3))
# print(3 in arr)
# arr.pop(3)
# print(arr)
# arr.extend([7,7,7,7])
# print(arr)


# l = 1000000 #int(input("Len = "))
# arr = [random.randint(0,200000) for i in range(l)]
# t1 = datetime.datetime.now()
# # print(arr)
# count = 0
# # arr.sort()
# for i in range(len(arr) - 1):
#     for j in range(len(arr) - 1 - i):
#         if arr[j] > arr[j+1]:
#             t = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = t
#             count +=1
# print(datetime.datetime.now() - t1)
# # print(arr)
# print(count)

# for i in range(len(arr)):
#     print(f"{arr[i]:3}", end='')
# print()
# for i in range(len(arr)):
#     print(f"{i:3}", end='')
# print()
# delta = 0
# for i in range(len(arr)-1):
#     if abs(arr[i] - arr[i+1]) > delta:
#         delta = abs(arr[i] - arr[i+1])
#         h = i
# print(h)
# print(arr)

# i = 0
# while i < len(arr):
#     if arr[i] % 2 == 0:
#         arr.pop(i)
#         i -= 1
#     i += 1
#
# print(arr)

row = 4
col = 4

# arr = [[1,2,3], [2,3,4], [4,5,8]]
arr = [[random.randint(0, 9) for i in range(col)] for j in range(row)]
# for l in arr:
#     for elem in l:
#         print(elem, end=" ")
#     print()

# print(arr[1])

s_row = 0
for i in range(len(arr)):
    s = 0
    for j in range(len(arr[i])):
        s += arr[i][j]
        print(f"{arr[i][j]:4}", end="")
    print(" | ", s)
    if s > s_row:
        s_row = s
        iMR = i
s_col = 0
for j in range(len(arr[0])):
    s = 0
    for i in range(len(arr)):
        s += arr[i][j]
    print(f"{s:4}", end="")
    if s > s_col:
        s_col = s
        iMC = j
print()

print("Row", iMR)
print("Col", iMC)
# print(arr[2][1])
