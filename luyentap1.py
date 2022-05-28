import math
#cau1
# a = (2 + (3^2))/((5/2)+(2^5))
# print(a)
# b = math.log(27,3)
# print(b)
# c = math.sin(3*(math.pi)/4)
# print(c)
# d1 = math.e
# d2 = (2*math.pi)/(math.log(4,d1))
# d = math.pow(d1,d2)
# print(d)
# e = math.sqrt(math.pow(5,6)+math.factorial(3))
# print(e)
#cau2
def DTtamgiac(chieucao, canhday):
    S = 0
    S = (1/2)*chieucao*canhday
    return S
print(DTtamgiac(6,10))
#cau3
def DThinhtron(duongkinh):
    S = 0
    S = math.pi*math.pow((duongkinh/2),2)
    return S
print(DThinhtron(8))
#cau4
lis = [math.pi, (math.pi)/2, 4*(math.pi)/3]
def checkham(list):


    for i in list:
        if (math.pow(math.sin(i),2) + math.pow(math.cos(i),2)) == 1:
            return True
        else:
            return False
print(checkham(lis))
#cau5
# def ptbac2():
#     a = int(input("nhap a: "))
#     b = int(input("nhap b: "))
#     c = int(input("nhap c: "))
#     lis = []
#     x1=0; x2=0
#     delta = math.pow(b,2) - 4*a*c
#     if delta == 0:
#         x1 = x2 = -c/b
#         return x1
#     elif delta < 0:
#         return "phuong trinh vo nghiem"
#     else:
#         x1 = (-b + math.sqrt(delta))/ (2*a)
#         x2 = (-b - math.sqrt(delta)) /(2*a)
#         lis.append(x1)
#         lis.append(x2)
#         return lis
# print(ptbac2())
#cau6
# def abslonhon10():
#     a = int(input("nhap a: "))
#     b = int(input("nhap b: "))
#     c = int(input("nhap c: "))
#     lis = []
#     res = []
#     lis.append(a)
#     lis.append(b)
#     lis.append(c)
#     for i in lis:
#         if math.fabs(i) < 10:
#             res.append(i)
#     return res
# print(abslonhon10())
#cau7
def findMax():
    lis = []
    dic = {}
    dic1 = {}
    for i in range(5):
        a = int(input("nhap so thu "+ str(i+1) +": "))
        lis.append(a)
    lis.sort()
    max = lis[4]
    min = lis[0]
    dic["max"] = max
    dic1["min"] = min
    dic.update(dic1)
    return dic
print(findMax())



