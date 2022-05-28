# def countChar(c):
#     set1 = set()
#     lis = []
#     dic = {}
#     for i in c:
#         if i.isalpha():
#             lis.append(i)
#     for i in c:
#         if i.isalpha():
#             set1.add(i)
#     for i in set1:
#         cnt = 0
#         for j in lis:
#             if i == j:
#                 cnt +=1
#         dic[i] = cnt
#     print(dic)
# countChar("vu duy dat")
dic = {"hoc" : 60, "ngu": 180, "dichoi" : 60, "thethao":120}
def quanly(dict):
    lis=[]
    dict1 = {}
    dict2 = {}
    time = int(input("nhap thoi gian: "))
    active = input("nhap hoat dong can them thoiw gian: ")
    for i in dict.keys():
        if i == active:
            dict[i] +=time
    for i in dict.keys():
        dict[i] = dict[i]/60
    max = 0
    for i in dict.keys():
        if dict[i] > max:
            max = dict[i]
            min = max
            dict1["hoat dong dai nhat "] = i
    for i in dict.keys():
        if dict[i] < min:
            min = dict[i]
            dict2["hoat dong ngan nhat "] = i
            dict1.update(dict2)
    print(dict1)
    return dict
#print(quanly(dic))
def findkey(dict):
    a = int(input("nhap value: "))
    for i in dict.keys():
        if dict[i] == a:
            return i
#print(findkey(dic))
# def password(pas):
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     if len(pas) >= 8:
#         a = 1
#     for i in pas:
#         if i.isdigit():
#             b = 1
#         if i.isalpha():
#             c = 1
#         if (i.isalpha() == False) and (i.isdigit() == False):
#             d = 1
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     if a == 1 and b == 1 and c == 1 and d == 1:
#         return 'Mạnh vl'
#     else:
#         return 'Yếu vc'
#
# print(password('wegv3787fg32hv32vu!'))
def saveElectric(P):
    if P < 2:
        return 5
    elif P <=4:
        return 4
    elif P <6:
        return 3
    elif P < 10:
        return 2
    else:
        return 1
def thongbao():
    p = int(input("nhap so dien"))
    if saveElectric(p) < 3:
        return 'khong  tiet kiem'
    else:
        return 'tiet kiem'
