# 基础

## 注释

`print('hello	world')	# 注意到 print 是一个函数`

## 字面常量
## 数字
## 字符串
- 单引号
- 双引号
- 三引号：你可以通过使用三个引号—— """ 或 ''' 来指定多行字符串。

```python
'''这是一段多行字符串。这是它的第一行。
This is	the	second line.
"What's	your name?," I asked.
He said "Bond, James Bond."
'''
```
## 字符串是不可变的
## 格式化方法

构建字符串，使用`format()`方法。

```python
age  = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this	book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
```

输出:

```
Swaroop was 20 years old when he wrote this book
Why is Swaroop playing with that python?
```

注意数字只是一个可选选项:

```python
age  = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this	book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
```

`format()` 方法 更详细的格式,例如:

```python
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本,并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

输出:

```
0.333
___hello___
Swaroop wrote A Byte of Python
```

※ print 总是会以一个不可见的“新一行”字符( \n )。为防止打印过程中出现这一换行符,你可以通过 end 指定其应以空白结尾:

```python
print('a', end='')
print('b', end='')
```

输出:

```
ab
```

## 转义序列
## 原始字符串

在字符串前增加`r`或`R`来指定一个 原始(Raw) 字符串：

```python
r"Newlines are indicated by \n"  # \n 将不会被转义
```

## 变量
## 标识符命名

变量是标识符的一个例子。标识符(Identifiers)	是为	某些东西	提供的给定名称。

- 第一个字符必须是字母表中的字母或下划线( _ )。
- 标识符的其它部分可以由字符下划线( _ )、数字(0~9)组成。
- 标识符名称区分大小写。例如, myname 和 myName 并不等同。

## 数据类型
## 对象

需要记住的是 , Python 将程序中的任何内容统称为`对象(Object)`。

## 案例:使用变量与字面常量

```python
# 文件名:var.py
i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)
```

输出:

```
5
6
This is a multi-line string.
This is the second line.
```

## 逻辑行与物理行

尽量保证 一 物理行 对应一个 逻辑行（不使用分号；）。

如果你有一行非常长的代码,你可以通过使用反斜杠将其拆分成多个物理行。这被称作`显式行连接`

```python
s = 'This is a string. \
This continues the string.'
print(s)
```

输出：

```
This is a string. This continues the string.
```

## 缩进

每一组这样的语句被称为 `块(block)`。Python 将始终对块使用缩进,并且绝不会使用大括号。

# 运算符与表达式

表达式可以拆分成`运算符(Operators)`与`操作数(Operands)`。

## 运算符

- \+ (加)
- \- (减)
- \* (乘)
- \*\* (乘方) eg： 3 \*\* 4 输出 81 (即 3 \* 3 \* 3 * 3 )。
- / (除)
- // (整除) eg： 13 // 3 输出 4 。
- % (取模)
- << (左移)
- - 将数字的位向左移动指定的位数。(每个数字在内存中以二进制数表示,即 0 和 1 )
- - 2 << 2 输出 8 。 2 用二进制数表示为 10 。
- - 向左移 2 位会得到 1000 这一结果,表示十进制中的 8 。
- (右移)
- & (按位与)
- - 5 & 3 输出 1 。
- | (按位或)
- - 5 | 3 输出 7 。
- ^	(按位异或)
- - 5 ^ 3 输出 6 。
- ~ (按位取反)
- - x 的按位取反结果为 -(x+1)。
- - ~5 输出 -6 。
- < (小于) 比较可以任意组成组成链接: 3 < 5 < 7 返回 True 。（所有的比较运算符返回的结果均为 True 或 False ）
- \> (大于)
- <= (小于等于)
- \>= (大于等于)
- == (等于)
- != (不等于)
- not (布尔“非”)
- and (布尔“与”)  作短路计算
- or (布尔“或”)

## 数值运算与赋值的快捷方式

`a = a * 3	<==>  a *= 3`

## 求值顺序 运算符的优先级

## 改变运算顺序  使用括号

## 结合性  同优先级的运算符从左至右依次求值

## 表达式

```python
length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
```

输出:

```
Area is 10
Perimeter is 14
```

# 控制流

## 	if 语句

```python
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新块在这里结束
elif guess < number:
    # 另一代码块
    print('No,	it	is	a	little	higher	than	that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No,	it	is	a	little	lower	than	that')
    # 你必须通过猜测一个大于(>)设置数的数字来到达这里。
print('Done')
# 这最后一句语句将在
# if 语句执行完毕后执行。
```

输出:

```
Enter an integer : 50
No, it is a little lower than that
Done
```

一个最小规模且有效的 `if 语句` 是这样的:

```python
if True:
 	print('Yes, it is true')
```

## while 语句

`while 语句`同样可以拥有`else 子句`作为可选选项！！！！

```python
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations,	you	guessed	it.')
        # 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No,	it	is	a	little	higher	than	that.')
    else:
        print('No,	it	is	a	little	lower	than	that.')
else:
    print('The	while	loop	is	over.')
# 在这里你可以做你想做的任何事
print('Done')
```

输出:

```
$ python while.py
Enter an integer	:	50
No,	it	is	a	little	lower	than	that.
Enter an integer	:	22
No,	it	is	a	little	higher	than	that.
Enter an integer	:	23
Congratulations,	you	guessed	it.
The	while loop is over.
Done
```

## 	for 循环

```python
for i in range(1, 5): # range(1,5) 将输出序列 [1, 2, 3, 4] 。 range(1,5,2) 将会输出 [1, 3] 。
    print(i)
else:
    print('The for loop is over')
```

输出:

```
$ python for.py
1
2
3
4
The for loop is over
```

另外需要注意的是,`range()`每次只会生成一个数字,如果你希望获得完整的数字列表,要在使用`range()`时调用`list()`。例如下面这样: `list(range(5))`,它将会返回 [0, 1, 2, 3, 4] 。

## 	break 语句

## 	continue 语句

# 函数

函数可以通过关键字`def`来定义。

```python
def say_hello():
    # 该块属于这一函数
    print('hello world')
# 函数结束

say_hello()  # 调用函数
say_hello()  # 再次调用函数
```

输出:

```
$ python function1.py
hello world
hello world
```

## 函数参数

要注意在此使用的术语——在定义函数时给定的名称称作`“形参”(Parameters)`,在调用函数时你所提供给函数的值称作`“实参”(Arguments)`。

```python
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# 直接传递字面值
print_max(3, 4)
x = 5
y = 7
# 以参数的形式传递变量
print_max(x, y)
```

输出:

```
$ python function_param.py
4 is maximum
7 is maximum
```

## 局部变量

所有变量的`作用域`是它们被定义的`块`

## global 语句

你可以在同一句 global 语句中指定不止一个的全局变量,例如`global	x, y, z`。

## 默认参数值

要注意到,默认参数值应该是`常数`！！！更确切地说,默认参数值应该是`不可变的`！！！

```python
def say(message, times=1):
    print(message * times)
```

>※ 只有那些位于参数列表末尾的参数才能被赋予默认参数值,意即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前。
>
>这是因为值是按参数所处的位置依次分配的。举例来说,`def func(a, b=5)`是有效的,但 def func(a=5, b) 是无效的。

## 关键字参数

我们使用命名(关键字)而非位置(一直以来我们所使用的方式)来指定函数中的参数。

这样做有两大优点——其一,我们不再需要考虑参数的顺序,函数的使用将更加容易。其二,我们可以只对那些我们希望赋予的参数以赋值,只要其它的参数都具有默认参数值。

```python
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


func(3, 7)
func(25, c=24)  # 注意这顺序是乱的
func(c=50, a=100)  # 注意这顺序是乱的
```

输出:

```python
$ python function_keyword.py
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50
```

## 可变参数

想定义的函数里面能够有任意数量的变量,也就是参数数量是可变的

```python
def total(a=5, *numbers, **phonebook):

    print('a', a)

    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
```

输出:

```
$ python function_varargs.py
a 10
single_item 1
single_item 2
single_item 3
Inge 1560
John 2231
Jack 1123
None
```

## 	return 语句

如果 return 语句没有搭配任何一个值则代表着`返回 None`。每一个函数都在其末尾隐含了一句 return None ,除非你写了你自己的 return 语句。

```python
def some_function():
    pass
```

※ Python 中的 pass 语句用于指示一个没有内容的语句块。

## DocStrings

Python 有一个甚是优美的功能称作文档字符串(Documentation	Strings),在称呼它时通常会使用另一个短一些的名字docstrings。

```python
def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能,将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
```

输出:

```
$ python function_docstring.py
5 is maximum
打印两个数值中的最大数。

 这两个数都应该是整数

```

这里要注意文档字符串也适用于后面相关章节将提到的`模块(Modules)`与`类(Class)` 。

强烈推荐你为你编写的所有重要的函数配以文档字符串。

# 模块
