# Python快速编程入门

[TOC]

## 第1章 Python概述

### 01  认识Python

> 人生苦短，我用python

python语言是**面向对象解释型编**程语言（动态）

Python 语 言 的 优 点：

- 简洁。Python代码的行数往往只有C、C++、Java代码数量的1/5~1/3。
- 语法优美。Python语言是高级语言，它的代码接近人类语言，只要掌握由英语单词表示的助记符，就能大致读懂Python代码。
- 简单易学。Python是一门简单易学的编程语言，它使编程人员更注重解决问题，而非语言本身的语法和结构。
- 开源。Python是FLOSS（自由/开放源码软件）之一，用户可以自由地下载、拷贝、阅读、修改代码。
- 可移植。Python语言编写的程序可以不加修改地在任何平台中运行。
- 扩展性良好。Python不仅可以引入.py文件，还可以通过接口和库函数调用由其它高级语言（如C语言、C++、Java等）编写的代码。
- 类库丰富。世界各地的程序员通过开源社区又贡献了十几万个几乎覆盖各个应用领域的第三方函数库。
- 通用灵活。Python是一门通用编程语言，可被用于科学计算、数据处理、游戏开发、人工智能、机器学习等各个领域。
- 模式多样。Python既支持面向对象编程，又支持面向过程编程。
- 良好的中文支持。Python 3.x解释器采用UTF-8编码表达所有字符信息，编码支持英文、中文、韩文、法文等各类语言。

Python 语 言 的 缺 点

- 执行效率不够高，Python程序的效率只有C语言程序的1/10。
- Python 3.x和Python 2.x不兼容。

### 02  Python解释器的安装与Python程序的运行



### 03  Python开发工具

- 新建项目，配置解释器的位置，执行欢迎脚本
- 新建文件，书写代码，执行快捷命令：ctrl+shife+F10

### 04  Python模块

#### 1.4.1 模块的安装

利用Python内置的pip工具（安装Python3.8时会自动安装该工具）可以非常方便地安装Python第三方模块，该工具可在命令行中使用。

- 查看命令

`pip list`

- 安装命令

`pip instll 模块名称`

#### 1.4.2 模块的导入与使用

```python
import turtle as t #导入模块
from turtle import *
t.forward(200)
t.seth(-90)
t.forward(200)
t.right(90)
t.forward(200)
t.left(-90)
t.forward(200)
t.done()
```

## 第2章 Python基础

### 2.1 代码格式

#### 2.1.1 注释

单行注释以“#”开头，用于说明当前行或之后代码的功能。单行注释既可以单独占一行，也可以位于标识的代码之后，与标识的代码共占一行。

多行注释是由三对双引号或单引号包裹的语句，主要用于说明函数或类的功能。

```python
print("人生苦短，我用Python!") #也可以写在代码后面，告诉计算机这是注释用的，你不用执行我。
# 上面这段代码的作用是输出“”的内容
#print("人生苦短，我用Python!") #单行注释

""""
多行注释是由三对双引号或单引号包裹的语句，主要用于说明函数或类的功能
"""
'''
多行注释是由三对双引号或单引号包裹的语句，主要用于说明函数或类的功能
'''
'''
多行注释，用于有多行的说明
'''
```

 #### 2.1.2 缩进

Python代码的缩进可以通过Tab键控制，也可使用空格控制。空格是Python3首选的缩进方法，一般使用4个表示一级缩进；Python3不允许混合使用Tab和空格。

```python
#下面的代码展示缩进的重要性
if True:
    print("真")
else:
    print("假")

print("假")
```

#### 2.1.3 语句换行

### 2.2 标识符和关键字

#### 2.2.1 标识符

若希望在程序中表示一些事物，开发人员需要自定义一些符号和名称，这些符号和名称叫做标识符。 Python中的标识符需要遵守一定的规则。

- 标示符由字母、下划线和数字组成，且数字不能开头。
- Python中的标识符是区分大小写的。例如，andy和Andy是不同的标识符。
- Python中的标识符不能使用关键字 。 

 a-1 A_1 a_1 a*1 1_a

#### 2.2.2 关键字

关键字是Python已经使用的、不允许开发人员重复定义的标识符（有特殊含义的标识符）。Python3中一共有35个关键字，每个关键字都有不同的作用。

False	        await	     else		import		pass		None
break            except	     in		raise		True		class
finally            is		     return	and   		continue             for          
lambda	        try	                  as		def		from	             nonlocal
while	        assert	    del		global		not		with 
async	        elif		     if		or		yield

#### 2.3.1 变量

标识内存单元的标识符又称为变量名，Python通过赋值运算符“=”将内存单元中存储的数值与变量名建立联系，即定义变量，具体语法格式如下：变量 = 值

什么是变量？就是程序在运行期间其值会改变的。

### 2.3 变更和数据类型

#### 2.3.2 数据类型

根据数据存储形式的不同，数据类型分为基础的数字类型和比较复杂的组合类型，其中数字类型又分为整型、浮点型、布尔类型和复数类型；组合类型分为字符串、列表、元组、字典等。

Python内置的数字类型有整型（int）、浮点型（float）、复数类型（complex）和布尔类型(bool)，其中int、float和complex分别对应数学中的整数、小数和复数；bool类型比较特殊，它是int的子类，只有True和False两种取值

- 整型： 0     101     -239     False     True

- 浮点型：  3.1415     4.2E-10     -2.334E-9

- 复数类型：  3.12+1.2.3j     -1.23-93j

- 布尔类型：  True     False

字符串是一个由单引号、双引号或者三引号包裹的、有序的字符集合。

- 使用单引号包含： 'Python123￥' 

- 使用双引号包含：  "Python4*&%"	

- 使用三引号包含：  '''Python s1 ~(())'''

列表是多个元素的集合，它可以保存任意数量、任意类型的元素，且可以被修改。Python中使用“[]”创建列表，列表中的元素以逗号分隔，示例如下： 

- [1, 2, 'hello']

元组与列表的作用相似，它可以保存任意数量与类型的元素，但不可以被修改。Python中使用“()”创建元组，元组中的元素以逗号分隔，示例如下：

- (1, 2, 'hello'])

集合与列表和元组类似，也可以保存任意数量、任意类型的元素，不同的是，集合使用“{}”创建，集合中的元素无序且唯一。示例如下：

- {'apple', 'orange', 1} 

集合与列表和元组类似，也可以保存任意数量、任意类型的元素，不同的是，集合使用“{}”创建，集合中的元素无序且唯一。示例如下：

- {'apple', 'orange', 1} 

#### 2.3.3 变量的输入与输出

input()函数用于接收用户键盘输入的数据，返回一个字符串类型的数据，其语法格式如下所示：



print()函数用于向控制台中输出数据，它可以输出任何类型的数据，其语法格式如下所示：

### 2.4 实训案例

#### 2.4.1 打印购物小票

### 2.5 数字类型

#### 2.5.1 整型

整数类型（int）简称整型，它用于表示整数。整型常用的计数方式有4种，分别是二进制（以“0B”或“0b”开头）、八进制（以数字“0o”或“0O”开头）、十进制、十六进制（以“0x”或“0X”开头）。

- 0b101		# 二进制
- 0o5			# 八进制
- 5			# 十进制
- 0x5			# 十六进制

为了方便使用各进制的数据，Python中内置了用于转换数据进制的函数：bin()、oct()、int()、hex()，关于这些函数的功能说明如下。

#### 2.5.2 浮点型

浮点型（float）用于表示实数，由整数和小数部分（可以是0）组成例如，3.14、0.9等。较大或较小的浮点数可以使用科学计算法表示。

Python中的浮点型每个浮点型数据占8个字节（即64位），且遵守IEEE标准。Python中浮点型的取值范围为-1.8e308~1.8e308，若超出这个范围，Python会将值视为无穷大（inf）或无穷小（-inf）

#### 2.5.3 复数类型

复数由实部和虚部构成，它的一般形式为：real+imagj，其中real为实部，imag为虚部，j为虚部单位

#### 2.5.4 布尔类型



```python
num_one=2
num_two=2.2
print(int(num_two))  # 结果等于多少？  2
print(float(num_one)) # 2.0
print(complex(num_one)) # 复数类型 实部 虚部 2+0j

```
### 2.6 运算符
####  2.6.1 算术运算符

Python中的算术运算符包括+、-、*、/、//、%和**。以操作数a = 2，b = 8为例对算术运算符进行使用说明。

Python中的算术运算符既支持对相同类型的数值进行运算，也支持对不同类型的数值进行混合运算。在混合运算时，Python会强制将数值的类型进行临时类型转换，这些转换遵循如下原则

- 整型与浮点型进行混合运算时，将整型转化为浮点型。
- 其他类型与复数运算时，将其他类型转换为复数类型。

#### 2.6.2 赋值运算符

赋值运算符的作用是将一个表达式或对象赋值给一个左值。左值是指一个能位于赋值运算符左边的表达式，它通常是一个可修改的变量，不能是一个常量。
例如将整数3赋值给变量num：num=3。
赋值运算符允许同时为多个变量赋值

