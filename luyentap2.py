#cau1
import math


def sum1(n):
    S = 0
    s = 0
    i = 1
    while i <= n:
        s+=i
        S += 1/s
        i +=1
    return S
print(sum1(4))
#cau2
def sum2(n):
    S = 0
    for i in range(1,n+1):
        S += 1/(i*(i+1))
    return S
print(sum2(3))
#cau5
# def findmax():
#     lis = []
#     lis1 = []
#     c = True
#     while c:
#         n = int(input("nhap 1 so nguyen: "))
#         while n <= 0:
#             n = int(input("nhap 1 so nguyen: "))
#         for i in range(n):
#             a = int(input("nhap so nguyen thu " + str(i + 1) + ": "))
#             lis.append(a)
#         for i in lis:
#             if i % 2 != 0:
#                 lis1.append(i)
#         lis1.sort()
#         print(lis1[len(lis1) - 1])
#         c = input("ban có muốn tiếp tục không? nếu có nhấn phím c, nếu không nhấn bất kì: ")
#         if c != 'c':
#             break
#         else:
#             continue
# print(findmax())
#cau6
def sum3(n):
    x = int(input("nhap 1 so: "))
    S = x
    s = 1
    for i in range(2, n+1):
        s += i
        S += (pow(x,i))/s
    return S
print(sum3(4))