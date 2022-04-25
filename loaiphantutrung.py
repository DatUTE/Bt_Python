lis = [2,4,3,5,3,4,6,8,7,2]
def loaitrung(list):
    set1 = set()
    for j in list:
        set1.add(j)
    for i in set1:
        print(i, end="")
loaitrung(lis)