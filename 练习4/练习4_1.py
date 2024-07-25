
s = "helloworld"

for i in range(0, len(s)):  # 正序索引， 0 到N-1
    print(i, s[i], end="\t\t")

print("\n", "-"*100)

for i in range(-len(s), 0):  # 倒序索引，-N到-1
    print(i, s[i], end="\t\t")

print("\n", s[-10], s[0])
