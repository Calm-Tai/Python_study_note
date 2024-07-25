d = {1001: "aaa", 1002: "bbb", 1003: "ccc"}  # {1001: 'aaa', 1002: 'bbb', 1003: 'ccc'}
print(d)
d[1004] = "ddd"  # 通过赋值给字典添加键值对
print(d)  # {1001: 'aaa', 1002: 'bbb', 1003: 'ccc', 1004: 'ddd'}

keys = d.keys()  # 获取字典所有key
print(keys)  # dict_keys([1001, 1002, 1003, 1004])
print(list(keys))  # [1001, 1002, 1003, 1004]
print(tuple(keys))  # (1001, 1002, 1003, 1004)

values = d.values()  # 获取字典所有value
print(values)  # dict_values(['aaa', 'bbb', 'ccc', 'ddd'])
print(list(values))  # ['aaa', 'bbb', 'ccc', 'ddd']
print(tuple(values))  # ('aaa', 'bbb', 'ccc', 'ddd')

lit = list(d.items())
print(lit)  # [(1001, 'aaa'), (1002, 'bbb'), (1003, 'ccc'), (1004, 'ddd')]
# 通过items()函数以元组形式获取键值对并转换为列表作为元素

d = dict(lit)  # 再次转化为字典类型
print(d)

d.pop(1001)  # 取出键值对
print(d)  # {1002: 'bbb', 1003: 'ccc', 1004: 'ddd'}
print(d.pop(1008, "不存在"))  # 取出不存在的键值对，取默认值   不存在


#取出最后一对键值对
print(d.popitem())  # (1004, 'ddd')
print(d)  # {1002: 'bbb', 1003: 'ccc'}

d.clear()  # 清空字典
print(bool(d))  # False
