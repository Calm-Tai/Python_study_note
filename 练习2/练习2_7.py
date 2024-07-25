
a =1
answer = input("今天要上课吗？（yes/no）：")
i = 1
while a == 1:


    if answer == "yes":
        if i == 1:
            print("好好学习，天天向上")
            i = 2
            answer = input("下课了，你要出去走走吗？：")
        elif i == 2:
            print("遛狗时间，讲性修睦")
            i = 3
            answer = input("你看到黄愯塏了，要强奸他吗？：")
        elif i == 3:
            print("黄忠林气得让你连上20节课，你鼠了")
            break
    else:
        if i == 1:
            i = 1
            print("你必须上学，好好学习天天向上")
            answer = input("你要上课吗？：")
        elif i == 2:
            print("20分钟过去了")
            i = 1
            answer = input("继续上课吗？")
        elif i == 3:
            print("不草是吧，他说你照片好丑（嬉笑）")
            i = 1
            answer = input("继续上课吗？")