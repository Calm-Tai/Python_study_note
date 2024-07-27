# 集合由{}创建，无序，唯一
s1 = {10, 20, 30}
print(s1)  # {10, 20, 30}
s1 = {10, 20, 10, 30}
print(s1)  # {10, 20, 30}

# 也可以通过set()进行创建
s2 = set("helloworld")
print(s2)  # {'e', 'd', 'w', 'o', 'l', 'h', 'r'}  可见无序特点，只存在一个o可见其”唯一“特点

s3 = set()
print(s3, type(s3), bool(s3))  # set() <class 'set'> False 由此可创建一个空集合

s4 = {}
print(s4, type(s4), bool(s4))  # {} <class 'dict'> False 空大括号只能创建空字典

del s4  # 删除集合
