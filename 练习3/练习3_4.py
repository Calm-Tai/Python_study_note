

money = 888.88
data = 888
time = 588

while True:
    print("-" * 10, "欢迎使用10086查询功能", "-" * 10, sep="")
    print("输入1， 查询余额")
    print("输入2， 查询流量")
    print("输入3， 查询通话剩余时间")
    print("输入0， 退出查询")
    choice = input("请输入将执行操作：")
    if choice == "1":
        print("当前余额：", money, "元")
    elif choice == "2":
        print("当前剩余流量：", data, "G")
    elif choice == "3":
        print("当前剩余通话时间：", time, "min")
    else:
        print("已退出咨询")
        break
    again_choice = input("请问还要继续咨询吗？（y/n）：")
    if again_choice == "y":
        pass
    else:
        print("已退出咨询")
        break

