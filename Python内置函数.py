#!/usr/bin/env python3
# coding: utf8

import sys

arv = sys.argv[1]

## 返回数字的绝对值。
if 'abs' == arv:
    print("abs(-40) : ", abs(-40))  ## 40
    print("abs(100.10) : ", abs(100.10))  ## 100.1

## all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
## 元素除了是 0、空、None、False 外都算 True。
## all(iterable) iterable -- 元组或列表。
if 'all' == arv:
    print("all(['a', 'b', 'c', 'd']) : ", all(['a', 'b', 'c', 'd']))  ## True
    print("all(['a', 'b', '', 'd']) : ", all(['a', 'b', '', 'd']))  ## False
    print("all([0, 1, 2, 3]) : ", all([0, 1, 2, 3]))  ## False
    print("all(('a', 'b', 'c', 'd')) : ", all(('a', 'b', 'c', 'd')))  ## True
    print("all(('a', 'b', '', 'd')) : ", all(('a', 'b', '', 'd')))  ## False
    print("all((0, 1, 2, 3)) : ", all((0, 1, 2, 3)))  ## False
    print("all([]) : ", all([]))  ## True(特别注意)
    print("all(()) : ", all(()))  ## True(特别注意)

## any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
## 元素除了是 0、空、FALSE 外都算 TRUE。
## any(iterable) iterable -- 元组或列表。
if 'any' == arv:
    print("any(['a', 'b', 'c', 'd']) : ", any(['a', 'b', 'c', 'd']))  ## True
    print("any(['a', 'b', '', 'd']) : ", any(['a', 'b', '', 'd']))  ## True
    print("any([0, '', False]) : ", any([0, '', False]))  ## False
    print("any(('a', 'b', 'c', 'd')) : ", any(('a', 'b', 'c', 'd')))  ## True
    print("any(('a', 'b', '', 'd')) : ", any(('a', 'b', '', 'd')))  ## True
    print("any((0, '', False)) : ", any((0, '', False)))  ## False
    print("any([]) : ", any([]))  ## False
    print("any(()) : ", any(()))  ## False

## 返回一个表示对象的字符串
if 'ascii' == arv:
    print('test')  ## test
    print(ascii('test'))  ## 'test'
    print(type(ascii(['test'])))  ## <class 'str'>

## 返回一个整数 int 或者长整数 long int 的二进制表示
if 'bin' == arv:
    print(bin(10))  ##  0b1010
    print(bin(20))  ##  0b10100

## 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
if 'bool' == arv:
    print(bool())  ## False
    print(bool(0))  ## False
    print(bool(1))  ## True
    print(bool(''))  ## False
    print(bool([]))  ## False
    print(bool({}))  ## False

## 类似于 pdb (Python debugger) 的 断点调试器(仅有 3.7 以后可以)
## 常用命令
## p 计算并打印变量的值，和 print 类似。也可以直接输入变量名回车也会打印变量的值。
## n 下一行，逐行调试的时候可以使用。
## c 继续运行直到下一个断点，也就是 continue 的缩写。
## l 查看断点附近的代码，方便知道目前所处的位置。
## b 后面加行号，就可以动态添加断点了。
## s 进入函数内部。
## r 执行代码直到从当前函数返回。
## q 强制退出，这样的话程序会异常退出。
## commands 其实就是执行任何代码。比如强制改值来测试不同例子。
if 'breakpoint' == arv:
    favourite_ic = 555
    user_guess = input("Try to guess our favourite IC >>> ")
    breakpoint()

    if user_guess == favourite_ic:
        print("Yup, that's our favourite!")
    else:
        print("Sorry, that's not our favourite IC")

if 'bytearray' == arv:
    print()

if 'bytes' == arv:
    print()