Python3.8中新增了一个赋值运算符——海象运算符“:=”，该运算符用于在表达式内部为变量赋值，因形似海象的眼睛和长牙而得此命名。



```python
num_one = 1
# 使用海象运算符为num_two赋值
result = num_one + (num_two:=2)
print(result)

```

#### 2.6.3 比较运算符

比较运算符也叫关系运算符，用于比较两个数值，判断它们之间的关系。Python中的比较运算符包括==、!=、>、<、>=、<=，它们通常用于布尔测试，测试的结果只能是True或False。以变量x=2，y=3为例，具体如下：

#### 2.6.4 逻辑运算符

Python中分别使用“or”，“and”，“not”这三个关键字作为逻辑运算符，其中or与and为双目运算符，not为单目运算符

#### 2.6.5 成员运算符

成员运算符in和not in用于测试给定数据是否存在于序列（如列表、字符串）中，关于它们的介绍如下：

- in：如果指定元素在序列中返回True，否则返回False。
- not in：如果指定元素不在序列中返回True，否则返回False。

#### 2.6.6 位运算符

- 左移 <<
- 右移 >>
- 与 &
- 或 |
- 异或 ^
- 取反~

#### 2.6.7 运算符优先级 

Python支持使用多个不同的运算符连接简单表达式，实现相对复杂的功能，为了避免含有多个运算符的表达式出现歧义，Python为每种运算符都设定了优先级
### 2.7 实训案例
#### 2.7.1 绝对温标

绝对温标又称开氏温标、热力学温标，是热力学和统计物理中的重要参数之一，也是国际单位制七个基本物理量之一。绝对温标的单位为开尔文（简称开，符号为K），绝对温标的零度对应我们日常使用的摄氏温度（单位为摄氏度，简称度，符号为℃）的-273.15℃。
本实例要求编写代码，实现将用户输入的摄氏温度转换为移绝对温标标识的开氏温度的功能。

```python
# 提示：
# T(K)=t(℃)+273.15
# 1.从键盘上输入摄氏温度 c=input(""),强制转换成float()类型
# 2.将从键盘上取得的数字加上273.15
# 3.最后输出c print()

c=input("提示：请输入摄氏温度：")
c=float(c)+273.15
print('转换后的绝对温标:{}'.format
```





#### 2.7.2 身体质量指数

BMI指数即身体健康指数，它与人的体重和身高相关，是目前国际常用的衡量人体胖瘦程度以及是否健康的一个标准。已知BMI值的计算公式如下：
体质指数（BMI）= 体重（kg）÷身高^2（m）
本实例要求编写代码，实现根据用户输入的身高体重计算BMI指数的功能 

```python
height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
BMI = weight / (height ** 2)
print('您的BMI值为:',BMI)

```

## 第3章 流程控制

### 3.1    条件语句

#### 3.1.1    if语句

if语句由关键字if、判断条件和冒号组成，if语句和从属于该语句的代码段可组成选择结构。

执行if语句时，若if语句的判断条件成立（判断条件的布尔值为True），执行之后的代码段；若if语句的判断条件不成立（判断条件的布尔值为False），跳出选择结构，继续向下执行。

```python
#判断考试及格
# score=80
score=float(input("请输入成绩："))
if score>60:
    print("考试及格！")
```

#### 3.1.2 if-else语句

执行if-else语句时，若判断条件成立，执行if语句之后的代码段1；若判断条件不成立，执行else语句之后的代码段2。

```python
#双分支判断语句
score=50
if score>60:
    print("及格")
else:
    print("不及格")
```

#### 3.1.3 if-elif-else语句

```python
#多分支
score=float(input("请输入成绩:"))
if score>85:
    print("优秀")
elif 75 <= score <=85:
    print("良好")
elif 60 <= score <75:
    print("及格")
else:
    print("不及格")

```

#### 3.1.4 if嵌套

```python
year=2020
month=2
if month in [1,3,5,7,8,10,12]:
    print("%d年%d月有31天" % (year,month))
elif month in [4,6,9,11]:
    print("%d年%d月有30天" % (year,month))
elif month==2:
    if year % 400==0 or year % 4==0 and year % 100!=0:
        print("%d年%d月有29天" % (year,month))
    else:
        print("%d年%d月有28天" % (year,month))

```

### 3.2 实训案例

#### 3.2.1 计算器
 ```python
 # 计算器可以进行基础运算（加、减、乘、除）被除数不为0
first = float(input("请输入第一个数："))
second = float(input("请输入第二个数："))
operator = input("请选择运算符：+ - * /:")
if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    if second == 0:
        print("除数不能为0")
    else:
        print(first / second)

 ```

#### 3.2.2 猜数字

```python
guess_num = input("请设定要猜的数字：\n")
for frequency in range(1,6):
    number = input("请输入第"+str(frequency)+"次猜测的数字:")
    if number.isdigit() is False:
        print('请输入一个正确的数字')
    elif int(number) < 0 or int(number) > 100:
        print("请输入1-100范围的数字")
    elif int(guess_num) == int(number):
        print("恭喜你用了%d次猜对了" % frequency)
        break
    elif int(guess_num) > int(number):
        print("很遗憾，你猜小了")
    else:
        print("很遗憾，你猜大了")
    if frequency == 5:
        print("很遗憾，%d次机会已用尽，游戏结束,答案为%d" % (frequency, int(guess_num)))
```



### 3.3   循环语句

#### 3.3.1 while语句

while语句一般用于实现条件循环，该语句由关键字while、循环条件和冒号组成，while语句和从属于该语句的代码段组成循环结构

```python
# 求1+2+3+4+5+6..+10的和
i=1
r=0
while i<=10:
    r=r+i
    i+=1
print("等于:",r)
```



```python
while True:
    print("我是无限循环。。。")
```



#### 3.3.2 for语句

for语句一般用于实现遍历循环。遍历指逐一访问目标对象中的数据，例如逐个访问字符串中的字符；遍历循环指在循环中完成对目标对象的遍历

```python
# for w in "人生苦短，我用Pthon":
#     print(w)

r = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    r = r + i
print("等于:", r)

```

#### 3.3.3 循环嵌套

循环之间可以互相嵌套，进而实现更为复杂的逻辑。循环嵌套按不同的循环语句可以划分为while循环嵌套和for循环嵌套。

```python
i = 1
while i < 6:
    j = 0
    while j < i:
        print("*", end=' ')
        j += 1
    print()
    i += 1

for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()
```

### 3.4 实训案例

### 3.5 跳转语句

#### 3.5.1 break语句

break语句用于结束循环，若循环中使用了break语句，程序执行到break语句时会结束循环；若循环嵌套使用了break语句，程序执行到break语句时会结束本层循环。

```python
# 在使用for循环遍历字符串python时，遍历到字符o时就使用break结束循环。
for word in "python":
    if word == 'o':
        break  # 中止循环
    print(word, end=' ')

```



#### 3.5.2continue语句

continue语句用于在满足条件的情况下跳出本次循环，该语句通常也与if语句配合使用。

```python
# 在使用for循环遍历字符串python时，遍历到字符o时就使用continue结束本次循环。
for word in "python":
    if word == 'o':
        continue  # 结束本次循环
    print(word, end=' ')

```

## 第4章 字符串

### 4.1    字符串介绍

字符串是由字母、符号或者数字组成的字符序列。

Python支持使用单引号、双引号和三引号定义字符串，其中单引号和双引号通常用于定义单行字符串，三引号通常用于定义多行字符串。

转义字符

一些普通字符与反斜杠组合后将失去原有意义，产生新的含义。类似这样的由“\”和而成的、具有特殊意义的字符就是转义字符。转移字符通常用于表示一些无法显示的字符，例如空格、回车等。

原始字符串

```python
print('使用单引号定义的字符串')
print("使用双引号定义的字符串")
print("""使用三引号
定义的
字符串""")
print("let's learn python")
print('let\'s learn python')  # 转义字符

print("let's learn\n python")  # 转义字符

print("转义字符中:\n表示换行;\r表示回车;\b表示退格")  # 转义字符
print(r'转义字符中:\n表示换行;\r表示回车;\b表示退格')  # 原始字符串
```



### 4.2  格式化字符串

#### 4.2.1 使用%格式化字符串

```python
name = "张三"
age = 18
print("我叫%s,今年%d岁了" % (name, age))
```

#### 4.2.2 使用format()方法格式化字符串

```python
print("我叫{},今年{}岁了".format(name, age))
print("姓名：{1},年龄:{0}".format(name, age))
print("姓名：{name},年龄:{age}".format(name=name, age=age))
print("百分号{:.2%}".format(10/3))
```

#### 4.2.3 使用f-string格式化字符串

f-string提供了一种更为简洁的格式化字符串的方式，它在形式上以f或F引领字符串，在字符串中使用“{变量名}”标明被替换的真实数据和其所在位置。

```python
print(f'姓名：{name}, 年龄:{age}')
```

### 4.3 实训案例

#### 4.3.1 进制转换

