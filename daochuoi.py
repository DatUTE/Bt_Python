def daochuoi():
    a = input("nhap chuoi: ")
    lis = []
    for i in a:
        lis.append(i)
    for j in range(len(lis)-1, -1, -1):
        print(lis[j], end= "")
daochuoi()

