# Python 基础

[TOC]

## Introduction

解释性语言。
由荷兰人Guido van Rossum 1989年圣诞节创建。

* 特点：
    * 语法优雅，简单明确，易于上手
    * 丰富的第三方类库
    * 应用广泛，前景不可估量

* 应用场景/领域/实际应用：
    * Web开发/爬虫
        * Django
        * Flask
        * bootle
        * Tornado
        * scrapy 
    * IT基础设施及自动化运维
        * OpenStack
        * SaltStack
        * Ansible
    * 机器学习/深度学习
        * TensorFlow
        * Theano
        * Caffe
    * 科学计算/数据处理/数据可视化
        * NumPy
        * SciPy
        * SymPy
        * matplotlib
        * Traits
        * TraitsUI
        * Chaco
        * TVTK
        * Mayavi
        * Visual
        * OpenCV
    * 自然语言处理
        * NLTK 
    * 封装其他语言的模块
        * Java等应用启动脚本
    * ...

## Beginning

### Installing Python

* Windows
    * 下载、安装（python，pip）
    * 设置环境变量
    * 重启系统
* Linux (自带Python)
* MacOS X (自带Python)

### Python Versoin

> Python2.7 与 Python3.x会有兼容问题，需要注意系统的版本及第三方库以来的版本。

```bash
# 查看python版本
python --version
```

### Try Python

* 交互式命令行运行Python

    ```python
    $ python # 命令行运行python
    Python 2.7.13 (default, Apr  4 2017, 08:47:57)
    [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 100 + 200           # 在Python shell下，执行python代码
    300                     # ->返回执行结果
    
    >>> print 'hello world' # 在Python shell下，执行python代码
    hello world             # ->返回执行结果
    
    >>> exit()      # 退出python shell
    $               # 返回默认shell
    ```

* Python程序文件

    * 后缀：`Python`文件默认以`.py`为后缀
    * 注释：
        * 单行注释: # This is comment
        * 块注释: """块注释""" 或 '''块注释'''
    * `Python`对缩进要求非常严格，**行首不能有空格**
    * `print`会依次打印每个字符串，遇到逗号“,”会输出一个空格。
    * ...

    ```python
    $ vi hello.py   # 创建hello.py文件
    
    # 保存以下代码
    print 100 + 200
    print 'Hello World!'
    print 'hello','world'
    
    $ python hello.py   # 执行hello.py, 输出以下内容
    300
    Hello World!
    Hello World!
    ```

* 声明解释器及字符

    ```python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    ```

## Python Tools

* pip
* virtualenv
* virtualenvwrapper
* ipython
* pylint

## 基本数据类型

### 1. 整型

* 十进制
* 十六进制（0x）前缀为0-f，如：0xff00。

```python
>>> print 45678 + 0x12fd2
123456
```

### 2. 浮点型

即小数。1.23x10^9 即 1.23e9，0.000012即 1.2e-5。

### 3. 字符串

单引号或双引号（''或 ""）括起来的任意文本。

### 4. 布尔

* 直接使用布尔值表示：
    * `True`
    * `False`

> 注意: 区分大小写
    
* 通过运算符计算：
    * 与运算符：`and`
    * 或运算符：`or`
    * 非运算符：`not`

```python
>>> print 100 < 99
False

>>> print 0xff == 255
True
```

### 5. 空 

```python
>>> None == 0   # 注意：None不等于0
False

>>> None == ''  # 注意：None不等于0
False
```

## 变量 & 数据类型

* 变量名必须是以下的组合（不能用数字开头）：
    * 大小写英文
    * 数字
    * 下划线（_）
* 变量在使用之前必须要被“定义”(分配一个值), 否则会产生一个错误

    ```bash
    >>> print VAR
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'VAR' is not defined
    
    >>> VAR = 1
    >>> print VAR
    1
    
    # 求 1 4 7 10 13 16 19... 前100项和
    an = 1 + 3 * (n-1)
    a100 = 1 + 3 * (100 - 1)
    sum100 = (1 + a100) * 100/2
    print sum100
    ```
    
### 字符串

