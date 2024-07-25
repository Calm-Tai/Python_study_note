
"""
通过 二分法 得出 根号2 的估值
"""

num = eval(input("输入num"))
a, b = 0, num+1
c = (a + b) / 2

for i in range(1, 20):
    if c ** 2 > num:
        b = c
        c = (a + b) / 2
    elif c ** 2 < num:
        a = c
        c = (a + b) / 2
    else:
        break

print("近似数为", c)