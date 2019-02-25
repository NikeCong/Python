db_infos = [{"name": "张三丰","gender": 1, "nick_name": "三爷", "idcard": "110101153808081017", "blood": "b", "native":"湖北省丹江口市武当山玉虚宫"},{"name": "张大彪","gender": 1, "nick_name": "斌仔", "idcard": "130323197711111011", "blood": "b", "native":"河北省秦皇岛市武山海关区鞋拔子路胶水胡同103"}]

for person in db_infos:

    name = person["name"]
    nick_name = person["nick_name"]
    gender = person["gender"]
    blood = person["blood"]
    address = person["native"]
    id1 = person["idcard"]

    if not name.startswith("张"):
        continue
    if nick_name.find("斌") == -1 and name.find("斌") == -1:
        continue
    if gender !=1:
        continue
    if blood.lower() != "b":
        continue
    if address.find("河北")==-1:
        continue
    if int(id1[6:10])<1975 or int(id1[6:10])>1978 :
        continue

genders={1:"男",0:"女"}
print("姓名:"+name, "别名:"+nick_name, "性别:"+genders[gender], "血型:"+blood, "地址:"+address, "身份证号:"+id1)

