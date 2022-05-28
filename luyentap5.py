bangdiem = {1: {"toan": 4,"li": 7, "hoa": 9},
            2: {"toan": 6,"li": 9, "hoa": 7}
            }
def printmonno(dict,mssv):
    dic = {}
    dic['Mon no'] = {}
    for i in bangdiem:
        if i == mssv:
            for j in dict[i]:
                if dict[i][j] < 5:
                    dic['Mon no'] = {j:dict[i][j]}
    return dic
def diemtrungbinh(dict, mssv):
    dtb = 0
    cnt = 0
    sum = 0
    if mssv not in bangdiem:
        return -1
    else:
        for i in bangdiem:
            if i == mssv:
                for j in dict[i].values():
                    cnt += 1
                    sum += j
                dtb = sum / cnt
    return dtb
#print(diemtrungbinh(bangdiem,3))
def capnhatdiem(dict, mssv, tenmon, diem):
    if mssv not in dict:
        return "NO_ID"
    if tenmon not in dict[mssv]:
        return "NO_SUBJECT"
    else:
        diem1 = dict[mssv][tenmon]
        dict[mssv][tenmon] = diem
    return mssv, tenmon, diem1
#print(capnhatdiem(bangdiem,1,"hoa", 8))
def capnhatdiem2( mssv, tenmon,diem, chophepthem):
    dict1 = {}
    if chophepthem == True:
        if mssv not in bangdiem:
            dict1[mssv] = {}
            dict1[mssv][tenmon] = diem
            print("da them mssv,tenmon, diem")
            bangdiem.update(dict1)
        else:
            if tenmon not in bangdiem[mssv]:
                bangdiem[mssv][tenmon] = diem
                print("da them tenmon, diem")
            elif tenmon in bangdiem[mssv]:
                bangdiem[mssv][tenmon] = diem
                print("da cap nhat diem")
        return mssv, tenmon, diem
    else:
        if mssv not in bangdiem or tenmon not in bangdiem[mssv]:
            return "'NO_ID','NO_SUBJECT',-1"
        else:
            diem1 = bangdiem[mssv][tenmon]
            bangdiem[mssv][tenmon] = diem
        return mssv, tenmon, diem1

print(capnhatdiem2( 3, "ly",8, True))
print(bangdiem)
print(capnhatdiem2( 3, "toan",8, True))
print(bangdiem)
doanhthu = [0,0,-3,8,-7,-9,2]
def danhgiadoanhthu(list):
    sum = 0
    tb = 0
    cnt = 0
    i = 0
    a = 0
    for i in range(len(list)):
        sum +=list[i]
    for i in list:
        if i < 0:
            cnt+=1
            if cnt == 3:
                a = 1
        else:
            cnt = 0
    print(cnt)
    tb = sum/len(list)
    if tb >= 3:
        return "kha quan"
    elif tb >=0:
        return "on dinh"
    elif tb < 0 and a == 1:
        return "cai thien ngay"
    else:
        return "can cai thien"
#print(danhgiadoanhthu(doanhthu))