```python
num = int(input("请输入要转换的数据:\n"))
change = input("请选择转换进制：二 、八、十、十六\n")
if change == '2':
    print(f"进制转换后的数据为：{bin(num)}")
elif change == '8':
    print("进制转换后的数据为：%s" % (oct(num)))
elif change == '10':
    print("进制转换后的数据为：%d" % (int(num)))
elif change == '16':
    print("进制转换后的数据为：{}".format(hex(num)))

```

#### 4.3.2 进度条

```python
import time

incomplete_sign = 50   # .的数量
print('='*23+'开始下载'+'='*25)
for i in range(incomplete_sign + 1):
    completed = "*" * i   # 表示已完成
    incomplete = "." * (incomplete_sign - i)  # 表示未完成
    percentage = (i / incomplete_sign) * 100  # 百分比
    print("\r{:.0f}%[{}{}]".format(percentage, completed, incomplete), end="")
    time.sleep(0.5)
print("\n" + '='*23+'下载完成'+'='*25)
```

### 4.4 字符串的常见操作

#### 4.4.1 字符串的查找与替换

```python
#查找
word='t'
str='python'
res=str.find(word)
res1='python'.find('h')
print(res,res1)

#替换
string = 'Then turn left, Then go forward, and Then turn right."'
new_str=string.replace('Then','then',2)
print(new_str)
```

#### 4.4.2 字符串的分割与拼接

```python
#分割
string= "Hello, my name is Wang Hong"
print(string)
print(string.split())
print(string.split('a'))
print(string.split('a',1))
print(string.split(','))
#拼接
s='*'
w='python'
print(s.join(w))
print('+'.join('python'))

start='py'
end='thon'
print(start+end)

```

#### 4.4.3 删除字符串的指定字符

```python
#删除指定字符
old_str='  life is short,use python   '
print('原始字符:',old_str)
print(f'strip方法:{old_str.strip()}') #左边和右边
print(f'lstrip方法:{old_str.lstrip()}') #左边
print(f'rstrip方法:{old_str.rstrip()}') #右边


```

#### 4.4.4 字符串大小写转换

```python
#大小写转换
str='hello woRld'
print(f'全部转换成大写：{str.upper()}')
print(f'全部转换成小写：{str.lower()}')
print(f'首字母转换在大写：{str.capitalize()}')
print(f'每个单词首字母转换在大写：{str.title()}')

#字符串对齐
str1='hello world'
print(f"居中对齐：{str1.center(13,'-')}")
print(f"左对齐：{str1.ljust(13,'+')}")
print(f"右对齐：{str1.rjust(13,'+')}")
```

### 4.5 实训安案例

#### 4.5.1 敏感词替换

```python
sensitive_character = '你好'  			# 敏感词库
test_sentence = input('请输入一段话:')
for line in sensitive_character:  		# 遍历输入的字符是否存在敏感词库中
    if line in test_sentence:  			# 判断是否包含敏感词
        test_sentence = test_sentence.replace(line, '*')
print(test_sentence)

'''
1. 敏感词库 你好
2. 你好，同学
3. fot遍历 (你好) 第一个字 line=你
4. 判断 你 有没有在 你好，同学 ？
5. 替换 你好，同学 替换成 *好，同学
3. fot遍历 (你好) 第二个字 line=好
4. 判断 好 有没有在 你好，同学 ？
5. 替换 你好，同学 替换成 **，同学
6. 输出 **，同学
'''
```



## 第五章 组合数据类型

### 5.1 认识组合数据类型

### 5.2 列表

#### 5.2.1 创建列表

Python列表的创建方式非常简单，既可以直接使用中括号“[]”创建，也可以使用内置的list()函数快速创建。

```python
# 创建列表
list1=[]
list2=[1,2,3,4,5,'p','y',3.14]

# list3=list(1) # 出错
list4=list('python')
list5=list([1,'python'])
# print(list3)
print(list4)
print(list5)
```



#### 5.2.2 访问列表元素

列表中的元素可以通过索引或切片这两种方式进行访问，也可以在循环中依次访问

```python
# 索引
list=['java','c#','python','PHP']
print(list[0])
print(list[-1])

# 切片
li=['p','y','t','h','o','n']
print(li[0:3])
print(li[0:4:2]) 
print(li[2:])
print(li[:4])
print(li[:])

for l in li:
    print(l,end=' ')

print()
print('y' in li) # 存在于li中
print('y' not in li) # 不存在于li中 
```



#### 5.2.3 添加列表元素

向列表中添加元素是非常常见的一种列表操作，Python提供了append()、extend()和insert()这几个方法向列表末尾、指定位置添加元素。

```python
list_one=[1,2,3,4]
list_one.append(5)  # 从尾部添加一个元素
print(list_one)

list_str=['a','b','c']
list_num=[1,2,3]
list_str.extend(list_num) # 从尾部添加一个列表
print(list_str)

names=['baby','lucy','jia']
names.insert(2,'aaa') # 从指定位置插入
print(names)
```

#### 5.2.4 元素排序

```python
li_one=[6,2,5,3]
li_two=[7,3,5,4]
li_three=['python','java','php']
li_one.sort() # 升序
li_two.sort(reverse=True) # 降序
li_three.sort(reverse=True,key=len) # 按字符长度降序
print(li_one)
print(li_two)
print(li_three)

li=[4,3,2,1]
li_new=sorted(li) # 老的列表不会改变，会产生新的列表
print(li)
print(li_new)

li_str=['a','b','c','d']
li_str.reverse() # 逆置列表
print(li_str)
```

#### 5.2.5 删除元素

```python
names=['a','b','c','d']
del names[1] # 按索引移除
print(names)
del names
#print(names)

chars=['h','e','l','l','e']
chars.remove('l') # 移除指定元素
print(chars)

ch=['h','e','l','l','e']
print(ch.pop()) #弹出，默认弹出最后一个
print(ch.pop(0))

ch.clear() #清空
print(ch)

```

#### 5.2.6 列表推导式

列表推导式是符合Python语法规则的复合表达式，它用于以简洁的方式根据已有的列表构建满足特定需求的列表。

```python
ls=[1,2,3,4,5,6,7,8,9]
ls=[data*data  for data in ls ]
print(ls)

# ls=[1,2,3,4,5,6,7,8,9]
# for data in ls:
#     sum=data*data
#     print(sum,end=' ')

ls=[1,2,3,4,5,6,7,8,9]
ls=[data for data in ls if data>4]
print(ls)

ls_one=[1,2,3]
ls_two=[3,4,5]
ls_three=[x+y for x in ls_one for y in ls_two]
print(ls_three)

ls_one=[1,2,3]
ls_two=[3,4,5]
for x in ls_one:
    for y in ls_two:
        print(x+y,end=' ')
```

### 5.3 元组

元组的表现形式为一组包含在圆括号“()”中、由逗号分隔的元素，元组中元素的个数、类型不受限制。
使用圆括号可以直接创建元组，还可以使用内置函数tuple()构建元组

```python
t3=(1,3.14,3,'a',5,6,'p')
# 索引
print(t3[1])
# 切片
print(t3[1:4]) # 请试着输出 3.14,3,'a'

#循环遍历
for data in t3:
    print(data,end=' ')

# **元组是不可变类型，元组中的元素不能修改。它不支持添加、删除和排序。**
print()
l=[1,2,3]
l[0]=3
print(l)

t=(1,2,3)
# t[0]=3
print(t)
```

**元组是不可变类型，元组中的元素不能修改。它不支持添加、删除和排序。**

### 5.4 实训案例

#### 5.4.1 十大歌手

```python
# 9 8 5 6 4 7 3 8 5 1 
# 1 3 4 5 5 6 7 8 8 9
# 3 4 5 5 6 7 8 8

# 评分列表
score_li = []
# 总分
total_score = 0
for i in range(1, 11):
    score = float(input(f"请第{i}位评委输入评分：\n"))
    score_li.append(score) # 从尾部一个个添加进去
score_li.sort() #默认是升序
print(f"去掉最低分：{score_li[0]}")
print(f"去掉最高分：{score_li[len(score_li)-1]}")
# 去掉最低分
score_li.remove(score_li[0]) # 移除 第一个元素
# 去掉最高分
score_li.pop()  # 移除 最后一个元素
for j in score_li:
    total_score += j  # 求总分
print(f'选手最终得分为：{total_score/(len(score_li))}') # 最后输出平均分
```



### 5.5 集合

Python的集合（set）本身是可变类型，但Python要求放入集合中的元素必须是不可变类型。
集合类型与列表和元组的区别是：集合中的元素无序但必须唯一。
集合的表现形式为一组包含在大括号“{}”中、由逗号“,”分隔的元素。使用“{}”可以直接创建集合，使用内置函数set()也可以创建集合。

创建集合

 ```python
s1={1}
s2={1,'b',(2,5)}
s3={1,1,1,'a','a','b'}
s4=set() #我是空集合
s5={1,2,3,4}
print(s3)

 ```

集合添加、移除、弹出、复制、清空

