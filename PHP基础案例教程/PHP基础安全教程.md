# PHP基础案例教程

[toc]

## PHP开篇

### 1.1 PHP基础知识

#### 1.1.1 Web技术

含义：Web的本意是蜘蛛网，在计算机领域中称为网页
构成：它是一个由很多互相链接的超文本文件组成的系统
资源：系统中每个有用的文件都称为“资源”，并由“通用资源标识符”（URI）进行定位，这些资源通过超文本传输协议（Hypertext Transfer Protocol，HTTP）传送给用户，用户单击链接即可获得资源。

B/S（Browser/Server）架构：指的是浏览器/服务器端的交互

C/S（Client/Server）架构：指的是客户端/服务器端的交互

`http://www.itheima.com:80/index.html`

由于80是Web服务器的默认端口号，因此可以省略URL中的“:80”
即：http://www.itheima.com/index.html

#### 1.1.2 PHP概述

PHP: Hypertext Preprocessor（超文本预处理器）
PHP是全球网站使用最多的脚本语言之一
全球前100万的网站中，有超过70%的网站是使用PHP开发的

LAMP：PHP与Linux、Apache和MySQL共同组成一个强大的Web应用程序平台

特点：

- 开源免费
- 面向对象
- 快捷性
- 跨平台性
- 支持多种数据库
- PHP中可嵌入HTML，编辑简单、实用性强、程序开发快

### 1.2 WampServer的安装和使用（实训手册）

- 实训说明

图标颜色：绿色表示相关服务已经启动成功，黄色表示部分启动，红色表示已停止。

`http://localhost/文件名称.php`

- 实训任务描述
- 常见错误

403（Forbidden，拒绝访问）
404（Not Found，页面未找到）
500（Internal Server Error，服务器内部错误）




### 1.3 PHP编程快速体验

编写hello world程序

```php
<?php
echo 'hello world'; //全部英文和标点符号都要在输入法英文状态下
```

进行一些加，减等运算

```php
<?php
echo 230+100;
echo '<br>';//输出一个换行
echo 2*3+25/5-4;
?>
```

和字母混合编写

```php
aaa <?php echo 200+200; ?>ccc
<br>
<?php echo 300+300; ?>
```

PHP代码嵌入HTML

```php
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title><?php echo '这是标题'; ?></title>
    <style>
        body { background-color: <?php echo 'black'; ?>; }
    </style>
    <script>
        alert(<?php echo 10 + 20; ?>);
    </script>
</head>
<body>
<font color="<?php echo 'white'; ?>">
    <?php echo '<strong>黑马</strong>'; ?>程序员
</font>
</body>
</html>
```



## 第2 章 PHP基本语法

### 2.1 标记与注释

标记：由于PHP 是嵌入式脚本语言，它在实际开发中经常会与HTML内容混编在一起，所以为了区分HTML与PHP代码，需要使用标记对PHP代码进行标识。

- 混合

```php
<html>
<body>
<p>
    hello THML
</p>
<p>
    <?php  echo 'hello php' ?> //与HTML语句混合编写时标记开始和结束要成对
</p>
</body>
</html>
```

- 纯PHP

```php
<?php
echo 'hello php';//纯PHP语句，可以只要开始标记
```



注释：在PHP开发中，为了便于对代码的阅读和维护，可以使用注释来进行解释和说明。它在程序解析时会被PHP解析器忽略。

```php
<?php
echo 'hello php';
//纯PHP语句，可以只要开始标记
# SHELL风格的注释
/*
echo 'hello php';
echo 'hello html';
*/
```



输出语句：使用很简单，它不仅可以输出各种类型的数据，还可以在学习和开发中进行简单的调试。

- echo
- print
- print_r()
- var_dump()

```php
<?php
echo 'true';
echo 'result=',4+3*3; //echo 可以输出多个。
echo '<br>';

print 'best';//只能输出一个。
echo '<br>';

print_r('hello');//是PHP的内置函数
echo '<br>';

var_dump(2);//是PHP的内置函数,可以先判断类型和个数
echo '<br>';
var_dump('php','c',3);
```



标识符：PHP程序开发中，经常需要自定义一些符号来标记一些名称，如变量名、函数名、类名等，这些符号被称为标识符。

标识符的定义需要遵循一定的规则，具体如下：

- 标识符只能由字母、数字、下划线组成，且不能包含空格
- 标识符只能以字母或下划线开头的任意长度的字符组成
- 标识符用做变量名时，区分大小写
- 如果标识符由多个单词组成，那么应使用下划线进行分隔（例如：user_name）



