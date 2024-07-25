

#正方形
for i in range(1,5):
    for q in range(1,5):
        print("*",end="")
    print("")
print("-"*30)

#正三角
for i in range(1,5):
    print("*"*i)
print("-"*30)

#倒三角
i =1
q = 4
while i <=5:

    print("*"*q)
    q -= 1
    i += 1
print("-"*30)

#等腰三角形
i = 1
q = 4
while i <= 5:
    print(" "*q, end="")
    print("*"*(2*i-1))
    i += 1
    q -= 1
print("-"*30)

#生成菱形
while 1:
    i = eval(input("请输入菱形行数:"))
    if i % 2:
        h = 1
        H = i // 2
        q = H
        while h <= H:
            print(" " * q, end="")
            print("*" * (2 * h - 1))
            h += 1
            q -= 1
        print("*"*(2 * (H+1) - 1))
        h = 1
        q = 1
        while h <= H:
            print(" " * q, end="")
            print("*" * ((2 * H - 1) - 2*(h-1)))
            h += 1
            q += 1
        break
    else:
        print("请输入奇数...")
print("-"*30)

#生成空心菱形
while 1:
    i = eval(input("请输入菱形行数:"))
    if i % 2:
        h = 1
        H = i // 2 - 1
        q = H
        print(" "*q,"*")
        while h <= H:
            print(" " * q, end="")

            print("*"," "*(2 * h - 1),"*",sep="")

            h += 1
            q -= 1
        print("*"," "*(2 * (H+1) - 1),"*",sep="")
        h = H
        q = 1
        while h >= 1:
            print(" " * q, end="")
            print("*"," " * (2 * h - 1),"*",sep="")
            h -= 1
            q += 1
        print(" "* q, "*",sep="")
        break
    else:
        print("请输入奇数...")

