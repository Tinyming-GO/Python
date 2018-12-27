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




