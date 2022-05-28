#bai3
lis = [5,24,10,22,18,33,44,45,25,30,6,7,8,54]
def findmax(list):
    max = 0
    for i in list:
        if i % 5 == 0:
            if i > max:
                max = i
    return max
print(findmax(lis))
#bai4
def removeA(list):
    a = int(input("nhap so a: "))
    for i in range(len(list)-1, -1,-1):
        if (list[i] > a):
            del list[i]
    return list
lis.sort()
print(lis)
print(removeA(lis))
#bai 5
def insertA(list):
    list.sort()
    print(list)
    a = int(input("nhap so a: "))
    for i in range(len(list)):
        if a >= list[i] and a <= list[i+1]:
            list.insert(i+1, a)
            break
        elif a>= list[len(list)-1]:
            list.append(a)
            break
    if a <= list[0]:
        list.insert(0, a)
    return list
#print(insertA(lis))