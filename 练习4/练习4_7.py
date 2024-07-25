import random

lit = [item for item in range(1, 11)]  # 遍历1到11的数字组成列表
print(lit)

lit = [item*item for item in range(1, 11)]
print(lit)

lit = [random.randint(1, 100) for _ in range(10)]  # 生成1到100之间的随机数10次
print(lit)

lit = [i for i in range(1, 20) if i % 2 == 0]  # 遍历i 1到20 筛选出偶数
print(lit)