```python
>>> languge = 'python'
>>> print languge
python

# 包含双引号
>>> s = 'This is a "string".'
>>> print s
This is a "string".

# 字符串拼接
>>> ss = 'This is ' + 'a test.'
>>> print ss
This is a test.

# 字符串重复
>>> sss = 'a' * 3
>>> print sss
aaa

# 按索引位置获取字符
>>> ss = 'language'
>>> print ss[3]
g

## 尝试获取一个不存在索引位置会产生一个错误
>>> print ss[10]  # 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

## 给字符串的索引位置赋值会产生一个错误
>>> ss[3] = 'B'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

* 常用的转义字符
    * \n  表示换行
    * \t  表示一个制表符
    * \\  表示 \ 字符本身   

    ```python
    # 使用转义字符 \
    >>> say = 'Python2.7 says: \n\t \"I\'m OK\" \nto Python3.'
    >>> print say
    Python2.7 says:
         "I'm OK"
    to Python3.
    ```
* 定义中文字符串

    ```python
    >>> s = u'中文字符串'
    ```

### 整数和浮点数

Python运算规则和数学上的四则运算规则基本一致。

```python
# 对整数和浮点数直接进行四则混合运算
>>> 1 + 2 + 3
6
>>> 4 * 5 - 6
14
>>> 7.5 / 8 + 2.1
3.0375

# 括号可以提升优先级，只能使用小括号，可以嵌套很多层
>>> (1 + 2) * 3
9
>>> (2.2 + 3.3) / (1.5 * (9 - 0.3))
0.42145593869731807

# Python的整数运算结果仍然是整数，浮点数运算结果仍然是浮点数
>>> 1 + 2
3
>>> 1.0 + 2.0
3.0

# 整数和浮点数混合运算的结果就变成浮点数
>>> 1 + 2.0
3.0
```

> 区分浮点数和整数是因为：

* 整数运算的结果永远是精确的
* 浮点数运算的结果不一定精确，可能是无限的
* 计算机内存再大，也无法精确表示出无限循环小数，比如 0.1 换成二进制表示就是无限循环小数。


```python
# Python的整数除法，即使除不尽，结果仍然是整数，余数直接被丢弃
>>> 11 / 4
2

# 可使用求余% 来求余数
>>> 11 % 4
3
```

> 对于要计算两个整数相除的精确结果的场景，可以把两个数中的一个变成浮点数

```python
>>> 11 / 4
2
>>> 11.0 / 4
2.75
```

### 布尔类型

* 布尔类型数据
* 逻辑运算符
    * and
    * or
    * not 

```python
>>> True and False
False
>>> True or False
True
>>> not True
False
>>> not False
True
```

`and`和 `or` 运算的一条重要法则：**短路计算**

> Python把`0`、`空字符串''`和`None`看成 `False`，其他数值和非空字符串都看成 `True`

```python
>>> True and 'a=T'
'a=T'
>>> 'a=T' or 'a=F'
'a=T'

>>> None
>>> not None
True

>>> None and True
>>> None and False
>>> None or True
True
>>> None or False
False

>>> print None and True
None
>>> print None and False
None
>>> print None or True
True
>>> print None or False
False
```

### List & Tuple

* `list`和`tuple`都是**有序集合**，二者非常类似。
    * `list`使用方括号: [1,2,3,4]
    * `tuple`使用小括号: (1,2,3,4) 
* `tuple`创建完不能修改

```python
>>> L = [1,2,3,4]
>>> T = (1,2,3,4)

>>> L
[1, 2, 3, 4]
>>> T
(1, 2, 3, 4)

>>> L[2] = 5
>>> l
[1, 2, 5, 4]

>>> T[2] = 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

#### List

```python
# list中的元素可以是不同类型
>>> L = ["hello", 520, True, None]
>>> L
['hello', 520, True, None]

# 空List
>>> L = []
>>> L
[]
```

* 访问元素
    * 可使用索引访问`List`元素；
    * 越界会报`IndexError`;
    * 可使用复数倒序访问`List`；
* 添加元素
    * `append('element')` 往`List`末追加元素
    * `insert(index, element)` 插入元素到`List`指定索引
* 删除元素
    * `pop()` 删除`List`最后一个元素
    * `pop(index)` 删除`List`指定索引元素
* 替换元素
    * `L[3] = 20` 重新赋值替换

#### Tuple

* 单元素`tuple`

    ```python
    # 单元素tuple，结果为该元素
    >>> T = (1)
    >>> T
    1
    
    # 单元素`tuple`要多加一个逗号“,”
    >>> T = (1,)
    >>> T
    (1,)
    ```

