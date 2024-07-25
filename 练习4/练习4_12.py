t = (i for i in range(1, 4))
print(t)  # 得到一个生成器
# t = tuple(t)  # 转化为元组
# print(t)

print(t.__next__())
print(t.__next__())
print(t.__next__())

t = tuple(t)
print(t)  # 元组为空， 因为__next__()函数已经把元素全都取出来了