```python
s1={1}
s1.add(2)
print(s1)

s2={1,2,3}
s2.remove(2)
print(s2)

s2.discard(3)
print(s2)

s3={1,2,3,4}
s3.pop()
print(s3)

s4=s3.copy()
print(s4)

s4.clear()
print(s4)

s5={1,2}
s6={4,3}
print(s5.isdisjoint(s6))
# s5和s6 相同返回（哪怕只有一个）false，完全不同返回 true



```

集合推导式

```python
ls=[1,2,3,4,5,6,7,8]
s={data for data in ls if data%2==0} #集合推导式
s1=[data for data in ls if data%2==0] #集合推导式
print(s)
print(s1)

for data in ls:
    if data%2==0:
        print(data,end=' ')
```

### 5.6   字典

#### 5.6.1 创建字典

字典的表现形式为一组包含在大括号“{}”中的键值对，每个键值对为一个字典元素，每个元素通过逗号“，”分隔，每对键值通过“：”分隔。

字典的值可以是任意类型，但键不能是列表或字典类型。字典像集合一样使用“{}”包裹元素，它也具备类似集合的特点：字典元素无序，键值必须唯一

```python
d1={}
d2={'A':123,'B':456}
d3={'c':'python',12:'ABC'}
d4=dict()
d5=dict({'D':'123','E':678})
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
```

#### 5.6.2 字典的访问

字典的值可通过“键”或内置方法get()访问

字典涉及的数据分为键、值和元素（键值对），除了直接利用键访问值外，Python还提供了内置方法keys()、values()和items()。

```python
# 第一种方法
d2={'ye':'叶','B':456}
print(d2['ye'],d2['B'])

# 第二种方法 内置的get()
print(d2.get('ye'))

# 第三种方法 keys(),valus(),items()
dic={'name':'jack','age':23,'height':185}
print(dic.keys()) #打印所有的 键
print(dic.values()) # 打印所有 值
print(dic.items())

for key in dic.keys(): # 经常会用到的方式
    print(key)

# 思考：能不能用遍历的方法打印出所有的值或键值？？
```

#### 5.6.3 字典元素的添加和修改

字典支持通过为指定的键赋值或使用update()方法添加或修改元素。

```python
add_dic={'name':'jack','age':23,'height':185}
add_dic['age']=18 # 修改元素
add_dic['sco']=98 # 添加元素
add_dic.update(height=160) # 修改元素
print(add_dic)

```

#### 5.6.4 字典元素的删除

Python支持通过pop()、popitem()和clear()方法删除字典中的元素。

```python
dic={'name':'jack','age':23,'height':185}
print(dic.pop('height')) # 删除指定的键对应的值
print(dic)

dic1={'name':'jack','age':23,'height':185}
print(dic1.popitem()) #随机删除
print(dic1)

dic2={'name':'jack','age':23,'height':185}
dic2.clear() # 清空
print(dic2)
```

#### 5.6.5 字典推导式

字典推导式的格式、用法与列表推导式类似，区别在于字典推导式外侧为大括号“{}”，且内部需包含键和值两部分。

```python
old_dict = {'name': 'Jack','age':23,'height':185}
new_dict = {value:key  for key,value in old_dict.items()}
print(new_dict)
```

### 5.8   组合数据类型与运算符

Python中针对数字类型的运算符对组合数据类型同样适用，包括+、*、in、not in。

- 字符串、列表和元组使用“ + ”运算符，会对数据进行拼接。
- 字符串、列表和元组使用“ * ”运算符，会对数据进行整数倍拼接。
- “in”“not in”运算符称为成员运算符，用于判断某个元素是否属于某个变量。

```python
str_one='hello'
str=' '
str_two='world'
print(str_one+str+str_two)
l_one=[1,2,3]
l_two=[4,5,6]
print(l_one+l_two)

ls=[1,2,3]
print(ls*3)

ls1=[1,2,3]
print(1 in ls1)
print(1 not in ls1)
```

## 第6章 函数

### 6.1 函数概述

函数是组织好的、实现单一功能或相关联功能的代码段。我们可以将函数视为一段有名字的代码，这类代码可以在需要的地方以“函数名()”的形式调用

函数式编程具有以下优点：

- 将程序模块化，既减少了冗余代码，又让程序结构更为清晰
- 提高开发人员的编程效率
- 方便后期的维护与扩展

```python
for i in range(2):
    for i in range(2):
        print('*',end=' ')
    print()

```



### 函数的定义和使用

####  6.2.1 定义函数

```python
# 函数的定义
def add(): # 无参数
    res=11+22
    print(res)

def add_modify(a,b): # 带参数,形参
    res=a+b
    add()
    print(res)
#  函数的调用
add_modify(10,20) #实参
```

#### 6.2.2 调用函数

```python
def add_modify(a,b): # 外层函数定义，带参数
    res=a+b
    print(res)

    def test(): # 内层函数定义
        print('我是内层函数')
    test() # 外层函数不能调用内层函数
add_modify(10,20)
```

### 6.3 函数参数的传递

我们通常将定义函数时设置的参数称为形式参数（简称为形参），将调用函数时传入的参数称为实际参数（简称为实参）。函数的参数传递是指将实际参数传递给形式参数的过程。

函数参数的传递可以分为**位置参数传递、关键字参数传递、默认参数传递、参数的打包与解包以及混合传递**

#### 6.3.1 位置参数的传递

函数在被调用时会将实参按照相应的位置依次传递给形参，也就是说将第一个实参传递给第一个形参，将第二个实参传递给第二个形参，以此类推。

```python
def get_max(a,b): #按位置传送
    if a>b:
        print(a,'是较大的值！')
    else:
        print(b,'是较大的值！')

get_max(8,5)
```

#### 6.3.2 关键字参数的传递

```python
def connect(ip,port): # 关键字参数的传递
    print(f'设备{ip}:{port}连接')
connect(port='3066',ip='172.0.0.1')
```

#### 6.3.3 默认参数传递

函数在定义时可以指定形参的默认值，如此在被调用时可以选择是否给带有默认值的形参传值，若没有给带有默认值的形参传值，则直接使用该形参的默认值。

```python
def con(ip,port=8080): # 默认参数传递
    print(f'设备{ip}:{port}连接')
con('192.168.1.1') # 实参就一个，另外一个用默认的
con('192.168.1.1','8000') # 实参两个
```

#### 6.3.4 参数的打包与解包 

1.  打包

如果函数在定义时无法确定需要接收多少个数据，那么可以在定义函数时为形参添加“*”或“**”：
“ *  ” —— 接收以元组形式打包的多个值
“**  ”—— 接收以字典形式打包的多个值

```python
def test(*args): # 以元组形式打包的多个值
    print(args)

test(11,22,33,44,55)

def test_dic(**kwargs): # 以字典形式打包的多个值
    print(kwargs)

test_dic(a=11,b=22,c=33)
```

2. 解包

```python
def test(a,b,c,d,e):
    print(a,b,c,d,e)
num=(11,22,33,44,55)
test(*num) # 以元组形式打解包的多个值

def test_dic(a,b,c,d,e):
    print(a,b,c,d,e)

nums={'a':11,'b':22,'c':33,'d':44,'e':55}
test_dic(**nums)
```

6.3.5 混合传递

前面介绍的参数传递的方式在定义函数或调用函数时可以混合使用，但是需要遵循一定的规则，具体规则如下。

-  优先按位置参数传递的方式。

- 然后按关键字参数传递的方式。

- 之后按默认参数传递的方式。

- 最后按打包传递的方式。

```python
def test(a,b,c=33,*args,**kwargs):
    # 位置参数，关键字参数，默认参数，元组打包，字典打包
    print(a,b,c,args,kwargs)
test(1,b=2)
test(1,2,3)
test(1,2,3,4)
test(1,2,3,4,e=5)
```

### 6.4  函数的返回值

函数中的return语句会在函数结束时将数据返回给程序，同时让程序回到函数被调用的位置继续执行。

```python
def word(words):
    if '山寨' in words:
        new_words=words.replace('山寨','**')
        return new_words # 返回语句

result=word('我这个手机是山寨版的吧！')
print(result)

def move(x,y,step):
    nx=x+step
    ny=y-step
    return nx,ny
result_move=move(100,100,60) #可以返回多个值
print(result_move)
```



#### 6.6.1 角谷猜想

```python
def guess(number):
    i = 0  # 统计变换的次数
    original_number = number  # 记录最初的number
    while number != 1:
        if number % 2 == 0:  # number为偶数
            number = number / 2
        else:  # number为奇数
            number = number * 3 + 1
        i += 1
    print(f"{original_number}经过{i}次变换后回到1")


num = int(input("请输入一个大于1的正整数:"))
guess(num)
```

### 变量作用域

变量并非在程序的任意位置都可以被访问，其访问权限取决于变量定义的位置，其所处的有效范围称为变量的作用域。

#### 6.5.1 局部变量和全局变量

根据作用域的不同，变量可以划分为局部变量和全局变量。

1. 局部变量

- 函数内部定义的变量，只能在函数内部被使用

- 函数执行结束之后局部变量会被释放，此时无法再进行访问。

```python
def test_1():
    num=10 # 局部变量
    print(num)

def test_2():
    num=20
    print(num)

test_1()
test_2()

#print(num)
```

