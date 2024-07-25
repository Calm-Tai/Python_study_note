

# 求1——100之间的偶数和
i = 1
s = 0  # 初始化

while i <= 100:
    if i % 2 == 1:
        i += 1
        continue
    s += i
    i += 1
print("1——100之间的偶数和为:", s)