关键字：是编程语言里事先定义好并赋予特殊含义的单词，也称作保留字。和其他语言一样，PHP中保留了许多关键字，例如class、public等。

| __halt_compiler() | abstract   | and        | array()        | as           |
| ----------------- | ---------- | ---------- | -------------- | ------------ |
| break             | ●callable  | case       | catch          | class        |
| clone             | const      | continue   | declare        | default      |
| die()             | do         | echo       | else           | elseif       |
| empty()           | enddeclare | endfor     | endforeach     | endif        |
| endswitch         | endwhile   | eval()     | exit()         | extends      |
| final             | ▲finally   | for        | foreach        | function     |
| global            | ★goto      | if         | implements     | include      |
| include_once      | instanceof | ●insteadof | interface      | isset()      |
| list()            | ★namespace | new        | or             | print        |
| private           | protected  | public     | require        | require_once |
| return            | static     | switch     | throw          | ●trait       |
| try               | unset()    | use        | var            | while        |
| xor               | ▲yield     | __CLASS__  | ★__DIR__       | __FILE__     |
| __FUNCTION__      | __LINE__   | __METHOD__ | ★__NAMESPACE__ | ●__TRAIT__   |

### 2.2 数据与运算

常量

概念：常量就是在脚本运行过程中值始终不变的量。
特点：是一旦被定义就不能被修改或重新定义。

```php
<?php  //常量
    define('PAI','3.14');//define('常量名','值');
    define('R','5',true);//define('常量名','值','是否区分大小写');
    echo '圆周率=',PAI;
    echo '半径=',R;
    echo '半径=',r;
    echo '<br>';

    const R=6; //const 是关键字，它可以是表达式
    const P=2*R;
    echo 'P=',P;
```

预定义常量

| **常量名**  | **功能描述**                           |
| ----------- | -------------------------------------- |
| __FILE__    | PHP程序文件名                          |
| __LINE__    | PHP程序中的当前行号                    |
| PHP_VERSION | PHP程序的版本，如“7.1.4”               |
| PHP_OS      | 执行PHP解析器的操作系统名称，如“WINNT” |
| TRUE        | 该常量是一个真值（true）               |
| FALSE       | 该常量是一个假值（false）              |
| NULL        | 该常量是一个空值（null）               |
| E_ERROR     | 该常量表示错误级别为致命错误           |
| E_WARNING   | 该常量表示错误级别为警告               |
| E_PARSE     | 该常量表示错误级别为语法解析错误       |
| E_NOTICE    | 该常量表示错误级别为通知提醒           |

```php
<?php
//预定义常量
echo '当前文件路径为:',__FILE__;
echo '<br>';
echo '当前PHP版本信息为：',PHP_VERSION;
echo '<br>';
echo '当前操作系统为：',PHP_OS;
```

变量

概念：变量就是保存可变数据的容器。
组成：在PHP中，变量是由$符号和变量名组成的。
规则：变量名的命名规则与标识符相同。
举例：如$number、$_it为合法的变量名，而$123、$*math为非法变量名。

变量的赋值

传值赋值

```php
<?php //传值赋值
$number=10; // =名字赋值号（不是等号），作用是将右侧的值传递给左边的变量
$result=$number;  //$number为10，$result=10
$number=100; //$number为100
echo '$number=',$number;
echo '<br>';
echo '$result=',$result;
```

引用赋值

```php
<?php //引用赋值
$number=10; // =名字赋值号（不是等号），作用是将右侧的值传递给左边的变量
$result=&$number;  //&是引用赋值，$number为10，$result为100
$number=100; //$number为100
echo '$number=',$number;
echo '<br>';
echo '$result=',$result;
```

可变变量

概念：可以将另外一个变量的值作为该变量的名称。

```php
<?php //可变变量
$a='say'; //可以将另外一个变量的值作为该变量的名称
$say='hello';
$hello='Lucy';

//echo $a,$say,$hello;
echo $a,' ',$$a,' ',$$$a;
```



表达式

概念：在PHP中，任何有值的内容都可以理解为表达式。



数据类型

- 标量数据类型
  - bool(布尔型)
  - int(整型)
  - float(浮点型)
  - string(字符串型)
- 复合数据数组
  - array（数组）
  - object(对象)
- 特殊数据类型
  - resoure(资源)
  - NULL(空值)



布尔型

表示事物的“真”和“假”，并且不区分大小写。 



