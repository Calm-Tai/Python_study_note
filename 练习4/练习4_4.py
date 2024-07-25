# 两种创建列表的方法
lit1 = [12, "hello", 112.4, True]
print(lit1)

lit2 = list("helloworld")
lit3 = list(range(1, 20, 2))
print(lit2)
print(lit3)

# 列表是序列的一种，所以可以对列表干所有列表能干的事情
print(lit1+lit2+lit3)
print(lit2*2)
print(lit2[1:10:2])
print("s" in lit2)
print(lit2.index("e"))
print(lit2.count("e"))
