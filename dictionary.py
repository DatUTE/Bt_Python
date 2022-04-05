
list = ["l1","l2"]
dic = {1:'a',2:'b'}
dict1 = {}
dict2 = {}
for i in range(len(list)):
    dict1 = {list[i]: dic}
    dict2.update(dict1)
print(dict2)

dict = {"class":{"student":{"name":"dat",
                             "diem":{
                                 "toan":8,
                                 "ly":9
                                 }
                             }
                 }
        }
print(dict)
dict["class"]["student"]["diem"]["toan"] = 10
print(dict["class"]["student"]["diem"]["ly"])
print(dict)