整型

整型可以由十进制、八进制和十六进制数指定，用来表示整数

- 在它前面加上“-”符号，可以表示负数。
- 八进制数使用0~7表示，且数字前必须加上0
- 十六进制数使用0~9与A~F表示，数字前必须加上0x



浮点型

概念：浮点数是程序中表示小数的一种方法。通常使用标准格式和科学计数法格式表示。



字符串型

字符串是由连续的字母、数字或字符组成的字符序列。

分别为单引号、双引号、heredoc语法结构和nowdoc 语法结构。

```php
<?php
$number=100;
echo '$number=',$number; // $number=100 单引号，原样输出
echo '<br>';

echo "$number=",$number; //100=100 双引号，类似代替的功能
echo '<br>';

echo ' \' '; //转义字符
echo '<br>';

$str='方向的';
echo "PHP{$str}程序员";
```



```php
<?php
$name = 'PHP';
$heredoc = <<<EOD
<ul>
  <li>$name 是世界上最好的语言！</li>
  <li>$name is the best programming language in the world !</li>
</ul>
EOD;
echo $heredoc;

$nowdoc = <<<'EOD'
<ul>
  <li>$name 是世界上最好的语言！</li>
  <li>$name is the best programming language in the world !</li>
</ul>
EOD;
echo $nowdoc;
?>

```



数据类型检测

PHP中变量的数据类型通常不是开发人员设定的，而是根据该变量使用的上下文在运行时决定的。



数据类型转换

自动转换和强制转换



运算符及优先级

运算符，专门用于告诉程序执行特定运算或逻辑操作的符号

算术运算符

| **运算符** | **运算**                 | **范例** | **结果** |
| ---------- | ------------------------ | -------- | -------- |
| +          | 加                       | 5+5      | 10       |
| -          | 减                       | 6-4      | 2        |
| *          | 乘                       | 3*4      | 12       |
| /          | 除                       | 3/2      | 1.5      |
| %          | 取模（即算术中的求余数） | 5%7      | 5        |
| **         | 幂运算（PHP5.6新增）     | 3**4     | 81       |

字符串运算符

```php
<?php
//字符串运算符
$str='lu';
$html = 'Welcome to ' . $str . ' PHP';
echo $html;
```

赋值运算符

| **运算符** | **运算**     | **范例**            | **结果**     |
| ---------- | ------------ | ------------------- | ------------ |
| =          | 赋值         | $a=3;$b=2;          | $a=3;$b=2;   |
| +=         | 加并赋值     | $a=3;$b=2;$a+=$b;   | $a=5;$b=2;   |
| -=         | 减并赋值     | $a=3;$b=2;$a-=$b;   | $a=1;$b=2;   |
| *=         | 乘并赋值     | $a=3;$b=2;$a*=$b;   | $a=6;$b=2;   |
| /=         | 除并赋值     | $a=3;$b=2;$a/=$b;   | $a=1.5;$b=2; |
| %=         | 模并赋值     | $a=3;$b=2;$a%=$b;   | $a=1;$b=2;   |
| .=         | 连接并赋值   | $a='abc';$a.='def'; | $a='abcdef'; |
| **=        | 幂运算并赋值 | $a=2;  $a**= 5;     | $a=32;       |



```php
<?php
//赋值运算符
$a=3;
$b=2;
$a+=$b; //$a=$a+$b;
echo 'a='.$a;

$a-=$b; //$a=$a-$b;
echo 'a='.$a;

```

比较运算符

| **运算符** | **运算**   | **范例**   | **结果** |
| ---------- | ---------- | ---------- | -------- |
| ==         | 等于       | $x  == 4   | false    |
| !=         | 不等于     | $x  != 4   | true     |
| <>         | 不等于     | $x  <> 4   | true     |
| ===        | 全等       | $x  === 5  | true     |
| !==        | 不全等     | $x  !=='5' | true     |
| >          | 大于       | $x  > 5    | false    |
| >=         | 大于或等于 | $x  >= 5   | true     |
| <          | 小于       | $x  < 5    | false    |
| <=         | 小于或等于 | $x  <= 5   | true     |

逻辑运算符

