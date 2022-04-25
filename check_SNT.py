def check_SNT():
    a = int(input("nhap 1 so: "))
    cnt = 0
    if a < 2:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a, 1):
            if a % i == 0:
                cnt = cnt + 1
    if cnt >=1:
        return False
    else:
        return True
k = check_SNT()
print(k)