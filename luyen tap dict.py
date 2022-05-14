# bai 1 tinh tong value
dic = {'a' : 7, 'b':10, 'c':12}
def sum_value(dict):
    sum = 0
    list1 = list(dict.values())
    for i in list1:
        sum = sum + i
    return sum
print(sum_value(dic))
#bai 2 ham tao dictionary
keys = ['a', 'b','c']
values = [1,2,3]
def khoitaodict(k,v):
    dict ={}
    dict1 = {}
    for i in range(len(k)):
        dict = {k[i] : v[i]}
        dict1.update(dict)
    return dict1
print(khoitaodict(keys,values))
#bai 3
def check_dict():
    yourdict = dict()
    cnt = 0
    sothich1 = {'bongchuyen', 'bongda', 'caulong', 'cu ta'}
    yourdict['so thich'] = sothich1
    mydict = dict()
    sothich2 = {'bongda', 'bongchuyen', 'caulong'}
    mydict['so thich'] = sothich2
    if mydict['so thich'] == yourdict['so thich']:
        return True
    else:
        return False
    # lis1 = list(yourdict.values())
    # lis2 = list(mydict.values())
    # for i in range(len(lis1)):
    #     for j in range(len(lis2)):
    #         if lis1[i] == lis2[j]:
    #             cnt+=1
    # if cnt == len(lis1):
    #     return True
    # else:
    #     return False
print(check_dict())
#bai 4: xoa dict theo key
lis= ['a', 'b']
def del_listkey(dict, list_key):
    for i in list_key:
        dict.pop(i)
    return dict
print(del_listkey(dic,lis))