* 可变`tuple`

    ```python
    # 将List作为tuple的一个元素
    >>> T = ('a', 'b', ['A', 'B'])
    >>> T
    ('a', 'b', ['A', 'B'])
    
    >>> L = T[2]
    >>> L
    ['A', 'B']
    
    >>> L[0] = 1
    >>> L[1] = 2
    >>> T
    ('a', 'b', [1, 2])
    ```

    `Tuple`所谓的**“不变”**是说，`Tuple`的每个元素，**指向永远不变**。即指向'a'，就不能改成指向'b'，指向一个`list`，就不能改成指向其他对象，但指向的这个`List`本身是可变的。

## 条件语句

* `if` 语句后接表达式，用`:`表示代码块开始;
* Python代码的缩进规则。`具有相同缩进`的代码被视为代码块;
* Python交互环境下敲代码：退出缩进需要多敲一行回车；

### if

```python
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'

print 'END'
```

**缩进请严格按照Python的习惯写法：`4个空格，不要使用Tab，更不要混合Tab和空格`**

### if...else

```python
if age >= 18:
    print 'your age is', age
    print 'adult'
else:
    print 'your age is', age
    print 'child'
```

### if..elif..else

```python
score = 85
if score>=90:
    print 'excellent'
elif score>=85:
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'
```

## 循环

### for

```python
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name

# 求平均值
L = [75, 92, 59, 68]
sum = 0.0
count = 0
for score in L:
    sum += score
    count+=1

print sum / count

# 求最大/小值 [1,42,5,7,8,9,0]
```

### while

```python
# 从 0 开始打印不大于 N 的整数
N = 10
x = 0
while x < N:
    print x
    x = x + 1
    
# 计算100以内奇数的和
sum = 0
x = 0
while x < 100:
    if x%2 == 1:
        sum += x

print sum
```

### break 退出循环

```python
sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
```

### continue 跳过本次循环

```python
for f in [1,2,3,4,5]:
    if f == 3:
        continue
    print f
```

### 多层循环

输出一个 9 * 9 乘法表

```python
x = 1
while x <= 9:
    y = 1
    while y <= x:
        print y, '*', x, '=', x * y, ' ',
        if x == y:
            print ''
        y = y + 1
    x = x + 1
```

对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。

```python
x = 1
while x < 10:
    y = 1
    while y < x:
        print y * 10 + x
        y = y + 1
    x = x + 1
```

## dict & set

* dict 作用是建立一组 key 和一组 value 的映射关系
    * **key不能重复** 
    * **key不可变**（Python的基本类型如字符串、整数、浮点数都是不可变的，都可做key，List是可变的不能作为key）
    * **无序**，以key-value键值对保存（打印的顺序不一定是创建的顺序）；
    * **查找效率高**，速度快，与元素数量无关（List的速度会随元素数量增加而下降）;
    * **占用内存大**；
* set 持有一系列元素
    * **元素没有重复**；
    * **无序**

### dict

Python 的 dict 用于表示key-value：

```python
d = {
    'adam': 90,
    'Lisa': 100,
    'Bart': 50,
}

# 计算大小
len(d)     
``` 

构造器 dict() 从键 -值对序列里直接生成字典

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) 
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> dict([(x, x**2) for x in (2, 4, 6)]) # 使用列表推导式 {2: 4, 4: 16, 6: 36}
```

#### 访问 dict

```python
# 访问指定key
print d['adam']

# 建议先判断下是否存在
if 'adam' in d:
    print d['adam']

# 使用get获取，若不存在，则返回None
print d.get('adam')

# 设置默认值，若不存在，则返回默认值
print d.get('adam', 'default')

# 删除一个键/值对
del d['Bart']

# 返回该字典中所使用键的列表
list(d.keys())

# 排序
sorted(d.keys())
```

#### 更新dict

```python
# 往dict里增加元素, 若key已存在，则替换该key的value
d['test'] = 30
``` 

#### 遍历 dict

> 检查某一个键是否在字典里, 使用 in 关键字

```python
for k in d:
    print k,d[k]

# items() 方法同时取回键和对应的值
for k,v in d.items():
    print k,v

# enumerate() 函式来同时取回位置索引和相应的值.
for i,v in enumerate(['tic', 'tac', 'toe']):
    print i,v

# 同时对两个或更多的序列进行遍历时, 可用 zip() 进行组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'theholygrail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
    
# 反向遍历序列时, 先指定这个序列, 然后调用 reversed() 函式
for i in reversed(range(1, 10, 2)):
    print i
```

### set

## Reference

* [Python.org](https://www.python.org/)
* [Python 2.7教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000)
* [Python风格规范 - Google 开源项目风格指南](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/)


