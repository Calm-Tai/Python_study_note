lit1 = []
for i in range(5):
    item = input("请输入购物信息")
    lit1.append(item)

for item in lit1:
    print(item)

# 购物车变量
car_lit = []
while True:
    num = input("输入商品编号:")
    _bool = False
    for item in lit1:
        if num == item[0: 4]:
            _bool = True
            print("商品加入成功")
            car_lit.append(item)
            break
    if num == "q":
        break
    if not _bool:
        print("商品未找到，请输入正确编号")

car_lit.reverse()
for i in car_lit:
    print(i)
