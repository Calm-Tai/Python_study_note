year = [89, 99, 23, 00, 34]
Year = []
# for i in range(len(year)):  # 第一种方法
#     if year[i] != 0:
#         Year.append("19" + str(year[i]))
#     else:
#         Year.append("200" + str(year[i]))
# print(year)
# print(Year)

for index, item in enumerate(year, 0):  # 第二种
    if year[index] != 0:
        Year.append("19" + str(year[index]))
    else:
        Year.append("200" + str(year[index]))
print(year)
print(Year)
