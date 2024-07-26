import random

d = {item: random.randint(1, 100) for item in range(4)}
print(d)

lit1 = [10, 20, 30]
lit2 = [23, 12, 34]
d = {key: value for key, value in zip(lit1, lit2)}
print(d)