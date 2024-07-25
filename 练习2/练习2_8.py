
Name = input("请设置您的姓名:")
Keyword = input("请输入您的密码:")  #获取姓名与密码
print("-"*40)
name = input("请输入您的姓名:")
keyword = input("请输入您的密码:")  #登录获取姓名与密码

for i in range(1,4): #登录三次机会
    if i < 3:
        if name == Name and keyword == Keyword:
            print("登录成功")
            break
        else:
            print("账号或密码错误，请重试...","(还有", (3 - i), "次机会)",sep="")
            print("-"*40)
            name = input("请输入您的姓名:")
            keyword = input("请输入您的密码:")  # 登录获取姓名与密码

            i += 1
    else:
        print("登录失败")
        break
