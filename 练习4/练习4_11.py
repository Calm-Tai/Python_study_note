# 遍历元组的方法（同列表的三组遍历方法）
t = (10, 20, 45)
for item in t:
    print(item)

for i in range(len(t)):
    print(i, t[i])

for index, item in enumerate(t, start=1):
    print(index, item)
