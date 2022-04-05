"""""
n = int(input("nhap so phan tu cua list 1: "))
i = 0
list1=[]
for i in range(n):
    x = int(input("nhap gia tri: "))
    list1.append(x)
print(list1)
m = int(input("nhap so phan tu cua list 2: "))
j = 0
list2=[]
for i in range(m):
    y = str(input("nhap gia tri: "))
    list2.append(y)
print(list2)
dict={}
dict1={}
for k in range(len(list1)):
    dict1 = {list1[k]:list2[k]}
    dict.update(dict1)
print(dict1)
"""""