| **运算符** | **运算** | **范例**    | **结果**                                                     |
| ---------- | -------- | ----------- | ------------------------------------------------------------ |
| &&         | 与       | $a  && $b   | $a和$b都为true，结果为true，否则为false                      |
| \|\|       | 或       | $a  \|\| $b | $a和$b中至少有一个为true，则结果为true，否则为false          |
| !          | 非       | !  $a       | 若$a为false，结果为true，否则相反                            |
| xor        | 异或     | $a  xor  $b | $a和$b的值一个为true，一个为false时，结果为true，否则为false |
| and        | 与       | $a  and $b  | 与&&相同，但优先级较低                                       |
| or         | 或       | $a  or $b   | 与\|\|相同，但优先级较低                                     |

```
1 && 1=1,1 && 0 =0,0 && 1=1,0 && 0=0
1 || 1=1, 1 || 0=1,0 || 1=0,0 || 0=0
!1=0,!0=1
1 xor 1=0,1 xor 0=1
```

递增递减运算符

| **运算符** | **运算**   | **范例**      | **结果**   |
| ---------- | ---------- | ------------- | ---------- |
| ++         | 自增（前） | $a=2;$b=++$a; | $a=3;$b=3; |
| ++         | 自增（后） | $a=2;$b=$a++; | $a=3;$b=2; |
| --         | 自减（前） | $a=2;$b=--$a; | $a=1;$b=1; |
| --         | 自减（后） | $a=2;$b=$a--; | $a=1;$b=2; |

位运算符

| **运算符** | **运算** | **范例**  | **结果**                                |
| ---------- | -------- | --------- | --------------------------------------- |
| &          | 按位与   | $a  & $b  | $a和$b每一位进行“与”操作后的结果        |
| \|         | 按位或   | $a  \| $b | $a和$b每一位进行“或”操作后的结果        |
| ~          | 按位非   | ~  $a     | $a的每一位进行“非”操作后的结果          |
| ^          | 按位异或 | $a  ^ $b  | $a和$b每一位进行“异或”操作后的结果      |
| <<         | 左移     | $a  << $b | 将$a左移$b次（每一次移动都表示“乘以2”） |
| >>         | 右移     | $a  >> $b | 将$a右移$b次（每一次移动都表示“除以2”） |

   101100011

& 110011001

​    100000001 



   101100011

| 110011001

​    111111011



~ 101100011

​    010011100



   101100011

^ 110011001

​    011111010



   << 101100011  (3)

​        100011000



右移 101100011 （3）

​         000101100

运算符优先级

