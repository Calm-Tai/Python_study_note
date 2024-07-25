
# 直接用括号创建元组
t = (123, "hello", [10, 28, 34], "hi哈哈")
print(t)

# 使用内置函数创建元组
t = tuple("helloworld")
print(t)

t = tuple([[10, 10, 20], [24, 56, 10], [43, 56, 70, 13], [10000, 10, 10, 10, 10, 10]])
print(t)

print("10 在元组t中是否存在：", (10 in t))
print("10 在元组t中是否不存在：", (10 not in t))
print("t元组中的最大值：", (max(t)))
print("t元组中的最小值：", (min(t)))
print("元组t的长度：", len(t))
print("元组t中第一次出现的序列位置：", t.index([10, 10, 20]))
print("列表[10, 10, 20]在元组t中出现的次数", t.count([10, 10, 20]))

# 如果元组中只有一个元素
t = (10)
print(t, type(t))
t = (10,)
print(t, type(t))

del t  # 元组的删除
