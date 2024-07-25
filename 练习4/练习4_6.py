lst = [10, 42.5, "hello", "2024"]  # 创建列表

print("原列表：", lst, id(lst))

lst.append(37)
print("新列表", lst, id(lst))

lst.insert(0, 37)  # index 表示序列序号（0到n-1）
print("新列表", lst, id(lst))

a = lst.pop(1)
print("新列表", lst, id(lst), a)

lst.clear()  # 清空列表
print("新列表", lst, id(lst))

lst = list(range(1, 20, 2))
print("原列表", lst, id(lst))
lst.remove(3)
print("新列表", lst, id(lst))

lst.reverse()
print("新列表", lst, id(lst))

lst_copy = lst.copy()
print("复制列表", lst_copy, id(lst))

"""
每个列表都有固定的内存地址，
创建与复制都会产生不同列表并出现新的内存地址
"""

# 修改列表元素
lst_copy[1] = 26
print(lst_copy, id(lst_copy))