2.  全局变量

全局变量可以在整个程序的范围内起作用，它不会受到函数范围的影响。

```python
num=10 # 全局变量
def test_1():
    print(num) # 可以访问全局变量
    # num=num+1 不能修改全局变量

test_1()

print(num)
```

#### 6.5.2 global和nonlocal关键字

1. global关键字

```python
num=10
def test():
    global num #通过 global 声明为全局变量
    num=num+1
    print(num)
test()
print(num)
```

2. nonlocal关键字

```python
def test():
    num=10
    def test_in():
        nonlocal num
        num=20

    test_in()
    print(num)
test()
```

#### 6.6.2 饮品自动售货机

```python
# 饮品信息
def all_goods():
    goods = {"可口可乐": 2.5, "百事可乐": 2.5, "冰红茶": 3, "脉动": 3.5, "果缤纷": 3,
             "绿茶": 3, "茉莉花茶": 3, "尖叫": 2.5}
    return goods


# 展示饮品信息
def show_goods():
    for x, y in all_goods().items():
        print(x, ":", str(y) + "元")


# 计算总额
def total(goods_dict):
    count = 0
    for name, num in goods_dict.items():
        total_money = all_goods()[name] * num
        # 总金额
        count += total_money
    print("需要支付金额：", count, "元")


def main():
    goods_dict = {}
    print("饮 品 自 动 售 货 机")
    show_goods()
    # 循环选购的商品
    print("输入q完成购买")
    while True:
        goods_name = input("请输入购物的商品：")
        if goods_name == 'q':
            break
        if goods_name in [g_name for g_name in  all_goods().keys()]:
            goods_num = input("请输入购物数量：")
            if goods_num.isdigit():
                goods_dict[goods_name] = float(goods_num)
            else:
                print('商品数量不合法')
        else:
            print('请输入正确的商品名称')
    total(goods_dict)


if __name__ == '__main__':
    main()

```

### 6.7   特殊形式的函数

#### 6.7.1 递归函数

若函数内部调用了自身，则这个函数被称为递归函数。

递归函数在定义时需要满足两个基本条件：一个是递归公式（调用自身），另一个是边界条件（中止条件）。其中:

- 递归公式是求解原问题或相似的子问题的结构；
- 边界条件是最小化的子问题，也是递归终止的条件。

递归函数的执行可以分为以下两个阶段：

1. 递推：递归本次的执行都基于上一次的运算结果。
2. 回溯：遇到终止条件时，则沿着递推往回一级一级地把值返回来。

#### 6.7.2  匿名函数

匿名函数是一类无需定义标识符的函数，它与普通函数一样可以在程序的任何位置使用。Python中使用lambda关键字定义匿名函数，它的语法格式如下：

lambda <形式参数列表> :<表达式>

```python
#匿名函数 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

#普通函数
def add(arg1,arg2):
    print(f'两个数字相加:{arg1+arg2}')
add(10,20)

temp=lambda x:pow(x,2)
print(f'平方：{temp(10)}')

#普通函数
def temp(n):
    print(f'平方：{n*n}')
temp(5)
```

```python
def p(n): # 普通函数p 带形参
    print(f'平方',n*n)
p(5)

p=lambda n:n*n # 用匿名函数改写
print(f'平方{p(10)}')
```



#### 6.8.1 兔子数列（斐波那契数列）

```python
def fib_recur(n):
	if n <= 1:
		return n
	else:
		return fib_recur(n-1) + fib_recur(n-2)
print('斐波那契数列:',end='')
for i in range(1, 20):
	print(fib_recur(i), end=' ')
```



```python
def fibonacci(month):
    if month == 0 or month == 1:
        return 1
    else:
        return fibonacci(month-1) + fibonacci(month-2)
# 测试经过12个月份后的兔子对数
result = fibonacci(12)
print(result)
```



###  6.9 阶段案例-学生信息管理系统

```python
"""
使用自定义函数，完成对程序的模块化
学生信息包含：姓名、性别、手机号
该系统具有的功能：添加、删除、修改、显示、退出系统
设计思路：
提示用户选择功操作
获取用户选择的功能
根据用户的选择，分别调用不同的函数
"""
# 新建一个列表，用来保存学生的所有信息
stu_info = []
# 功能打印
# 打印功能菜单
def print_menu():
    print('=' * 30)
    print('学生管理系统 V10.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询所有学生信息')
    print('0.退出系统')
    print('=' * 30)


# 添加学生信息
def add_stu_info():
    # 提示并获取学生的姓名
    new_name = input('请输入新学生的姓名:')
    # 提示并获取学生的性别
    new_sex = input('请输入新学生的性别:')
    # 提示并获取学生的手机号
    new_phone = input('请输入新学生的手机号码:')
    new_info = dict()
    new_info['name'] = new_name
    new_info['sex'] = new_sex
    new_info['phone'] = new_phone
    stu_info.append(new_info)


# 删除学生信息
def del_stu_info(student):
    del_num = int(input('请输入要删除的序号：')) - 1
    del student[del_num]
    print("删除成功！")


# 修改学生信息
def modify_stu_info():
    if len(stu_info) != 0:
        stu_id = int(input('请输入要修改学生的序号:'))
        new_name = input('请输入要修改学生的姓名:')
        new_sex = input('请输入要修改学生的性别:(男/女)')
        new_phone = input('请输入要修改学生的手机号码:')
        stu_info[stu_id - 1]['name'] = new_name
        stu_info[stu_id - 1]['sex'] = new_sex
        stu_info[stu_id - 1]['phone'] = new_phone
    else:
        print('学生信息表为空')


# 显示所有的学生信息
def show_stu_info():
    print('学生的信息如下：')
    print('=' * 30)
    print('序号    姓名    性别    手机号码')
    i = 1
    for tempInfo in stu_info:
        print("%d    %s    %s    %s" % (i, tempInfo['name'],
               tempInfo['sex'], tempInfo['phone']))
        i += 1


# 在main函数中执行不同的功能
def main():
    while True:
        print_menu()      # 打印功能菜单
        key = input("请输入功能对应的数字：")  # 获取用户输入的序号
        if key == '1':    # 添加学生信息
            add_stu_info()
        elif key == '2':  # 删除学生信息
            del_stu_info(stu_info)
        elif key == '3':  # 修改学生信息
            modify_stu_info()
        elif key == '4':  # 查询所有学生信息
            show_stu_info()
        elif key == '0':
            quit_confirm = input('亲，真的要退出么？(Yes or No):').lower()
            if quit_confirm == 'yes':
                print("谢谢使用！")
                break  # 跳出循环
            elif quit_confirm == 'no':
                continue
            else:
                print('输入有误!')



if __name__ == '__main__':
    main()

```

## 第七章 文件与数据格式化

### 7.1 文件概述

计算机文件是以计算机硬盘为载体存储在计算机上的信息集合。

文件标识：

- 文件标识的意义：找到计算机中唯一确定的文件。
- 文件标识的组成：文件路径、文件名主干、文件扩展名。
- 操作系统以文件为单位对数据进行管理

文件类型

根据数据的逻辑存储结构，人们将计算机中的文件分为文本文件和二进制文件。

- 文本文件：专门存储文本字符数据。
- 二进制文件：不能直接使用文字处理程序正常读写，必须先了解其结构和序列化规则，再设计正确的反序列化规则，才能正确获取文件信息。

### 7.2 文件的基础操作

文件的打开、关闭与读写是文件的基础操作，任何更复杂的文件操作都离不开这些操作。

#### 7.2.1 文件的打开与关闭

1. 打开文件

```python
file1=open('f:\\a.txt') # 只读方式，默认
```

2.  关闭文件

```python
file.close()
```

当打开文件与关闭之间的操作较多时，很容易遗漏文件关闭操作，为些Python引入with语句预定义清理操作、实现文件的自动关闭。

```python
with open('f:\\a.txt') as f:
	pass 
```



#### 7.2.2 文件的读写

1.  读取文件

- read()方法

```python
with open('f:\\a.txt') as f:
	print(f.read(2)) # 读取两个字符
	print(f.read())  # 读取所有字符
```

- readline() 方法

```python
with open('f:\\a.txt') as f:
	print(f.readline()) # 读取一行
	print(f.readline())
```

- readlines()方法

```python
with open('f:\\a.txt') as f:
	print(f.readlines()) # 读取所有内容，以列表方式输出
```



2. 写入文件

- write() 方法

```python
string = "Here we are all, by day; by night."
with open('f:\\b.txt','w') as f:
	size=f.write(string) # 以指定字符串写入
	print(size)
```

- writelines()方法

```python
string1 = "Here we are all, by day;\nby night we're hurl'd By dreams, \
each one into a several world."
with open('f:\\c.txt', mode='w', encoding='utf-8') as f:
	f.writelines(string1) # 以行列表写入
```

#### 7.2.3 文件的定位读写

•在文件的一次打开与关闭之间进行的读写操作是连续的，程序总是从上次读写的位置继续向下进行读写操作。

•每个文件对象都有一个称为“文件读写位置”的属性，该属性会记录当前读写的位置。