## 用于检查一个对象是否是可调用的
## 如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
## 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
if 'callable' == arv:
    print("callable(0) : ", callable(0))  ## False
    print("callable('runoob') : ", callable('runoob'))  ## False


    def add(a, b):
        return a + b


    print("callable(add) : ", callable(add))  ## True


    class A:  ## # 类
        def method(self):
            return 0


    print("callable(A) : ", callable(A))  ## True  类返回 True
    a = A()
    print("callable(a) : ", callable(a))  ## False  没有实现 __call__, 返回 False


    class B:
        def __call__(self):
            return 0


    print("callable(B) : ", callable(B))  ## True
    b = B()
    print("callable(b) : ", callable(b))  ## True  实现 __call__, 返回 True

## chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
if 'chr' == arv:
    print("0x30 : ", chr(0x61))  ## a  十六进制
    print("48 : ", chr(97))  ## a  十进制

## classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
if 'classmethod' == arv:
    class A(object):
        bar = 1

        def func1(self):
            print('foo')

        @classmethod
        def func2(cls):
            print('func2')
            print(cls.bar)
            cls().func1()


    A.func2()  ## func2 1 foo

## compile() 函数将一个字符串编译为字节代码。
## compile(source, filename, mode[, flags[, dont_inherit]])
## source -- 字符串或者AST（Abstract Syntax Trees）对象。
## filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
## mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
## flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
## flags和dont_inherit是用来控制编译源码时的标志
if 'compile' == arv:
    str = "for i in range(0,10): print(i)"
    c = compile(str, '', 'exec')  # 编译为字节代码对象
    print(exec(c))
    str = "3*4+5"
    a = compile(str, '', 'eval')
    print(eval(a))

## complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
if 'complex' == arv:
    print(complex(1, 2))  ## (1 + 2j)
    print(complex(1))  ## (1 + 0j)
    print(complex("1"))  ## (1 + 0j)
    print(complex("1+2j"))  ## (1 + 2j)

## delattr 函数用于删除属性。
if 'delattr' == arv:
    class Coordinate:
        z = 0


    point1 = Coordinate()
    print('z = ', point1.z)
    delattr(Coordinate, 'z')
    print('z = ', point1.z)  ## 触发错误

## dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
if 'dir' == arv:
    print(dir())
    print(dir({}))

## divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
if 'divmod' == arv:
    print(divmod(7, 2))  ## (3, 1)
    print(divmod(8, 2))  ## (4, 0)

## 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
if 'enumerate' == arv:
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enumerate(seasons)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    print(list(enumerate(seasons, start=1)))  # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')] 下标从 1 开始
    string = "daer"
    print(list(enumerate(string)))  # [(0, 'd'), (1, 'a'), (2, 'e'), (3, 'r')]

## 用来执行一个字符串表达式，并返回表达式的值。
if 'eval' == arv:
    string = "pow(2,2)"
    print(eval(string))  ## 4  pow() 方法返回 xy（x的y次方） 的值。
    string = "2 + 2"
    print(eval(string))  ## 4

## 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。
if 'exec' == arv:
    exec('print("Hello World")')  ## Hello World
    exec("""for i in range(3): print("iter time: %d" % i)""")
    # iter time: 0
    # iter time: 1
    # iter time: 2

if 'filter' == arv:
    def is_odd(n):
        return n % 2 == 1


    newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # <filter object at 0x7f9adff54e90>
    print(list(newlist))  # [1, 3, 5, 7, 9]

    import math


    def is_sqr(x):
        return math.sqrt(x) % 1 == 0


    newlist = filter(is_sqr, range(1, 101))
    print(list(newlist))  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## 将整数和字符串转换成浮点数
if 'float' == arv:
    print(float(1))  # 1.0
    print(float(-123.6))  # -123.6
    print(float('123'))  # 字符串 123.0

