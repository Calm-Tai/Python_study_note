

for i in "hello":
    print(i)

for i in range(1, 11):  #range函数可依次生成n 到 m的整数，不包含m
    print(i)

print("-"*40)
s = 0
for i in range(1, 11):
    s += i
print(s)

print("-"*20, "100到999的水仙花数","-"*20,sep= "-")
for i in range(100, 1000):
    c = i % 10
    b = i // 10 % 10   # 123 // 10 = 12 , 12 % 10 = 2
    a = i // 100

    if c**3 + b**3 + a**3 == i:
        print(i)