| **结合方向** | **运算符**                                               |
| ------------ | -------------------------------------------------------- |
| 无           | new     （最高）                                         |
| 左           | [                                                        |
| 右           | ++ --   ~  (int) (float)   (string) (array) (object)   @ |
| 无           | Instanceof                                               |
| 右           | !                                                        |
| 左           | *   / %                                                  |
| 左           | +   - .                                                  |
| 左           | << >>                                                    |
| 无           | == !=   === !== <>                                       |
| 左           | &                                                        |

| **结合方向** | **运算符**                                    |
| ------------ | --------------------------------------------- |
| 左           | ^                                             |
| 左           | \|                                            |
| 左           | &&                                            |
| 左           | \|\|                                          |
| 左           | ? :                                           |
| 右           | = +=   -= *= /=   .= %= &=   \|= ^= <<=   >>= |
| 左           | and                                           |
| 左           | Xor                                           |
| 左           | Or                                            |
| 左           | ,  （最低）                                   |



###  2.3 流程控制语句

选择结构语句

概念：选择结构语句指的就需要对一些条件作出判断，从而决定执行指定的代码

if单分支语句

举例：只有年龄大于等于18周岁，才输出已成年，否则无输出

```php
<?php
//举例：只有年龄大于等于18周岁，才输出已成年，否则无输出
$age=17;

if($age>=18){
    echo '成年';
}
```



if…else语句

```php
<?php

//举例：判断一个学生的年龄，大于等于18岁则是成年人，否则是未成年人。

if($age>=18){
    echo '已成年';
}else{
    echo '未成年';
}

```

三元运算符：又称为三目运算符，它也可以完成if…else语句的功能。



if...elseif...else语句

概念：if…elseif…else语句也称为多分支语句，用于针对不同情况进行不同的处理

```php
<?php
//举例：对一个学生的考试成绩进行等级的划分，若分数在90~100分为优秀，
//分数在80~90分为优秀为良好，分数在70~80分为中等，
//分数在60~70分为及格，分数小于60则为不及格。

$score=82;
if($score>=90){
    echo '优秀';
}elseif($score>=80){
    echo '良好';
}elseif($score>=70){
    echo '中等';
}elseif($score>=60){
    echo '及格';
}else{
    echo '不及格';
}
```

switch语句

概念：switch语句也是多分支语句，功能与if系列条件语句相同，不同的是它只能针对某个表达式的值作出判断，从而决定执行哪一段代码

循环结构语句

概念：就是可以实现一段代码的重复执行

举例：设计一个跑五圈的代码

```php
<?php
//跑五圈
$i=1;
echo '今天的跑步目标是五圈：','<br>';
while($i<=5){ //完成第五圈后结束跑步
    echo "第{$i}圈 ";
    ++$i;
}
```

举例：求0-4的和 0+1 +2 +3 +4

```php
<?php
//求0-4的和 0+1 +2 +3 +4
$i = $sum = 0;      // 初始化变量
while ($i < 5) {    // 循环条件
    echo ' $i=' . $i;
    $sum += $i;
    ++$i;           // 设置循环出口
}
echo '<br> $sum=' . $sum;
```

do…while循环语句

唯一的区别在于，while是先判断条件后执行循环体，而do...while会无条件执行一次循环体后再判断条件。

```php
<?php
$i=-2;
do{
    echo '$i='.$i;
    ++$i;
}while($i>=0);
//唯一的区别在于，while是先判断条件后执行循环体，
//而do...while会无条件执行一次循环体后再判断条件。
```

for循环语句

举例：分别用while和for 语句输出四个*号。

```php
<?php
//while
$i=0;
while($i<4){
    echo '*';
    ++$i;
}

echo '<br>';

for($j=0;$j<4;++$j){
    echo '*';
}
```

举例：使用for循环打印1-100的偶数和

```php
<?php
for ($i = 1, $sum = 0; $i <= 100; ++$i) {
    if ($i % 2 == 0) { //利用求余数来判断偶数
        $sum += $i;
    }
}
echo '1~100之间的偶数和：' . $sum;
```

break语句

break语句可应用在switch和循环语句中，其作用是终止当前语句的执行，跳出switch选择结构或循环语句，执行后面的代码

动手实践

具体功能的实现要求如下所示。

- 生成x行和y列的表格
- 生成标题行格
- 隔行变色，为除标题行外的其他普通单元格设置隔行变色。
- 九九乘法表：根据表格生成器的设计思想完成九九乘法表。

```php+HTML
<!doctype html>
<html>
<head>
<title>x行y列的表格</title>
<style>
  table{border:2px solid #CFCFCF;width:500px;border-collapse:collapse;}
  td,th{border:2px solid #CFCFCF;}
  th{background:grey}  /*标题栏颜色*/
  th,tr{height:40px;}
  .white{background:#FFF;}
  .gray{background:#EEE;}
  .title{background:#7D8BA5;}
</style>
</head>
<body>
<?php
// 自定义行和列的数值
$row = 5;
$col = 10;
echo '<table>';

// 生成表格标题行
echo '<tr>';
for ($i = 1; $i <= $col; ++$i) {
    echo '<th></th>';
}
echo '</tr>';

for ($i = 1; $i <= $row; ++$i) {        // 控制表格的行
    //echo '<tr>';
	
	$color = ($i % 2 == 0) ? 'gray' : 'white';
	echo '<tr class="' . $color . '">';
	
    for ($j = 1; $j <= $col; ++$j) {    // 控制表格的列
        echo '<td></td>';
    }
    echo '</tr>';
}
echo '</table>';
?>
</body>
</html>
```

九九乘法表

```php+HTML
<!doctype html>
<html>
<head>
<title>九九乘法表</title>
<style>
  table{border:2px solid #CFCFCF;width:500px;border-collapse:collapse;}
  td,th{border:2px solid #CFCFCF;}
  th{height:40px;}
  .white{background:#FFF;}
  .gray{background:#EEE;}
  .title{background:#7D8BA5;}
</style>
</head>
<body>
<?php
echo '<table>';
for ($i = 1; $i <= 9; ++$i) {       // 九九乘法表的层数
    echo '<tr>';
    for ($j = 1; $j <= $i; ++$j) {  // 单元格个数
        //echo '<td></td>';
        echo "<td>{$j}×{$i}=" . $j * $i . '</td>';
    }
    echo '</tr>';
}
echo '</table>';
?>
</body>
</html>
```



### 实验手册2：国际象棋棋盘

```php+HTML
<?php
    $row = 10;    // 行数
    $col = 10;    // 列数
?>
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>国际象棋棋盘</title>
    <style>
      table{border:1px solid #000;border-collapse:collapse}
      td{width:20px;height:20px}
      .black{background:#000}
    </style>
  </head>
  <body>
    <table>
    <?php
        for ($i = 0; $i < $row; ++$i) { // 行数
            echo '<tr>';
            for ($j = 0; $j < $col; ++$j) { // 列数
                if (($i + $j) % 2) { // if (($i + $j) % 2!=0)
                    echo '<td></td>';//不等0
                } else {
                    echo '<td class="black"></td>'; //等于0
                }
            }
            echo '</tr>';
        }
    ?>
    </table>
  </body>
</html>
```



## 第3章 函数

### 3.1 函数的定义与调用

#### 初识函数

函数：封装一段用于完成特定功能的代码
当使用一个函数时，只需关心函数的参数和返回值，就可以完成一个特定的功能

内置函数

```php
$str = 'ABcd';
$upper = strtoupper($str);		// 调用strtoupper()函数将$str转换成大写
$lower = strtolower($str);		// 调用strtolower()函数将$str转换成小写
echo $upper;			// 输出结果：ABCD
echo $lower;			// 输出结果：abcd

```

自定义函数

```php+HTML
<!doctype html>
<html>
<head>
    <title>自定义函数</title>
    <style>
        table{border:2px solid #CFCFCF;width:500px;border-collapse:collapse;}
        td,th{border:2px solid #CFCFCF;}
        th,td{height:40px;}
    </style>
</head>
<body>
<?php

function generate_table($row, $col) //自定义函数
{
    $html = '<table>';
    for ($i = 1; $i <= $row; ++$i) {
        $html .= '<tr>';
        for ($j = 1; $j <= $col; ++$j) {
            $html .= '<td></td>';
        }
        $html .= '</tr>';
    }
    return $html.'</table>';
}
echo generate_table(4, 8);
echo '<br>';
echo generate_table(10,10);


?>
</body>
</html>
```



函数的定义由以下4部分组成：

- 关键字function
- 函数名
- 参数
- 函数体
- 返回值

```php
function 函数名([参数1, 参数2, ……])
{
    函数体……
}

```



#### 参数设置

- 无参函数

```php
<?php
function hello(){ //无参数 ，函数定义
    echo 'hello world!';
}

hello(); //函数调用

```

- 按值传递

```php
//按值传递
function add($a,$b){ //有参数
    $a=$a+$b;
    return $a;
}

echo add(4,5);
echo '<br>';
$x=3;
$y=4;
echo add($x,$y);
```

- 引用传参

```php
//引用传参
function extra(&$str){
    $str.=' and some extra ';
}
$var='food';
extra($var);
echo $var;
```
- 设置参数的默认值

```php
function say($p,$con='你真帅！'){
    return "$p $con";
}
echo say('小明');
echo say('小王','你好漂亮!');
```

- 指定参数类型

```php
//指定参数类型
function sum1(int $a,int $b){ // 这种方式支持php7.0以上
    return $a+$b;
}
echo sum1(4.4,5.5);
//输出结果：9
```

#### 变量的作用域

思考：变量在定义后就可以在函数中使用嘛？
答案：默认情况下，函数中可以，函数外不可以。
解析：变量只有在其作用范围内才可以被使用，这个作用范围称为变量的作用域。

- 在函数中定义的变量称为局部变量
- 在函数外定义的变量称为全局变量

```php
<?php
function test(){
    global $sum; //global是全局变量
    $sum=36;
    return $sum;
}
$sum=0;
echo test();
echo '<br>'.$sum;
```



```php
<?php
function test()
{
    // 方式一：利用global关键字取得全局变量
    global $var;
    echo '全局变量$var：' . $var.'<br>';
    // 方式二：利用$GLOBALS['变量名']访问
    echo '全局变量$str：' . $GLOBALS['str'];
}
$var = 100;     // 定义变量$var
$str = 'php';   // 定义变量$str
test();
```

补充案例：案例3-4函数中变量的作用域

```php+HTML
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>函数中变量的作用域</title>
    <style>
      h1{font-size:18px;text-align:center}
      .box{width:350px;border:2px dotted #FE0D0B;padding:0 10px 10px 10px;margin:20px auto}
    </style>
  </head>
  <body>
    <div class="box">
    <h1>函数中变量的作用域</h1>
    <?php
        function getArea()
        {
            global $radius;
            // $radius = $GLOBALS['radius'];
            $area = round(pi() * pow($radius, 2), 2); //round(x,2)小数点后面保留两位，pi()是3.1415，pow（）求幂运算
            return $area;
        }
        $radius = 4;    // 圆的半径
        echo '圆的面积：' . getArea();
        
    ?>
    </div>
  </body>
</html>
```





### 3.2函数嵌套（递归）调用

嵌套调用

指的是在调用一个函数的过程中，调用另外一个函数，这种在函数内调用其他函数的方式称为嵌套调用。

举例：班主任老师要计算每个学生语文和数学平均分，其实现思路是首先编写一个函数用于计算学生的语文和数学的总分，然后再编写一个函数用于实现学生的平均分。

```php
<?php
function sum($sub1, $sub2) 
{
    return $sub1 + $sub2;
}
function avg($sub1, $sub2) 
{
    $sum = sum($sub1, $sub2);
    return $sum / 2;
}
echo avg(78.9, 56);     // 学生A语文和数学的平均分：67.45
echo avg(92, 90);       // 学生B语文和数学的平均分：91
```





递归调用

递归调用：是函数嵌套调用中一种特殊的调用。它指的是一个函数在其函数体内调用自身的过程，这种函数成为递归函数。

举例：求n的阶乘，计算公式为1×2×3×…×n。如4的阶乘等于1×2×3×4=24。

```php
<?php
function factorial($n)
{
    if ($n == 1)
        return 1;
    return $n * factorial($n - 1);
}
echo factorial(4);
```



### 3.3 函数的高级应用

- 静态变量

思考：如何轻松得到一个函数被访问的次数？
答案：一是在函数中使用全局变量记录，缺点是全局变量可随时在函数外被改变，不能准确的记录；二是在函数中使用静态变量。

```php
<?php
//方法1 使用静态变量求函数的访问次数。
function num(){
    //$i=1; //局部变量，每次调用完后其值就会被释放掉
    static $i=1; //静态变量，每次调用完后其值就会被保存起来
    echo $i;
    ++$i;
}

echo '第一次调用：',num(),'<br>';
echo '第二次调用：',num(),'<br>';
echo '第三次调用：',num(),'<br>';

//方法2 使用全局变量求函数的访问次数。
function num1(){
    global $i; //全局变量
    echo $i;
    ++$i;
}
$i=1;
echo '第一次调用：',num1(),'<br>';
echo '第二次调用：',num1(),'<br>';
echo '第三次调用：',num1();
```

- 可变函数

可变函数：可变变量，它的实现是在一个变量前添加一个“$”符号，就变成了另外一个变量。同理，可变函数的实现就是在一个变量名后添加一对圆括号“()”，让其变成一个函数的形式，然后PHP就寻找与变量值同名的函数，并且尝试执行它。

```php
<?php
function shout(){
    echo '你好';
}

$fun='shout';//可以把函数的名称当成变量的值
echo $fun();//可变函数
```

- 回调函数

回调函数（callback）：指的就是具有callable类型的函数，一般用作参数的传递。如PHP内置函数call_user_func()可以接受用户自定义的回调函数作为参数。

```php
<?php
function sum($a,$b){
    return $a+$b;
}
call_user_func('sum',4,5);//回调函数，可以把函数当成参数
```

- 匿名函数

就是没有函数名称的函数，也称作闭包函数，经常用作回调函数参数的值。对于临时定义的函数，使用匿名函数无需考虑函数命名冲突的问题。

```php
<?php
function sum($a,$b){
    return $a+$b;
}
call_user_func('sum',4,5);//回调函数，可以把函数当成参数
```



```php
<?php
$c=100; //外部变量
$sum=function($a,$b) use($c){//匿名函数，使用use关键字，访问外部变量
    return $a+$b+$c;
};
echo $sum(100,200);
```

匿名函数和回调函数一起使用

```php
<?php
function calculate($a,$b,$func){ //匿名函数
    return $func($a,$b);
}

echo calculate(100,200,function($a,$b){//回调函数
    return $a+$b;
});


//$func=function($a,$b){
//    return $a+$b
//};
```

### 3.4 PHP的内置函数

字符串函数

- 字符串函数——截取给定路径中的字符串

```php
<?php
$url = 'C:\web\apache2.4\htdocs\cat.jpg';
$pos=strrpos($url,'\\');//转义字符，求最后一次出现的位置

echo $pos,'<br>';
echo substr($url,$pos+1),'<br>';
echo substr($url,0,23),'<br>';//substr(字符串，起始位置，长度)；
//作业：要求截取htdocs
echo substr($url,17,6);

```

- 字符串函数——替换指定位数的字符

```php
$tel='18810881888';
$len=4;
$replace=str_repeat('*',$len);
echo substr_replace($tel,$replace,3,$len);
```


- 字符串函数——过滤字符串中的空白字符

```php
$str='    今天 天气 真好！    ';
echo '原字符串:'.$str.'<br>';
echo '去空白后的字符串:'.trim($str);
```

- 字符串函数——字符串的比较

```php
if(strcmp('ye_PHP','yePHP')){
    echo '不成立';
}else
    echo '成立';
```

- 字符串函数——获取字符串的长度

```php
$str1='abcd';
$str2='php程序设计基础教程';
echo strlen($str1),'<br>';
echo strlen($str2),'<br>';//一个中文当前三个英文字符
echo mb_strlen($str2,'UTF-8');
```

数学函数

```php
<?php
echo ceil(5.2),'<br>';//向上取最接近的整数

echo floor(4.2),'<br>'; //向下取最接近的整数

echo rand(1,36),'<br>'; //生成随机整数

echo pi(),'<br>';//取圆周率的值

echo max(3,2);
```

时间函数

概念：Unix时间戳（Unix timestamp）定义了从格林威治时间1970年01月01日00时00分00秒起至现在的总秒数，以32位二进制数表示。
Unix纪元：1970年01月01日零点也叫作Unix纪元。



### 动手实践

```php+HTML
<!doctype html>
<html>
<head>
<title>制作年历</title>
<style>
  body{text-align:center;}
  .box{margin:0 auto;width:880px;}
  .title{background:#ccc;}
  table{height:200px;width:200px;font-size:12px;text-align:center;float:left;margin:10px;font-family:arial;}
</style>
</head>
<body>
<?php
function calendar($y)// 1.定义年历生成函数
{
    // 3.获取指定年份1月1日的星期数值
    $w = date('w', strtotime("$y-1-1"));

    $html = '<div class="box">';

    // 2.拼接每个月份的表格
    for ($m = 1; $m <= 12; ++$m) {
        $html .= '<table>';
        $html .= '<tr class="title"><th colspan="7">' . $y . ' 年 ' . $m . ' 月</th></tr>';
        $html .= '<tr><td>日</td><td>一</td><td>二</td><td>三</td><td>四</td><td>五</td><td>六</td></tr>';

        // 获取当前月份$m共有多少天
        $max = date('t', strtotime("$y-$m"));
        /*// 从该月份的第1天循环到最后1天
        for ($d = 1; $d <= $max; ++$d) {
            // 控制星期值在0~6范围内变动
            $w = ($w + 1 > 6) ? 0 : $w + 1;
        }
        */

        $html .= '<tr>';                        // 开始<tr>标签
        for ($d = 1; $d <= $max; ++$d) {
            if ($w && $d == 1) {                // 如果该月的第1天不是星期日，则填充空白
                $html .= "<td colspan=\"$w\"> </td>";
            }
            $html .= "<td>$d</td>";
            if ($w == 6 && $d != $max) {        // 如果星期六不是该月的最后一天，则换行
                $html .= '</tr><tr>';
            } elseif ($d == $max) {             // 该月的最后一天，闭合<tr>标签
                $html .= '</tr>';
            }
            $w = ($w + 1 > 6) ? 0 : $w + 1;
        }

        $html .= '</table>';
    }
    $html .= '</div>';
    return $html;
}
echo calendar('2021');
?>
</body>
</html>
```



### 实验手册 1：利用PHP实现在一段文本中查找关键字，将找到的关键字的字体设置为红色加粗。

```
<?php
$text = 'PHP（外文名:PHP: Hypertext Preprocessor，中文名：“超文本预处理器”）是一种通用开源脚本语言。语法吸收了C语言、Java和Perl的特点，利于学习，使用广泛，主要适用于Web开发领域。PHP 独特的语法混合了C、Java、Perl以及PHP自创的语法。它可以比CGI或者Perl更快速地执行动态网页。用PHP做出的动态页面与其他的编程语言相比，PHP是将程序嵌入到HTML（标准通用标记语言下的一个应用）文档中去执行，执行效率比完全生成HTML标记的CGI要高许多；PHP还可以执行编译后代码，编译可以达到加密和优化代码运行，使代码运行更快。';
$keyword = '语言';
$html = "<strong style=\"color:red;\">$keyword</strong>";
echo str_replace($keyword, $html, $text);
```

