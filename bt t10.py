#hàm tìm số nguyên dương đầu tiên trong list
a = [-7,-4,-5,3,4,5,-6, 9]
def firsrN(list):
    for i in list:
        if(i>0):
            return i
            break
print(firsrN(a))
#hàm tìm vị trí số chẵn đầu tiên trong list
def find_firstchan(list):
    for i in range(len(list)):
        if(list[i] %2 == 0):
            return i
            break
print(find_firstchan(a))
#hàm tìm số chẵn cuối cùng trong list
def find_lastchan(list):
    for i in range(len(list)-1, 0, -1):
        if(list[i] %2 == 0):
            return i
            break
print(find_lastchan(a))
#hàm sắp xếp 1 list tăng dần
def sort_list(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if(list[j] < list[i]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list
print(sort_list(a))
#hàm kiểm tra nguyên âm hay phụ âm
def check_word():
    a = input("nhap 1 ki tu:")
    while len(a) > 1 or len(a) ==0:
        a = input("phải nhap 1 ki tu:")
    if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= "Z"):
        if a in ('u', 'e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I'):
            print(a, "la nguyên âm")
        else:
            print(a, "là phụ âm")
    elif (a >= '0' and a <= "9"):
        print(a, "là một số")
    else:
        print("không hợp lê")
#check_word()
#hàm trả về mùa trong năm nếu biết ngày và tháng
def check_season():
    d = int(input("nhap vao ngay: "))
    m = int(input("nhap vao thang: "))
    while(d <= 1 and d >= 31) and (m <= 1 and m >= 12):
        print("nhap sai, nhap lai!")
        d = int(input("nhap vao ngay: "))
        m = int(input("nhap vao thang: "))
    if m in(1,2,3):
        return "mua xuan"
    elif m in(4,5,6):
        return "mua he"
    elif m in (7,8,9):
        return "mua thu"
    else:
        return "mua dong"
#print(check_season())
