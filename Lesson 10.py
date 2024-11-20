# n = 5
# for k in range(3):
#     for i in range(k+3):
#         for j in range(n-1-i-k+2):
#             print(" ", end=' ')
#         for j in range(2*i+1+2*k):
#             if i == k+2 and (j == 0 or j == 2*i+1+2*k-1) or k == 0 and i == 0:
#                 print("#", end=' ')
#             else:
#                 print("*", end=' ')
#         print()


n = 7
for i in range(10**(n-1), 10**n):
    m = i
    s = 0
    while m > 0:
        r = m % 10
        s += r**n
        m //= 10
    if s == i:
        print(i)
