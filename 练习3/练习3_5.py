import random

num = random.randint(1, 100)  # 随机获取1到100之间的数字
times = 0

while True:
    answer = eval(input("请输入数字："))
    if answer > num:
        print("猜大了")
        times += 1
    elif answer < num:
        print("猜小了")
        times += 1
    else:
        times += 1
        print("恭喜你，你猜中了,共猜的次数为：", times)
        again = input("是否再来？（y/n）:")
        if again == "y":
            num = random.randint(1, 100)
            times = 0
        else:
            break
