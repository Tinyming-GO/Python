#!/usr/bin/python

#print(r'''hello,\n world''') # hello,\n world

#print(r'''Hello,
#Lisa!''') 
#Hello,
#Lisa!
#前后 ' 必须保持一致


#print('%2d-%02d' % (3,1)) #  3-01
#print('%.2f' % 3.1415926) # 3.14
#print('growth rate: %d %%' % 7) # growth rate: 7 %   # 用%%来表示一个%
#1、%d就是普通的输出了 
#2、% 2d是将数字按宽度为2，采用右对齐方式输出，若数据位数不到2位，则左边补空格。如下：
#3、% 02d，和% 2d差不多，只不过左边补0
#4、%.2d从执行效果来看，和% 02d一样
#5、%2f是把float的所有位数输出2位,包括小数点,如果不组2位,补0,如果超过2位,按照实际输出
#6、%.2f是float后的小数只输出两位。


#list
#list = ['Michael', 'Bob', 'Tracy'] #定义一个列表
#print(len(list)) # 3  长度
#print(list[0]) # Michael  第一个元素
#print(list[-1]) # Tracy  最后一个元素
#print(list[4]) # list index out of range  超过范围报错
#list.append('Tim') # 追加元素到末尾
#list.insert(1,'jack') # 插入元素到指定位置， 后面的元素顺序往后移动
#list.pop() # 删除list末尾的元素
#list.pop(1) # 删除指定索引位置的元素
#list[1] = 'sara' # 替换指定索引位置的元素，注意与insert的区别
#s= ['sting',1,True,['one','two']] #列表可以存储不同的类型的数据 以及多维数组表示方式


#tuple
#tuple = ('Michael', 'Bob', 'Tracy') #定义一个元组  元组一旦初始化就不能修改。它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
#tuple = （）# 空元组
#tuple=(1,) #一个元素的tuple定义 print输出 （1，）
#int=(1) # 数学公式中的小括号  print输出 1
#t = ('a', 'b', ['A', 'B'])  # 元组内部 可定义列表  列表内容是可修改的


#条件判断（if elif else）
#age = 3
#if age >= 18:
#    print('adult')
#elif age >= 6:
#    print('teenager')
#else:
#    print('kid')


#birth= input('birth:')
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')
#TypeError: unorderable types: str() > int()  因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情


#循环（for x in ...）（while break continue）
#names = ['Michael', 'Bob', 'Tracy']
#for name in names:
#    print(name)

#print(list(range(5)))  #[0, 1, 2, 3, 4] range() 函数生成一个整数序列  list(函数)将这序列转成list
#print(range(5)) range(0, 5)

#sum = 0
#for x in range(101):
#    sum = sum + x
#print(sum) #5050 计算0~100的和

#n = 1
#while n <= 100:
#    if n > 10: # 当n = 11时，条件满足，执行break语句
#        break # break语句会结束当前循环
#    print(n)
#   n = n + 1
#print('END') #打印出1~10后，紧接着打印END，程序结束。


#字典（dict）也称为map  (key-value)存储 查找速度快
#d = {'Michael': 95, 'Bob': 75, 'Tracy': 85} #定义一个dict
#d['Michael'] #查找
#d['Michael'] = 90 #重新赋值
#print('Thomas' in d)  #false 通过in判断key是否存在  如果不先判断 key不存在 会报错 KeyError: 'Thomas'
#print(d.get('Thomas'))  #none  第二种获取值的方法 如果不存在 返回none
#d.get('Thomas', -1)  #如果不存在 就返回默认值 -1

#和list比较，dict有以下几个特点：
#1、查找和插入的速度极快，不会随着key的增加而变慢；
#2、需要占用大量的内存，内存浪费多。


#set  和dict类似  不过不存储value  只存储key  且 key不能重复（数学中集合的概念）
#s = set([1, 2, 3]) # 要创建一个set，需要提供一个list作为输入集合
#print(set([1, 1, 2, 2, 3, 3]))  #{1, 2, 3}  重复的元素被自动过滤
#s.add(4) # 给set中添加元素 可重复添加 不过没有效果
#s.remove(4) # 删除元素
#s1 = set([1, 2, 3])
#s2 = set([2, 3, 4])
#print(s1 & s2)  #{2, 3}  集合的交集
#print(s1 | s2)  #{1, 2, 3, 4}  集合的并集


#set的原理和dict一样，所以，同样不可以放入可变对象（无法判断两个可变变量是否相等，也就无法保证set内部“不会有重复元素”）
#str是不变对象，而list是可变对象


#a = 'abc'
#b = a.replace('a', 'A')
#print(b) #Abc  #对于不变对象来说  调用任何方法 并不改变该对象内容  只是生成了一个新的对象
#print(a) #abc









