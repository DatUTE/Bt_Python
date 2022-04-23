#ham kiem tra nam nhuan
def check_namnhuan(y):
    if y %100 == 0:
        if y %400 ==0:
            return True
        else:
            return False
    elif y %100 != 0:
        if y % 4 ==0:
            return True
        else:
            return False
    else:
        return False
#hàm trả về số ngày trong tháng
def check_ngay(m):
    if m in (1,3,5,7,8,10,12):
        return 31
    elif m ==2 :
        if(check_namnhuan()):
            return 29
        else:
            return 28
    else:
        return 30
def return_nextDay():
    d = int(input("nhap ngay:"))
    m = int(input("nhap thang:"))
    y = int(input("nhap nam: "))
    while(d <= 1 and d >= 31) and (m <= 1 and m >= 12) and y < 0:
        print("nhap sai, nhap lai~")
        d = int(input("nhap ngay:"))
        m = int(input("nhap thang:"))
        y = int(input("nhap nam: "))
    if d == 28 and m == 2 :
        if  check_namnhuan(y) == False:
            d = 1; m = 3
            return (str(d) + "/" + str(m) +"/" + str(y))
        else:
            d = 29;
            m = 2
            return (str(d) + "/" + str(m) +"/" + str(y))
    elif d == 29 and m == 2 :
        if check_namnhuan(y) == True:
            d = 1;
            m = 3
            return (str(d) + "/" + str(m) +"/" + str(y))
        else:
            return "Error"
    elif (d == 30):
        if check_ngay(m) == 30:
            d = 1; m = m+1
            return (str(d) + "/" + str(m) +"/" + str(y))
        elif check_ngay(m) == 31:
            d = d+1
            return (str(d) + "/" + str(m) +"/" + str(y))
    elif d == 31 :
        if m != 12 and check_ngay(m) == 31:
            d = 1; m= m +1
            return (str(d) + "/" + str(m) +"/" + str(y))
        elif m == 12:
            d = 1;m = 1;y = y + 1
            return (str(d) + "/" + str(m) +"/" + str(y))
    else:
        d = d+1;
        return (str(d) + "/" + str(m) +"/" + str(y))
print(return_nextDay())