bangdiem = { 19145365: {'toan':10, 'ly':3, 'hoa': 4},
            19145363: {'toan':10, 'ly':4, 'hoa': 7},
            19145357: {'toan':8, 'ly':4, 'hoa': 6}}
def monno(mssv, bangdiem):
    lis = bangdiem.keys()
    lis1 = []
    for i in lis:
        if i == mssv:
            for j in bangdiem[mssv].keys():
                if bangdiem[mssv][j] < 5:
                    lis1.append(j)
            return lis1
        else:
            return -1

print("cac mon no la: ", end="" )
print(monno(19145365,bangdiem))
# nhap diem
def inputList():
    n = int(input("nhap so nguoi can nhap diem: "))
    bangdiem = {}
    for i in range( n + 1):
        id = input("nhap mssv: ")
        bangdiem[id] = {}
        while True:
            mon = input("nhap ten mon:")
            if mon == "stop":
                break
            else:
                diem = input("nhap diem:")
            bangdiem[id][mon] = diem
    return bangdiem
#mssv = int(input('Nhập mssv: '))
def diemtrungbinh(mssv,bangdiem):
    s = 0
    if mssv not in bangdiem:
        return -1
    else:
        for i in bangdiem[mssv].values():
            s += i
        trungbinh = s / len(bangdiem[mssv])
        return trungbinh
print(diemtrungbinh(19145365, bangdiem))
#a[start:stop:step] step = -1 thì đi từ cuối chuỗi
# a = 'pyy1yyp'
# def chuoidoixung(a):
#     if a[:] == a[::-1]:
#         print('chuỗi đối xứng')
#     else:
#         print('không phải chuỗi đối xứng')
# chuoidoixung(a)




