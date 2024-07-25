
fp = open("Calm.txt", "w") #使用open函数创建Calm.txt文件，w 意为write 写入
print("hello, Calm.", file=fp) #通过print函数写入信息
fp.close()#关闭文件