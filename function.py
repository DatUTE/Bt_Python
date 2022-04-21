def mid_number(a,b,c):
    if((a<b and a>c) or(a>b and a <c)):
        print("so o giua la:" +str(a))
        return a
    elif((b <c and b>a) or (b >c and b <a)):
         print("so o giua la:" +str(b))
         return b
    elif((c>a and c <b) or (c <a and c>b)):
         print("so o giua la:" +str(c))
         return c
mid_number(3,4,5)
#############################
def nam_nhuan(a):
    if(a % 4 == 0 and a % 100 != 0 ):
        #print(str(a) + " la nam nhuan")
        return True

    elif(a %100 == 0 and a%400 == 0):
        #print(str(a) +" la nam nham")
        return True
    else:
        #print(str(a)+" khong la nam nhuan")
        return False
#nam_nhuan(100)
#####################3
def get_day():
    a = int(input("nhap thang:"))
    b = int(input("nhap nam:"))
    if( a <= 12 and a > 0):
        if(a == 1 or a == 3 or a == 5 or a ==7 or a ==8 or a==10 or a ==12 ):
            print("thang" + str(a)+" co 31 ngay")
        elif(a == 2):
            if(nam_nhuan(b)):
                print("thang" + str(a) +" co 29 ngay")
            else:
                print("thang" + str(a) +" co 28 ngay")
        else:
            print("thang" + str(a) +" co 30 ngay")
    else:
        print("khong hop le")
get_day()
###################################
def check_tamgiac():
    a = int(input("nhap so a:"))
    b = int(input("nhap so b:"))
    c = int(input("nhap so c:"))
    if(a+b>c or a +c > b or b +c >a):
        return True
    else:
        return False
list = [-3,-5,-2,-4,-7,-6]
def find_N(list):
    i =0
    flag =0
    for i in range(len(list)):
        if(list[i] >0):
            return list[i]
            break
        else:
            flag += 1
    if(flag == len(list)):
        print("khong co so nguyen duong nao")
#print(find_N(list))
