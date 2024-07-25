

#输入
r = float(eval(input("输入圆的半径:")))

#处理
PI = 3.14        #常量PI
C =round(2 * PI * r)   #计算周长
S =round(PI * r**2)    #计算面积

#输出
print("圆的周长是:", C)
print("圆的面积是:", S)
d