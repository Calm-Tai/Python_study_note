# 使用大括号创建字典
d = {30: "iud", 20: "aaa"}
print(d)  # 字典key相同， 值进行了覆盖

lit1 = [10, 20, 30, 40]
lit2 = ["cat", "dog", "mouse", "key", "monkey"]
zipobj = zip(lit1, lit2)
print(zipobj)  # <zip object at 0x000002368D6EF380> zip类型，不能看到其中内容
lit = list(zipobj)
print(lit)  # 转换为列表类型
'''
[(10, 'cat'), (20, 'dog'), (30, 'mouse'), (40, 'key')]
发现字典每一个键值对都被转换为列表中的一个元素，且元素是一个元组类型
'''
dit = dict(lit)  # 将列表转换为字典类型
print(dit)  # {10: 'cat', 20: 'dog', 30: 'mouse', 40: 'key'}

#使用参数创建字典
d = dict(cat=20, dog=30)
print(d)  # {'cat': 20, 'dog': 30}  左侧是key 右侧是value

# 以元组作为字典key 因为key需要不可变数据类型
t = (10, 20, 30)
print({t: 20})  # {(10, 20, 30): 20}
#列表不可作为key，因为列表为可变数据类型
