#!/usr/bin/evn python3
# -*-encoding=utf-8-*-

import sys

arg_1 = sys.argv[1]

if 'print' == arg_1:
    print(r'''hello,\n world''')  # hello,\n world

if "'''" == arg_1:
    print(r'''Hello,
Lisa!''')  # 前后 ' 必须保持一致
# Hello,
# Lisa!

if "%" == arg_1:
    print('%2d-%02d' % (3, 1))  # 3-01 (3前面有空格)
    print('%.2f' % 3.1415926)  # 3.14 （小数截断）
    print('growth rate: %d %%' % 7)  # growth rate: 7 %  (用%%来表示一个%)
# 1、%d就是普通的输出了
# 2、%2d是将数字按宽度为2，采用右对齐方式输出，若数据位数不到2位，则左边补空格。如下：
# 3、%02d，和% 2d差不多，只不过左边补0
# 4、%.2d从执行效果来看，和% 02d一样
# 5、%2f是把float的所有位数输出2位,包括小数点,如果不组2位,补0,如果超过2位,按照实际输出
# 6、%.2f是float后的小数只输出两位。

if 'list' == arg_1:
    list = ['Michael', 'Bob', 'Tracy']  # 定义一个列表
    print("列表长度：%s" % len(list))  # 列表长度：3
    print("列表第一个元素：%s " % list[0])  # 列表第一个元素：Michael
    print("列表最后一个元素：%s" % list[-1])  # 列表最后一个元素：Tracy
    # print("超出返回报错：%s" % list[4])  # IndexError: list index out of range
    list.append('Tim')  # 追加元素到末尾
    list = ['Michael', 'Bob', 'Tracy']  # 定义一个列表
    list.insert(1, 'jack')  # 插入元素到指定位置， 后面的元素顺序往后移动
    print("insert的结果：%s" % list)  # ['Michael', 'jack', 'Bob', 'Tracy']
    list.pop()  # 删除list末尾的元素
    list.pop(1)  # 删除指定索引位置的元素
    list = ['Michael', 'Bob', 'Tracy']  # 定义一个列表
    list[1] = 'sara'  # 替换指定索引位置的元素，注意与insert的区别
    print("替换指定索引位置的元素：%s" % list)  # ['Michael', 'sara', 'Tracy']
    # s= ['sting',1,True,['one','two']] #列表可以存储不同的类型的数据 以及多维数组表示方式

if 'tuple' == arg_1:
    tuple_1 = ('Michael', 'Bob', 'Tracy')  # 定义一个元组  元组一旦初始化就不能修改。它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
    print("初始化元组：{}".format(tuple_1))
    tuple_2 = ()  # 空元组
    print("空元组：{}".format(tuple_2))
    tuple_3 = (1,)  # 一个元素的tuple定义，','逗号不能少
    print("一个元素的元祖定义需要注意了！：{}".format(tuple_3))
    t = ('a', 'b', ['A', 'B'])  # 元组内部 可定义列表  列表内容是可修改的
    t[2].append('C')
    print("元祖内的列表被修改了：{}".format(t))

if 'if' == arg_1:
    age = 3
    # age= input('age:')
    # age = int(age)  # 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。
    if age >= 18:
        print('成年人')
    elif age >= 6:
        print('年轻人')
    else:
        print('小孩')

if 'for' == arg_1:
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)

if 'range' == arg_1:
    print('经过list转换的range序列: {}'.format(list(range(5))))  # [0, 1, 2, 3, 4] (range() 函数生成一个整数序列  list(函数)将这序列转成list)
    print('range序列: {}'.format(range(5)))  # range(0, 5)  (貌似3后不需要list转换了，也是list)
    # 计算0~100的和
    sum = 0
    for x in range(101):
        sum = sum + x
    print("0~100的和：%d" % sum)

if 'while' == arg_1:
    ## 1-10的偶数
    n = 1
    while n <= 10:
        if n % 2 == 0:
            # break  # break语句会结束当前循环
            print(n)
        n = n + 1
    print('END')

if 'dict' == arg_1:
    # 字典（dict）也称为map  (key-value)存储 查找速度快
    name_age = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  # 定义一个dict
    print('Michael的年龄:%d' % name_age['Michael'])
    name_age['Michael'] = 90  # 重新赋值
    print('Michael修改后的年龄:%d' % name_age['Michael'])
    if 'Tomi' in name_age:  # 通过in判断key是否存在  如果不先判断 key不存在 会报错 KeyError: 'Thomas'
        print("Tomi在元组中")
    else:
        print("Tomi不在元组中")
    print('不存在的元素{}'.format(name_age.get('Tomi')))  # 第二种获取值的方法 如果不存在 返回none
    print('如果不存在 就返回默认值{}'.format(name_age.get('Tomi', -1)))
# 和list比较，dict有以下几个特点：
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。

if 'set' == arg_1:
    # set 和 dict 类似  不过不存储value  只存储key  且 key不能重复（数学中集合的概念）
    s = set([1, 2, 3])  # 要创建一个set，需要提供一个list作为输入集合
    print("set会自动过滤重复的值：{}".format(set([1, 1, 2, 2, 3, 3])))  # set([1, 2, 3]) 重复的元素被自动过滤
    s.add(4)  # 给set中添加元素
    s.add(4)  # 可重复添加 不过没有效果
    s.remove(4)  # 删除元素
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print("s1和s2的交集：{}".format(s1 & s2))  # set([2, 3]) (集合的交集)
    print("s1和s2的并集：{}".format(s1 | s2))  # set([1, 2, 3, 4]) (集合的并集)
# set的原理和dict一样，所以，同样不可以放入可变对象（无法判断两个可变变量是否相等，也就无法保证set内部“不会有重复元素”）
# str是不变对象，而list是可变对象


if 'replace' == arg_1:
    a = 'abc'
    b = a.replace('a', 'A')
    print("替换后的新对象：%s" % b)  # Abc (对于不变对象来说  调用任何方法 并不改变该对象内容  只是生成了一个新的对象)
    print("旧对象依旧不变：%s" % a)  # abc

if 'yield' == arg_1:
    # 带有 yield 的函数在 Python 中被称之为 generator（生成器）
    # 输出斐波那契數列前 N 个数
    def fab(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a + b
            n = n + 1


    fab(5)


    # 直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。

    # 使用 yield 输出斐波那契數列前 N 个数
    def fab(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b  # 使用yield
            # print(b)
            a, b = b, a + b
            n = n + 1


    print(fab(5))  # <generator object fab at 0x7ff376d44af0>

    for n in fab(5):
        print(n)
