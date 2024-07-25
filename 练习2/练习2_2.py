

num = eval(input("输入数字"))
if num % 2:
    print("是奇数")
else:
    print("是偶数")


x = 'aaa'
if x:
    print("是非空字符串")
else:
    print("是空字符串")

flag = eval(input("请输入一个布尔值"))
if flag:
    print("输入的值为true")
else:
    print("输入的值为false")
print(type(flag))