•文件读写位置默认为0，即在文件首部。

1. tell()方法

```python
with open('d:\\a.txt') as f:
	print(f.tell())
	print(f.read(5))
	print(f.tell())
```

2. seek()方法

在Python3中，若打开的是文本文件，那么seek()方法只允许相对于文件开头移动文件位置，若在参数from值为1、2的情况下对文本文件进行位移操作，将会产生错误。

```python
with open('d:\\a.txt') as f:
	print(f.seek(5,0))
```

Python提供了seek()方法，使用该方法可控制文件的读写位置，实现文件的随机读写。seek()方法的语法格式如下：

seek(offset, from)

poffset：表示偏移量，即读写位置需要移动的字节数。

pfrom：用于指定文件的读写位置，该参数的取值为0、1、2。

0：表示文件开头。

1：表示使用当前读写位置。

2：表示文件末尾。

seek()方法调用成功后会返回当前读写位置。

```python
with open('d:\\a.txt','rb') as f:
	print(f.seek(5,1))
```

### 7.3    文件与目录管理

1. 删除文件-remove()函数

```python
import os
os.remove('d:\\a.txt')
```

2. 文件重命名-rename()函数

```python
# rename(原文件名,新文件名)
import os
os.rename('d:\\a.txt','b.txt')

```

3.  创建/删除目录-mkdir()/rmdir()函数

```python
import os
os.mkdir('d:\\dir')
os.rmdir('d:\\dir')
```

4. 获取当前目录-getcwd()函数

```python
import os
os.getcwd()
# 'C:\\Users\\Teacher\\AppData\\Local\\Programs\\Python\\Python38'
```

5. 更改默认目录-chdir()函数

```python
os.chdir('d:\\dir')
```

6. 获取文件名列表-listdir()函数

```python
import os
dirs=os.listdir('d:\\')
print(dirs)
```

### 7.4 实训案例

#### 7.4.1 信息安全策略--文件备份

```python
import os
def file_backups(file_name, path):
    # 备份的文件名
    file_back = file_name.split('\\')[-1]
    # 判断用户输入的内容是文件还是文件夹
    if os.path.isdir(file_name) is not True:
        with open(file_name, mode='r') as file_data:
            # 创建新文件 , 以只读的方式打开
            new_path = path + '/' + file_back
            with open(new_path, 'w') as file_back:
                # 逐行复制源文件内容到新文件中
                for line_content in file_data.readlines():
                    file_back.write(line_content)

# 判断是目录还是文件
def judge(back_path, file_path):
    if os.path.isdir(file_path) is True:
        # 遍历当前目录下的文件
        file_li = os.listdir(file_path)
        for i in file_li:
            # 拼接文件名称
            new_file = file_path + '\\' + i
            file_backups(new_file, back_path)
    else:
        # 是文件
        if os.path.exists((file_path)):
            file_backups(file_path, back_path)
        else:
            print("备份的文件不存在!")
            exit()

# 备份目录
def backups_catalog():
    # 指定备份的目录
    back_path = input("请输入备份的目录：\n")
    file_path = input("请输入备份的文件:\n")
    # 指定目录不存在
    if os.path.exists(back_path) is False:
        os.mkdir(back_path)
        judge(back_path, file_path)
        print('备份成功!')
    # 指定目录存在
    else:
        judge(back_path, file_path)
        print('备份成功!')

if __name__ == '__main__':
    backups_catalog()

​```
请输入备份的目录：
d:\dir\b
请输入备份的文件:
d:\dir
备份成功!
​```
```

### 7.5 数据维度与数据格式化

#### 7.5.1 基于维度的数据分类

从广义上讲，维度是与事物“有联系”的概念的数量，根据“有联系”的概念的数量，事物可分为不同维度

基于维度的数据分类：根据组织数据时与数据有联系的参数的数量，数据可分为一维数据、二维数据和多维数据。

#### 7.5.2 一二维数据的存储与读写

- 数据读取

```python
csv_file=open('score.csv','r',encoding='utf-8')  # 打开文件，只读，编码方式utf-8
lines=[]  # 空列表
for line in csv_file:  # 遍历
    line=line.replace('\n','')  # replace字符串替换函数
    lines.append(line.split(','))  # split分割函数，以逗号分割.append函数添加到列表尾部
print(lines)
csv_file.close()  # 关掉文件
```

- 数据写入

```python
csv_file = open('score.csv', 'r', encoding='utf-8')
file_new = open('count.csv', 'w+', encoding='utf-8')
lines = []
for line in csv_file:
    line = line.replace('\n', '')
    lines.append(line.split(','))
lines[0].append('总分')
lines[0].append('平均分')

for i in range(len(lines) - 1):
    idx = i + 1
    sun_score = 0
    for j in range(len(lines[idx])):
        if lines[idx][j].isnumeric():  # isnumeric()函数，检测字符串是否由数字组成，是返回Ture，否返回False
            sun_score += int(lines[idx][j])
    lines[idx].append(str(sun_score))  # 总分
    lines[idx].append(str(sun_score/4))  # 平均分
for line in lines:
    print(line)
    file_new.write(','.join(line) + '\n')  # 写入，以逗号拼接
csv_file.close()
file_new.close()


```

## 第8章 面向对象

### 8.1 面向对象概述

面向对象是程序开发领域的重要思想，这种思想模拟了人类认识客观世界的思维方式，将开发中遇到的事物皆看作对象。

面向过程：

- 分析解决问题的步骤
- 使用函数实现每个步骤的功能
- 按步骤依次调用函数

面向对象：

- 分析问题，从中提炼出多个对象
- 将不同对象各自的特征和行为进行封装
- 通过控制对象的行为来解决问题。

### 8.2   类的定义与使用

面向对象编程有两个非常重要的概念：**类和对象**

对象映射现实中真实存在的事物。如一本python快速编程入书。或者说对象是类的实例

具有相同特征和行为的事物的集合统称为类。例如“书是人类进步的阶梯”

对象是根据类创建的，一个类可以对应多个对象

#### 8.2.1 类的定义

类是由3部分组成的：

- 类的名称：大驼峰命名法，首字母一般大写，比如Car。
-   类的属性：用于描述事物的特征，比如车轮（相当于变量）
-   类的方法：用于描述事物的行为，比如行驶。（相当于函数）

类成员包括：属性和方法

```
class 类名:
       属性名 = 属性值
       def 方法名(self): 
              方法体
```

#### 8.2.2 对象的创建与使用

根据类创建对象的语法格式如下： 

```
对象名 = 类名()
```

```python
# 类的定义
class Car: # 类名，首字母大写
    wheels=4 # 属性
    def drive(self): # 方法，注意参数self不能省略
        print("行驶") # 方法体

# 对象的创建
car=Car()
print(car.wheels)
car.drive()

print(f"汽车有{car.wheels}只轮子，正在",end='')
car.drive()

```

```python
class Stu:
    name="小王"
    # 编写跑步的方法
    def run(self):
        print("跑步")

stu=Stu()
print(stu.name)
stu.run()
print(f"同学叫{stu.name},正在",end='')
stu.run()
```

### 8.3    类的成员

#### 8.3.1 属性

属性按声明的方式可以分为两类：类属性和实例属性

- 类属性

声明在类内部、方法外部的属性。
可以通过类或对象进行访问，但只能通过类进行修改。

```python
class Car:
    wheels = 4  # 类属性。类内部，方法外部
                # 可以通过 类或对象，但只有类才能修改
    def drive(self):
        print("行驶")


car = Car()
print(Car.wheels)  # 类访问
print(car.wheels)  # 对象访问

Car.wheels = 3
print(Car.wheels)  # 类访问
print(car.wheels)  # 对象访问

car.wheels = 5  # 动态添加实例属性
print(Car.wheels)  # 类访问
print(car.wheels)  # 对象访问 实例属性

```

- 实例属性

实例属性是在方法内部声明的属性。
Python支持动态添加实例属性。

```python
class Car:
    def drive(self):
        self.wheels = 4  # 实例属性。只出现在方法内部的
        # 只能通过对象访问


car = Car()
car.drive()

print(car.wheels)
# print(Car.wheels)

car.wheels=3  # 可以通过对象进行修改
print(car.wheels)

# 动态添加实例属性
car.color='红色'
print(car.color)
```



#### 8.3.2 方法

Python中的方法按定义方式和用途可以分为三类：实例方法、类方法和静态方法。

1. 实例方法

- 形似函数，但它定义在类内部。
- 以self为第一个形参，self参数代表对象本身
- 只能通过对象调用

```python
class Car:
    def drive(self):
        print('我是实例方法')
car=Car()
car.drive()
# Car.drive()

```

2. 类方法

- 类方法是定义在类内部
- 使用装饰器@classmethod修饰的方法
- 第一个参数为cls，代表类本身
- 可以通过类和对象调用

```python
class Car:
    @classmethod  # 装饰器，告诉计算机我是类方法
    def stop(cls): # 形参 cls
        print('我是类的方法')

car=Car()
car.stop()
Car.stop() # 类方法可以通过，类或对象调用
```

