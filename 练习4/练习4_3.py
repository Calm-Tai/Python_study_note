s = "helloworld"
print("e在helloworld中存在吗？", ("e" in s))  # in的使用
print("v在helloworld中存在吗？", ("v" in s))

print("e在helloworld中不存在吗？", ("e" not in s))  # not in的使用
print("v在helloworld中不存在吗？", ("v" not in s))

# 内置函数的使用
print("len()", len(s))  # 序列长度
print("max()", max(s))  # 序列最大值
print("min()", min(s))  # 序列最小值

# 序列名称加点调用
print("s.index()", s.index("o"))  # 第一次出现o的序列位置
print("s.count()", s.count("o"))  # o在序列中出现的次数
