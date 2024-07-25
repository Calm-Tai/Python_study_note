

# 创建一个4行5列的列表
lit = [[j for j in range(5)] for i in range(4)]
for row in lit:
    for item in row:
        print(item,end="\t")

    print()
