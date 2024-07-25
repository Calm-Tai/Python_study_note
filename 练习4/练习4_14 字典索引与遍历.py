# 使用d[key] 索引
d = {"python": 20, "lala": 30, "will": 34}
print(d["python"])  # 20

# 使用d.get(key) 索引
print(d.get("python"))  # 20

# 两者存在一定区别，d[key] 不可索引不存在的key，会报错， 但d.get(key) 会输出默认值
#print(d["java"])  # KeyError: 'java'
print(d.get("java"))  # None
print(d.get("java", "不存在"))  # 不存在

# 遍历字典
for item in d.items():
    print(item)
    '''
('python', 20)
('lala', 30)
('will', 34)
会将字典以key = value 的形式形成元组输出
    '''
for key, value in d.items():
    print(key, value)
'''
python 20
lala 30
will 34
分别索引相对应的key和value
'''
