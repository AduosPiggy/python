# Python3.8 新增了一个函数形参语法 
# / 用来指明在此标记之前的所有参数必须使用位置参数传递，不能使用关键字参数。
# * 用来指明在此标记之后的所有参数必须使用关键字参数传递。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

#正确调用
f(10, 20, 30, d=40, e=50, f=60)
f(10, 20, d=30, c=40, e=50, f=60)

#错误调用
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式