类方法中可以使用cls访问和修改类属性的值

```python
class Car:
    wheels=4
    @classmethod  # 装饰器，告诉计算机我是类方法
    def stop(cls): # 形参 cls。类方法中可以使用cls访问和修改类的属性的值
        print(cls.wheels)  # cls.whells 是类属性
        cls.wheels=3  # 修改类属性
        print(cls.wheels)

car=Car()
car.stop()
```

3. 静态方法

- 静态方法是定义在类内部
- 使用装饰器@staticmethod修饰的方法
- 没有任何默认参数

```python
class Car: # 静态方法
    @staticmethod
    def test():
        print('我是静态方法')

car=Car()
car.test()
Car.test()
```

```python
class Car:
    wheels=4
    @staticmethod
    def test():  # 静态方法,在内部可以通过类名访问类属性
        print('我是静态方法')
        print(f'类属性的值{Car.wheels}')

car=Car()
car.test()
Car.test()
```



属性

- 类属性
  - 在方法外部。可以通过 类或对象访问，但只能由类修改
- 实例属性
  - 在方法内部。只能通过对象访问，也只能通过对象修改

方法

- 实例方法
  - 形参 self
- 类方法
  - 装饰器 @classmethod  形参 cls
  - 可以通过 类或对象调用
  - 类方法中可以使用cls访问和修改类属性的值
- 静态方法
  - 装饰器@staticmethod   形参 空
  - 可以通过 类或对象调用
  - 静态方法中可以通过类名访问属性或调用方法

#### 8.3.3 私有成员 

类的成员默认是公有成员，可以在类的外部通过类或对象随意地访问，这样显然不够安全。
为了保证类中数据的安全，Python支持将公有成员改为私有成员，在一定程度上限制在类的外部对类成员的访问。

Python通过在类成员的名称前面添加双下画线（__）的方式来表示私有成员，语法格式如下：

`__属性名`

`__方法名`

私有成员在类的内部可以直接访问，在类的外部不能直接访问，但可以通过调用类的公有成员方法的方式进行访问。

```python
class Car:
    __wheels=4  # 私有类属性
    def __drive(self): # 私有方法
        print("行驶")
    def test(self):    # 公有方法
        print(f'轿车有{self.__wheels}个轮') #通过公有方法内部访问私有成员
        self.__drive()
car=Car()
# print(car.wheels)
# car.drive()
car.test()
```



### 8.4  特殊方法

类中还包括两个特殊的方法：构造方法和析构方法，这两个方法都是系统内置方法。

#### 8.4.1 构造方法

构造方法指的是`__init__()`方法。
创建对象时系统自动调用，从而实现对象的初始化。
每个类默认都有一个`__init__()`方法，可以在类中显式定义`__init__()`方法。
`__init__()`方法可以分为无参构造方法和有参构造方法。

- 当使用无参构造方法创建对象时，所有对象的属性都有相同的初始值。

```python
class Car:
    def __init__(self): #构造方法
        # 使用无参构造方法创建对象时，所有对象的属性都有相同的初始值。
        self.color='红色'

    def drive(self): #实例方法
        print(f'车的颜色为:{self.color}')

car_one=Car()
car_one.drive()

car_two=Car()
car_two.drive()
```

- 当使用有参构造方法创建对象时，对象的属性可以有不同的初始值。

```python
class Car:
    def __init__(self,color): #构造方法
        # 当使用有参构造方法创建对象时，对象的属性可以有不同的初始值。
        self.color=color
    def drive(self): #实例方法
        print(f'车的颜色为:{self.color}')
car_one=Car('红色')
car_one.drive()
car_one=Car('黄色')
car_one.drive()
```



#### 8.4.2 析构方法

析构方法（即`__del__`方法）是销毁对象时系统自动调用的方法。
每个类默认都有一个`__del__`方法，可以显式定义析构方法。

```python
class Car:
    def __init__(self): # 构造方法 无参
        self.color = "蓝色"
        print("对象被创建")
    def __del__(self): # 当删除对象后，自动调用析构方法
        print("对象被销毁")
car = Car()
print(car.color)
del car # 删除对象
print(car.color) # 对象不存在，而报错

```

与文件类似，每个对象都会占用系统的一块内存，使用之后若不及时销毁，会浪费系统资源。那么对象什么时候销毁呢？

Python通过引用计数器记录所有对象的引用（可以理解为对象所占内存的别名）数量，一旦某个对象的引用计数器的值为0，系统就会销毁这个对象，收回对象所占用的内存空间。

### 8.6  封装

封装、继承、多态是面向对象三个重要特性

封装是面向对象的重要特性之一，它的基本思想是对外隐藏类的细节，提供用于访问类成员的公开接口。
如此，类的外部无需知道类的实现细节，只需要使用公开接口便可访问类的内容，这在一定程度上保证了类内数据的安全。

为了契合封装思想，我们在定义类时需要满足以下两点要求。
1．将类属性声明为私有属性。
2．添加两类供外界调用的公有方法，分别用于设置或获取私有属性的值。

```python
class Person:  # 定义类
    def __init__(self, name):  # 构造方法，初始化
        self.name = name
        self.__age = 1  # 这个私有属性，只有通过公有方法访问或修改

    def set_age(self, new_age):  # 修改私有属性
        if 0 < new_age <= 120:
            self.__age = new_age

    def get_age(self):  # 通过公有方法，获取私有属性
        return self.__age


persor = Person('小明')
persor.set_age(20)
print(f'{persor.name}的年龄为{persor.get_age()}岁')
```

### 8.7    继承

继承是面向对象的重要特性之一，它主要用于描述类与类之间的关系，在不改变原有类的基础上扩展原有类的功能。
若类与类之间具有继承关系，被继承的类称为父类或基类，继承其他类的类称为子类或派生类，子类会自动拥有父类的公有成员。



#### 8.7.1 单继承

单继承即子类只继承一个父类。现实生活中，波斯猫、折耳猫、短毛猫都属于猫类，它们之间存在的继承关系即为单继承

```
Python中单继承的语法格式如下所示：
class 子类名(父类名)：
```



```python
class Cat(object):
    def __init__(self,color):
        self.color=color
        # self.__age=1 只能继承公有方法或属性
        self.age=1
    def walk(self):
        print("走猫步。。。")

class Sfold(Cat):
    pass #略，什么代码都不写

flod=Sfold('灰色')
print(f'{flod.color}的波斯猫，今年{flod.age}岁')
flod.walk()

```



####  8.7.2 多继承

```python
class House(object):
    def live(self):
        print("居住")
class Car(object):
    def drive(self):
        print("行驶")

class Tcar(House,Car):
    pass

tcar=Tcar()
tcar.live()
tcar.drive()
```



#### 8.7.3 重写

子类会原封不动地继承父类的方法，但子类有时需要按照自己的需求对继承来的方法进行调整，也就是在子类中重写从父类继承来的方法

在子类中定义与父类方法同名的方法，在方法中按照子类需求重新编写功能代码即可

```python
# 定义一个表示人的类
class Person(object): # 父类
    def say_hello(self):
        print("打招呼方式")
# 定义一个表示中国人的类
class Chinese(Person): # 子类
    def say_hello(self):  					# 重写的方法
        super().say_hello() # 引用 父类的say_hello方法
        print("中国人：吃了吗？")
class Bri(Person):
    def say_hello(self):
        super().say_hello()
        print('英国人：hello')
chinese = Chinese()
chinese.say_hello()
bri=Bri()
bri.say_hello()
```



### 8.8 多态

多态是面向对象的重要特性之一，它的直接表现即让不同类的同一功能可以通过同一个接口调用，表现出不同的行为。

```python
'''
多态是面向对象的重要特性之一，它的直接表现即让不同类的同一功能可以通过同一个接口调用，表现出不同的行为。
'''


class Cat:
    def shout(self):  # 实例方法
        print("喵喵....")


class Dog:
    def shout(self):
        print("汪汪....")


def shout(obj):  # 同一个接口 函数定义
    obj.shout()


cat = Cat()  # 创建对象
dog = Dog()

shout(cat)  # 函数调用
shout(dog)
```



### 8.9 运算符重载

运算符重载是指赋予内置运算符新的功能，使内置运算符能适应更多的数据类型。

如果类中重写了Python基类object内置的有关运算符的特殊方法，那么该特殊方法对应的运算符将支持对该类的实例进行运算。

```python
class Calculator(object):
    def __init__(self, number):  # 构造函数，记录数值
        self.number = number

    def __add__(self, other):  # 重载运算符+
        self.number = self.number + other
        return self.number

    def __sub__(self, other):  # 重载运算符-
        self.number = self.number - other
        return self.number

    def __mul__(self, other):  # 重载运算符*
        self.number = self.number * other
        return self.number

    def __truediv__(self, other):  # 重载运算符/
        self.number = self.number / other
        return self.number

calculator = Calculator(10)
print(calculator + 5)
print(calculator - 5)
print(calculator * 5)
print(calculator / 5)
```





```python
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d,%d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

```

### 8.10 实训案例

#### 8.4.2 自定义列表