## 格式化字符串
## 基本语法是通过 {} 和 : 来代替以前的 % 。
if 'format' == arv:
    print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
    print("{0} {1}".format("hello", "world"))  # 设置指定位置
    print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置 world hello world
    print("姓名：{name}, 年龄：{age}".format(name="大明", age=12))  # 姓名：大明, 年龄：12
    person = {"name": "大明", "age": 12}
    ## *args 与 ** kwargs 的区别，两者都是 python 中的可变参数：
    ## *args 表示任何多个无名参数，它本质是一个 tuple
    ## ** kwargs 表示关键字参数，它本质上是一个 dict
    print("姓名：{name}, 年龄：{age}".format(**person))  # 通过字典设置参数
    ## 填充与格式化 :[填充字符][对齐方式 <^>][宽度]
    print('{0:*>10}'.format(10))  ## 右对齐 ********10
    print('{0:*<10}'.format(10))  ## 左对齐 10********
    print('{0:*^10}'.format(10))  ## 居中对齐 ****10****
    ## 精度与进制
    print('{0:.2f}'.format(1 / 3))  # 0.33
    print('{0:b}'.format(10))  # 1010 二进制
    print('{0:o}'.format(10))  # 12 八进制
    print('{0:x}'.format(10))  # a 16进制
    print('{:,}'.format(12369132698))  # 12,369,132,698 千分位格式化
    ## 使用索引
    li = ['hoho', 18]
    print('name is {0[0]} age is {0[1]}'.format(li))  # name is hoho age is 18

## frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。比如列表、字典、元组等等
if 'frozenset' == arv:
    a = frozenset(range(10))  # 生成一个新的不可变集合
    print(a)  # frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = frozenset('runoob')
    print(b)  # frozenset({'o', 'u', 'r', 'n', 'b'})

## 用于返回一个对象属性值。
if 'getattr' == arv:
    class A(object):
        bar = 1

        def set(self, a, b):
            x = a
            a = b
            b = x
            print(a, b)


    a = A()
    print(getattr(a, 'bar'))
    print(getattr(a, 'bar2', 3))  # 属性 bar2 不存在，但设置了默认值
    # print(getattr(a, 'bar2'))  # 属性 bar2 不存在，触发异常
    c = getattr(a, 'set')
    c(a='1', b='2')  # 可以直接使用
    print(A.set(a='1', b='2'))

## globals() 函数会以字典类型返回当前位置的全部全局变量。
if 'globals' == arv:
    print(
        globals())  ## {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f862e87b4d0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '001_内置函数.py', '__cached__': None, 'sys': <module 'sys' (built-in)>, 'arv': 'globals'}

## hasattr() 函数用于判断对象是否包含对应的属性。
if 'hasattr' == arv:
    class Coordinate:
        x = 10
        y = -5
        z = 0


    point1 = Coordinate()
    print(hasattr(point1, 'x'))  ## True
    print(hasattr(Coordinate, 'x'))  ## True

if 'hash' == arv:
    print()
if 'help' == arv:
    print()
if 'hex' == arv:
    print()
if 'id' == arv:
    print()
if 'input' == arv:
    print()
if 'int' == arv:
    print()
if 'isinstance' == arv:
    print()
if 'issubclass' == arv:
    print()
if 'iter' == arv:
    print()
if 'len' == arv:
    print()
if 'list' == arv:
    print()
if 'locals' == arv:
    print()
if 'map' == arv:
    print()
if 'max' == arv:
    print()
if 'memoryview' == arv:
    print()
if 'min' == arv:
    print()
if 'next' == arv:
    print()
if 'object' == arv:
    print()
if 'oct' == arv:
    print()
if 'open' == arv:
    print()
if 'ord' == arv:
    print()
if 'pow' == arv:
    print()
if 'print' == arv:
    print()
if 'property' == arv:
    print()
if 'range' == arv:
    print()
if 'repr' == arv:
    print()
if 'reversed' == arv:
    print()
if 'round' == arv:
    print()
if 'set' == arv:
    print()
if 'setattr' == arv:
    print()
if 'slice' == arv:
    print()
if 'sorted' == arv:
    print()
if 'staticmethod' == arv:
    print()
if 'str' == arv:
    print()
if 'sum' == arv:
    print()
if 'super' == arv:
    print()
if 'tuple' == arv:
    print()
if 'type' == arv:
    print()
if 'vars' == arv:
    print()
if 'zip' == arv:
    print()
if 'import' == arv:
    print()
