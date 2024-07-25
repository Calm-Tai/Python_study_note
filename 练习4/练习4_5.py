lit = ["mmm", "hello", 15, 370.40]

# 遍历三种形式
for item in lit:
    print(lit[item])  # 通过item遍历于序列中

for i in range(0, len(lit)):
    print(i, "-->", lit[i])  # for循环加索引

for index, item in enumerate(lit):
    print(index, item)
"""
for循环加enumerate()函数进行枚举， 
index表示序号而非索引！！
"""

for index, item in enumerate(lit, start=1):  # 可通过修改start来改变序列初始值
    print(index, item)

for index, item in enumerate(lit, 1):  # start也可以省略
    print(index, item)
