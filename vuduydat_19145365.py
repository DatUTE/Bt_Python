#bai 1.
def sochudao(d,m,y):
    ngay = str(d)
    thang = str(m)
    nam = str(y)
    s = 0
    for i in ngay:
        s+=int(i)
    for i in thang:
        s += int(i)
    for i in nam:
        s += int(i)
    while s >= 10:
        s = str(s)
        S = 0
        for i in s:
            S += int(i)
        s = S
    return s

print("so chu dao cua ban la: ", end="")
print(sochudao(29,9,1999))
#bai 2
traicay = ['tao', 'cam', 'chanh']
sothich = {'A': ['tao', 'cam', 'oi'], 'B':['chanh','tao', 'dao'],'C':['oi','chanh', 'cam']}
def bai2_1(list,dict,traicay):
    lis = []
    for i in dict.keys():
        for j in dict[i]:
            if j == traicay:
                lis.append(i)
    return lis
fruit = input("nhap ten trai cay: ")
print(bai2_1(traicay,sothich,fruit))
#bai2_2
def bai2_2(list,dict,hocsinh):
    for i in dict.keys():
        if i == hocsinh:
            return dict[i]
student =  input("nhap vao ten hoc sinh: ")
print(bai2_2(traicay,sothich, student))
#bai 3
chuoi = input("nhap chuoi can kiem tra: ")
def count_char(chuoi):
    lis = list(chuoi)
    set1 = set(chuoi)
    dic = {}
    for i in set1:
        if 'a' <= i <= 'z' or 'A' <= i <='Z':
            dic[i] ={}
            cnt =0
            for j in lis:
                if i == j:
                    cnt +=1
                    dic[i] = cnt
    return dic
print(count_char(chuoi))