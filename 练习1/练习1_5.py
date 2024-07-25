

hello = "北京欢迎你"
print(eval("hello"))

a = 15
print(a)
a +=5
print(a)
a *=3
print(a)
y = 3
a /= y
print(a)
print(type(a))
print(type(y))
a //= 3
print(a,type(a))

#python存在链式赋值
a = b = c =100
print(a,b,c)

#也有解包赋值
a,b = 10,20 #a = 10, b = 20
print(a,b)

#可以用解包赋值进行变量间的数值交换
a,b =b,a #a = b, b = a
print(a,b)