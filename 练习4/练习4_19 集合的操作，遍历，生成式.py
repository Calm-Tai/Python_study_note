s1 = {10, 20, 30, 40}
s1.add(43)  # 增加元素
print(s1)  # {40, 10, 43, 20, 30}
s1.add(20)  # 如果元素重复，则不增加任何元素
print(s1)  # {40, 10, 43, 20, 30}

s1.remove(20)  # 删除元素，若元素不存在则抱报错
print(s1)  # {40, 10, 43, 30}

s1.clear()  # 删除所有元素
print(s1)  # set()

s2 = {10, 20, 30, 40}
for i in s2:
    print(i, end="\t")  # 40   10	20	30
print()

for index, item in enumerate(s2):
    print(index, item)
    # 0 40
    # 1 10
    # 2 20
    # 3 30

s3 = {i for i in range(1, 11)}
print(s3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s3 = {i for i in range(1, 51) if i % 2 == 0}
print(s3)  # {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50}