```python
"""
from custom_list import MyList
add_demo = MyList(1,2,3,4,5)
print(add_demo+5)   每个元素都加5，并返回新的列表
"""

class MyList:
    def __isnumber(self, n):
        if not isinstance(n, (int, float, complex)):
            return False
        return True
    # 构造函数，进行必要的初始化
    def __init__(self, *args):
        for arg in args:
            if not self.__isnumber(arg):
                print('所有的元素必须是数字类型')
                return
        self.__value = list(args)
    def __str__(self):
        return str(self.__value)
    def __del__(self):
        del self.__value
    # 重载运算符+
    def __add__(self, num):
        if self.__isnumber(num):
            # 数组中所有元素都与数字num相加
            my_list = MyList()
            my_list.__value = [elem + num for elem in self.__value]
            return my_list
    # 重载运算符-
    # 数组中每个元素都与数字num相减，返回新数组
    def __sub__(self, num):
        if not self.__isnumber(num):
            print('所有的元素必须是数字类型')
            return
        my_list = MyList()
        my_list.__value = [elem - num for elem in self.__value]
        return my_list
    # 重载运算符*
    # 数组中每个元素都与数字num相乘，返回新数组
    def __mul__(self, num):
        if not self.__isnumber(num):
            print('所有的元素必须是数字类型')
            return
        my_list = MyList()
        my_list.__value = [elem * num for elem in self.__value]
        return my_list
    # 重载运算符/
    # 数组中每个元素都与数字num相除，返回新数组
    def __truediv__(self, num):
        if not self.__isnumber(num):
            print('所有的元素必须是数字类型')
            return
        my_list = MyList()
        my_list.__value = [elem / num for elem in self.__value]
        return my_list
        
add_demo = MyList(1,2,3,4,5)
print(add_demo+5)
        
```





### 8.11 总结

1. 面向对象的概述
2. 类和对象
3. 类的成员
   - 属性
     - 类属性
     - 实例属性
   - 方法
     - 实例方法
     - 类方法
     - 静态方法
4. 私有成员
5. 特殊方法
   - 构造方法
   - 析构方法
6. 三大特性
   - 封装
   - 继承
     - 单继承
     - 多继承
   - 多态
7. 运算符重载

## 第九章 异常

###  9.1 异常概述

#### 9.1.1 认识异常

程序开发或运行时可能出现异常，开发人员和运维人员需要辨别程序的异常，明确这些异常是源于程序本身的设计问题，还是由外界环境的变化引起，以便有针对性地处理异常

程序运行出现异常时，若程序中没有设置异常处理功能，解释器会采用系统的默认方式处理异常，即返回异常信息、终止程序。

异常信息中通常包含异常代码所在行号、异常的类型和异常的描述信息。

```python
>>> 10/0
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
```

#### 9.1.2 异常的类型

Python程序运行出错时产生的每个异常类型都对应一个类，程序运行时出现的异常大多继承自Exception类，Exception类又继承了异常类的基类BaseException。

1. NameError

NameError是程序中使用了未定义的变量时会引发的异常。

```python
>>> print(test)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(test)
NameError: name 'test' is not defined
```

2. IndexError

IndexError是程序越界访问时会引发的异常。

```python
>>> List=[1,2,3]
>>> List[4]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    List[4]
IndexError: list index out of range
```

3. AttributeError

AttributeError是使用对象访问不存在的属性时引发的异常。

```python
>>> class Car:
	pass

>>> car=Car()
>>> car.color='黑色'
>>> car.brand='宝马'
>>> car.color
'黑色'
>>> car.barn
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    car.barn
AttributeError: 'Car' object has no attribute 'barn'
```

4. FileNotFoundError

FileNotFoundError是未找到指定文件或目录时引发的异常。

```python
>>> file=open("test.txt")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    file=open("test.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
```

5. SyntaxError

SyntaxError是指语法错误

```python
>>> for i range(10):
	
SyntaxError: invalid syntax
```

### 9.2 异常捕获语句

Python既可以直接通过try-except语句实现简单的异常捕获与处理的功能，也可以将try-except语句与else或finally子句组合实现更强大的异常捕获与处理的功能。

```
try:
    可能出错的代码
except [异常类型 [as error]]:                    # 将捕获到的异常对象赋error
    捕获异常后的处理代码

```

try-except语句可以捕获与处理程序的单个、多个或全部异常。

```python
num1=int(input("请输入被除数："))
num2=int(input("请输入除数："))
try:
    print("结果为：",num1/num2)
except ZeroDivisionError as error:
    print("出错了",error)

'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ZeroDivisionError: division by zero
'''
```

#### 9.2.2	 异常结构中的else子句

else子句可以和try-except一起使用，语法格式如下：

```
try:
    可能出错的代码
except [异常类型 [as error]]:                    # 将捕获到的异常对象赋值error
    捕获异常后的处理代码
else:
    未捕获异常后的处理代码

```

```python
first_num = int(input("请输入被除数："))
second_num = int(input("请输入除数："))
try:
    res = first_num/second_num # 可能出错的代码
except ZeroDivisionError as error:
    print('异常原因：',error) # 出错了的处理代码
else:
    print("没有错误，正常输出：",res) #没有出错的处理代码
```

#### 9.2.3	异常结构中的finally子句

finally子句可以和try-except一起使用，语法格式如下：

```python
try:
    可能出错的代码
except [异常类型 [as error]]:                    # 将捕获到的异常对象赋值error
    捕获异常后的处理代码
finally:
    一定执行的代码

```



```python
try:
    file = open('./file.txt', mode='r', encoding='utf-8')
    print(file.read())
except FileNotFoundError as error:
    print(error)
finally: # 不管有没有异常，一定要执行的代码
    file.close()
    print('文件已关闭')

```

### 9.3    抛出异常

Python程序中的异常不仅可以自动触发异常，而且还可以由开发人员使用raise和assert语句主动抛出异常。

#### 9.3.1 使用raise语句抛出异常

raise 异常类				# 格式1：使用异常类名引发指定的异常
raise 异常类对象				# 格式2：使用异常类的对象引发指定的异常
raise 					# 格式3： 使用刚出现过的异常重新引发异常

-  异常类

```python
>>> raise IndexError
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise IndexError
IndexError
```

- 异常类对象

```python
>>> raise IndexError()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    raise IndexError()
IndexError
>>> raise IndexError('下标超出索引')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    raise IndexError('下标超出索引')
IndexError: 下标超出索引
```

- 重新引发异常

```python
>>> try:
	raise IndexError
except:
	raise

Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    raise IndexError
IndexError
```

#### 9.3.2 使用assert语句抛出异常

assert语句又称为断言语句(开发调试阶段)，其语法格式如下所示：

assert 表达式[,  异常信息]

表达式值：False  执行异常

​				   True  不执行任何操作

```python
num_one = int(input("请输入被除数："))
num_two = int(input("请输入除数："))
assert num_two != 0, '除数不能为0'  # assert语句判定num_two不等于0
result = num_one / num_two
print(num_one, '/', num_two, '=', result)
```

#### 9.3.3 异常的传递

如果程序中的异常没有被处理，默认情况下会将该异常传递到上一级，如果上一级仍然没有处理异常，那么会继续向上传递，直至异常被处理或程序崩溃

```python
def get_width():
    print("get_width开始执行")
    num=int(input("请输入除数："))
    width_len=10/num
    print("get_width执行结束")
    return width_len
def calc_area():
    print('calc_area开始结束')
    width_len=get_width()
    print('calc_area执行结束')
    return width_len*width_len
def show_area():
    try:
        print('show_area开始执行')
        area_val=calc_area()
        print(f'正方形的面积是：{area_val}')
        print('show_area执行结束')
    except ZeroDivisionError as e:
        print(f'捕捉到异常：{e}')
show_area()
```

#### 9.4    自定义异常

有时我们需要自定义异常类，以满足当前程序的需求。自定义异常的方法比较简单，只需要创建一个继承Exception类或Exception子类的类（类名一般以“Error”为结尾）即可。

```python
class ShortInputError(Exception):  #自定义异常类n 继承Exception类或Exception子类的类 （类名一般以“Error”为结尾)
    '''自定义异常类'''
    def __init__(self, length, atleast):
        self.length = length  	            # 输入的密码长度
        self.atleast = atleast  	            # 限制的密码长度
try:
    text = input("请输入密码：")
    if len(text) < 3:
        raise ShortInputError(len(text), 3)
except ShortInputError as result: # result相当于对象名
    print("ShortInputError：输入的长度是%d，长度至少应是 % d" %
          (result.length, result.atleast)) # 访问实例属性
else:
    print("密码设置成功")

```



## 第10章  Python计算生态

### 10.1    Python计算生态概述

Python计算生态涵盖网络爬虫、数据分析、文本处理、数据可视化、图形用户界面、机器学习、Web开发、网络应用开发、游戏开发、虚拟现实、图形艺术等多个领域，为各个领域的Python使用者提供了极大便利。



终端

`pip install 库名`

`pip install requests`

`pip install beautifulsoup4`

在控制台下面测试

`import requests`

`from bs4 import BeautifulSoup`