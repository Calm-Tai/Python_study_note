#生成倒三角  高度
h = 5  # 三角形高5
i = h
while i >= 1:
    q = 1
    while q <= i:
        print("*", end="")
        q += 1
    print("")  # 换行
    i -= 1

print("-" * 30)

#生成等腰三角形
"""
&&&&*    4 1
&&&***   3 3
&&*****  2 5
&******* 1 7
"""
h = 5  # 三角形高5
i = h
n = 1
while i >= 1:
    q = 1
    while q <= i:
        print(" ", end="")
        q += 1
    print("*" * (2 * n - 1), end="")
    print("")  # 换行
    i -= 1
    n += 1

print("-" * 30)
# 生成菱形
h = 11  # 菱形高11
i = h //2 # 5
n = 1
while i >= 1:
    q = 1
    while q <= i:
        print(" ", end="")
        q += 1
    print("*" * (2 * n - 1), end="")
    print("")  # 换行
    i -= 1
    n += 1
i = h // 2
n = 1
print("*" * (2 * (i+1) - 1))
while n <= (h//2):
    q = 1
    while q <= n:
        print(" ", end="")
        q += 1
    print("*" * (2 * i - 1), end="")
    print("")  # 换行
    n += 1
    i -= 1
print("-" * 30)
#生成空心菱形
h = eval(input("请输入菱形高度："))
i = h //2 # 5
n = 1
while i >= 1:
    q = 1
    while q <= i:
        print(" ", end="")
        q += 1
    q = 1
    while q <= (2*n -1):
        if q == 1 or q == (2*n -1):
            print("*",end="")
        else:
            print(" ",end="")
        q+=1
    print("")  # 换行
    i -= 1
    n += 1
i = h // 2
n = 1
print("*"," " * (2 * i - 1), "*", sep="")
while n <= (h//2):
    q = 1
    while q <= n:
        print(" ", end="")
        q += 1
    q = 1
    while q <= (2 * i - 1):
        if q == 1 or q == (2*i-1):
            print("*", end="")
        else:
            print(" ", end="")
        q+=1
    print("")  # 换行
    n += 1
    i -= 1
print("-" * 30)