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



## 第4章 数组

### 4.1 初识数组

思考：如何保存一个班级的所有学生、一个公司的全部员工等的相关信息
回答：一种方法，利用前面学习过的知识，则每一条信息都需要一个变量去保存，缺点是这样做很麻烦，而且容易出错，又不合理；另一种方法就是利用数组。
概念：数组就是一个可以存储一组或一系列数值的变量。

数组构成：数组是由一个或多个数组元素组成的
数组元素：一每个数组元素由键（Key）和值（Value）构成
键：“键”为元素的识别名称，也被称为数组下标
值： “值”为元素的内容
映射： “键”和“值”之间存在一种对应关系，称之为映射
类型划分：根据键的数据类型，可以将数组划分为索引数组和关联数组

索引数组是指键名为整数的数组。默认情况下，索引数组的键名是从0开始，并依次递增。它主要适用于利用位置（0、1、2……）来标识数组元素的情况。另外，索引数组的键名也可以自己指定。

关联数组是指键名为字符串的数组。通常情况下，关联数组元素的“键”和“值”之间有一定的业务逻辑关系。因此，通常使用关联数组存储一系列具有逻辑关系的变量。关联数组的“键”都是字符串，并与“值”之间具有一一对应的关系。

### 4.2 数组的基本使用

1.定义数组

```php
<?php
//第一种方式 array()方式
//定义索引数组
$fruits=array('a','b','cd',10); //省略键名，默认键名从0开始
$sports=array(2=>'d',4=>'e');//指定键名
echo '<pre>';
print_r($fruits);
var_dump($fruits);
//print_r($sports);
echo '</pre>';

//关联数组
$info=array('id'=>20,'name'=>'tom','tel'=>123456);
echo '<pre>';
var_dump($info);
echo '</pre>';

//混合数组
$temp=array();
$mixed=array(2,'str','id'=>5,5=>'b','a');//混合数组
echo '<pre>';
var_dump($mixed);
echo '</pre>';

//定义多维数组
$data=array(
    0=>array('id'=>01,'name'=>'tom'),
    1=>array('id'=>02,'name'=>'jimmy')
);
echo '<pre>';
var_dump($data);
echo '</pre>';

//第二种方式 赋值方式
$arr[]= 123;
$arr[]='abcd';
$arr[4]='php';
$arr['id']=5;

echo '<pre>';
var_dump($arr);
echo '</pre>';

//第三种方式 短数组方式

$w=[1,2,3,'a','b']; //索引数组
$o=['id'=>12,'name'=>'php']; //关联数组
$n=[[1,3],[2,4]]; //多维数组

echo '<pre>';
var_dump($w);
var_dump($o);
var_dump($n);
echo '</pre>';
```

2.访问数组

数组定义完成后，若想要查看数组中某个具体的元素，则可以通过“数组名[键]”的方式获取。

```php
<?php
//访问数组(引用数组)
$sub=['a','b','c',1,2];
echo $sub[2];//$sub[键名]

$data=['id'=>10,'name'=>'tom'];
echo '<br>',$data['name'];
```

3.遍历数组

```php
<?php
//遍历数组

$info=['id'=>1,'name'=>'tom','age'=>18];

foreach($info as $k=>$v){
    echo $k . ': ' . $v . ' ';
}

echo '<br>';

foreach ($info as $v) {
    echo $v . ' ';
}

//引用赋值
$arr=[1,2,3];
foreach($arr as &$v){
    $v=$v+2;
    //echo $v . ' ';
}
print_r($arr);
```

数组的删除

```ph[
<?php
$data = [//多维数组
    1 => ['name' => 'Tom', 'hobby' => 'swimming'],
    2 => ['name' => 'Lucy', 'hobby' => 'sing'],
    3 => ['name' => 'Jacie', 'hobby' => 'running'],
    4 => ['name' => 'Jimmy', 'hobby' => 'basketball']
];
unset($data[2]);    // 删除键名为2的数组元素
echo '<pre>';
print_r($data);
echo '</pre>';

// 删除数组
unset($data);
print_r($data);

```

5.数组操作符

```php
<?php
$num=[2,4];
$alp=['a','b','c'];
$m=$num+$alp; //+是联合的意思
echo '<pre>';
print_r($num);
print_r($alp);
print_r($m); //联合的功能，左边代替右边的值
echo '</pre>';
```

### 4.3 数组查找

**顺序查找法**是最简单的查找法，只需按照数组中元素的保存顺序，利用待查的值与数组中的元素从前往后一个一个的进行比较，直到找到目标值或查找失败。

```php
<?php
function search($arr, $find)//函数定义
{ 
    foreach ($arr as $k => $v) { //遍历数组
        if ($find == $v) {
            return "{$find}在数组中的键名为：$k";
        }
    }
    return '查找失败';
}
$arr = [55, 9, 7, 62];
echo search($arr, 7);     // 输出结果：7在数组中的键名为：2
echo search($arr, 10);    // 输出结果: 查找失败

```

二分查找法：针对有序数组的一种查找法，它的查询效率非常高。
实现原理：每次将查找值与数组中间位置元素的值进行比较，相等返回；不等则排除掉数组中一半的元素，然后根据比较结果大或小，再与数组中剩余一半中间位置元素的值进行比较，以此类推，直到找到目标值或查找失败。

```php
<?php
function bSearch($arr, $start, $len, $find)
{
    $end = $len - 1;
    $mid = round($len / 2);
    if ($start > $end) {
        return '查找失败';
    } elseif ($arr[$mid] > $find) {
        return bSearch($arr, $start, $mid - 1, $find);
    } elseif ($arr[$mid] < $find) {
        return bSearch($arr, $mid + 1, $end, $find);
    } else {
        return $mid;
    }
}
$arr = [1, 5, 9, 15, 28, 46, 98];   // 定义待查找数组
$len = count($arr);                 // 获取数组长度
echo bSearch($arr, 0, $len, 28);    // 输出结果：4
echo bSearch($arr, 0, $len, 10);    // 输出结果：查找失败

```

### 4.4 数组排序

- 冒泡排序

冒泡排序：是计算机科学领域中较简单的排序算法。
实现原理：按照要求从小到大排序或从大到小排序，不断比较数组中相邻两个元素的值，较小或较大的元素前移。冒泡排序比较的轮数是数组长度减1，每轮比较的对数等于数组的长度减当前的轮数。
缺点：冒泡排序的效率很低，在实际中使用较少。

```php
<?php
function bubble($arr)//自定义函数
{
    // 外层循环控制需要比较的轮数
    for ($i = 1, $len = count($arr); $i < $len; ++$i) {
        for ($j = 0; $j < $len - $i; ++$j) {    // 内层循环控制参与比较的元素
            if ($arr[$j] > $arr[$j + 1]) {      // 比较相邻的两个元素
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
            }
        }
    }
    return $arr;
}

$arr = [10, 2, 5, 27, 98, 31];
//echo count($arr);
// 输出结果：Array ( [0] => 2 [1] => 5 [2] => 10 [3] => 27 [4] => 31 [5] => 98 )
print_r(bubble($arr));

```

- 简单选择排序

快速排序：是对冒泡排序的一种优化。
实现原理：首先选择一个基准元素，通常选择待排序数组的第1个数组元素。通过一趟排序，将要排序的数组分成两个部分，其中一部分比基准元素小，另一部分比基准元素大，然后再利用同样的方法递归的排序划分出的两部分，直到将所有划分的数组排序完成。

```php
<?php
function selectSort($arr)
{
    for($i=0,$len=count($arr);$i<$len;++$i){
        $min=$i; //先假设我是最小的
        for($j=$i+1;$j<$len;++$j){
            if($arr[$j]<$arr[$min]){
                $min=$j; //确定我是最小的
            }
        }
        if($min!=$i){  //交换
            $temp=$arr[$i];
            $arr[$i]=$arr[$min];
            $arr[$min]=$temp;
        }
    }
    return $arr;
}

$arr = [9, 1, 2, 10, 4, 12];
// 输出结果：Array ( [0] => 1 [1] => 2 [2] => 4 [3] => 9 [4] => 10 [5] => 12 )
print_r(selectSort($arr));

```

- 快速排序

快速排序：是对冒泡排序的一种优化。
实现原理：首先选择一个基准元素，通常选择待排序数组的第1个数组元素。通过一趟排序，将要排序的数组分成两个部分，其中一部分比基准元素小，另一部分比基准元素大，然后再利用同样的方法递归的排序划分出的两部分，直到将所有划分的数组排序完成。

```php
<?php
function quickSort($arr)
{   //递归是函数调用自身，递归的终止
    // 获取待排序数组长度，当小于或等于1时直接返回数组（递归出口）
    $len = count($arr);
    if($len <= 1){ //小于或等于1时，递归出口
        return $arr;
    }
    // 设置基准元素（使用第1个元素）
    $pivot = $arr[0];
    $small = $big = [];
    // 根据基准元素，将数组分成2个部分：小于和大于
    for ($i = 1; $i < $len; ++$i) {
        if ($arr[$i] < $pivot) {         // 小于基准元素
            $small[] = $arr[$i];
        } else {                         // 大于等于基准元素
            $big[] = $arr[$i];
        }
    }
    //分别采用相同方案递归排序小于、大于部分的数组，然后进行合并
    return array_merge(quickSort($small), [$pivot], quickSort($big));
}
$arr = [31, 98, 5, 27, 2, 78];
// 输出结果：Array ( [0] => 2 [1] => 5 [2] => 27 [3] => 31 [4] => 78 [5] => 98 )
print_r(quickSort($arr));

```

- 插入排序

插入排序：也是冒泡排序的优化，是一种直观的简单排序算法。
实现原理：通过构建有序数组元素的存储，对未排序数组的元素，在已排序的数组中从最后一个元素向第一个元素遍历，找到相应位置并插入。其中，待排序数组的第1个元素会被看作是一个有序的数组，从第2个至最后一个元素会被看作是一个无序数组。

```php
<?php
function insertSort($arr)
{
    for ($i = 1, $len = count($arr); $i < $len; ++$i) {    // 遍历无序数组
        for ($j = $i; $j > 0; --$j) {         // 遍历有序数组
            if ($arr[$j] < $arr[$j - 1]) {    // 无序与有序进行比较
                $temp = $arr[$j];
                $arr[$j] = $arr[$j - 1];
                $arr[$j - 1] = $temp;
            }
        }
    }
    return $arr;
}
$arr = [98, 7, 65, 54, 12, 6];
// 输出结果：Array ( [0] => 6 [1] => 7 [2] => 12 [3] => 54 [4] => 65 [5] => 98 )
print_r(insertSort($arr));

```

### 4.5数组的常用函数

1. 指针操作函数

数组指针：用于指向数组中的某个元素，默认情况下，指向数组的第1个元素。通过移动或改变指针的位置，可以访问数组中的任意元素。

```php
<?php
$arr = ['a','b','c','d'];
echo key($arr).'--'.current($arr);
echo '<br>';
echo next($arr);
echo '<br>';
echo end($arr);
//var_dump($arr);

echo '<br>';
$s=['abc','def','hij'];
while(list($k,$v)=each($s)){
    $c=current($s);
    echo "{$k}=>{$v}-{$c}   ";
}
```

2. 数组元素操作函数

```php
<?php
$arr=['a','b','c'];
var_dump($arr);
echo '<br>';
array_pop($arr); //移出最后一个元素
var_dump($arr);
echo '<br>';
array_push($arr,'1');
var_dump($arr);
echo '<br>';
```

3. 排序函数

```php
<?php
$arr=['a','b','c','d',11,2,3];
print_r($arr);
asort($arr);
echo '<br>';
print_r($arr);
```



```
Array ( [0] => a [1] => b [2] => c [3] => d [4] => 11 [5] => 2 [6] => 3 )
Array ( [0] => a [1] => b [2] => c [3] => d [4] => 2 [5] => 3 [6] => 11 )
Array ( [0] => a [1] => b [2] => c [3] => d [5] => 2 [6] => 3 [4] => 11 )
```

4. 检索函数

数组中元素的查找

```php
<?php
$data=['a'=>1,'b'=>2,'c'=>3];
print_r($data);
var_dump(in_array(2,$data));
var_dump(in_array(5,$data));//检查数组中是否存在某个值
var_dump(array_search(2,$data));//在数组中搜索给定的值，如果成功则返回相应的键名
var_dump(array_key_exists('a',$data));//检查给定的键名是否存在于数组中

```

### 4.6数组在字符串与函数中的应用

1. 字符串与数组的转换

```php
<?php
var_dump(explode('n','banana'));//把字符串转换成数组
var_dump(explode('n','banana',2));
var_dump(explode('n','banana',-2));
echo '<br>';
echo implode('-',['a','b','c']);//把数组转换成字符串
echo '<br>';
echo implode(',',['a'=>1,'b'=>2,'c'=>'d']);
```

2. 函数可变参数列表

```php
<?php
function test(){
    echo func_num_args(),'<br>';//获取当前函数的参数个数
    foreach(func_get_args() as $v)//将参数列表以索引数组形式返回
    {
        echo $v . ' ';
    }
    echo '<br>',func_get_arg(1);//获取参数列表中的某一项
}

test('A','B','C','D','E','F');
```

### 实验手册：随机发牌

```php
<?php
// 建立数组保存的牌组池
$num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
$icon = ['♥' => 'red', '♦' => 'red', '♠' => 'black', '♣' => 'black'];
// 生成扑克牌组
$poker = [];
foreach ($icon as $k => $v) {
    foreach ($num as $vv) {
        $poker[] =  "<i style=\"color:$v;\">$vv $k</i>";
    }
}
// 打乱牌组顺序
shuffle($poker);
?>
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>随机发牌</title>
    <style>
      div{margin:15px 0}
      i{font-style:normal;border:1px solid #ccc;padding:6px 3px;margin-right:10px}
    </style>
  </head>
  <body>
    <div>玩家A 牌组</div>
    <?php for ($i = 0; $i < 10; ++$i) {
        echo current($poker);
        next($poker);
    } ?>
    <div>玩家B 牌组</div>
    <?php for ($i = 0; $i < 10; ++$i) {
        echo current($poker);
        next($poker);
    } ?>
    <div>玩家C 牌组</div>
    <?php for ($i = 0; $i < 10; ++$i) {
        echo current($poker);
        next($poker);
    } ?>
  </body>
</html>
```

## 第5 章 错误处理及调试

## 第6章 阶段案例-WEB表单

```php+HTML
<?php
require './generate.php';
//保存表单元素，多维数组
$elements = [
    [
        'attr' => ['type' => 'text', 'name' => 'user', 'size' => '25'],
        'tag' => 'input',
        'text' => '姓　　名：',
        
    ], [
        'tag' => 'input',
        'text' => '邮　　箱：',
        'attr' => ['type' => 'text', 'name' => 'email', 'size' => '25']
    ], [
        'text' => '手机号码：',
        'tag' => 'input',
        
        'attr' => ['type' => 'text', 'name' => 'tel', 'size' => '25']
    ], [
        'tag' => 'input',
        'text' => '性　　别：',
        'attr' => ['type' => 'radio', 'name' => 'gender'],
        'option' => ['m' => '男', 'w' => '女'],
        'default' => 'm'
    ], [
        'tag' => 'input',
        'text' => '爱　　好：',
        'attr' => ['type' => 'checkbox', 'name' => 'hobby[]'],
        'option' => ['swimming' => '游泳', 'reading' => '读书', 'running' => '跑步',],
        'default' => ''
    ], [
        'tag' => 'select',
        'text' => '住　　址：',
        'attr' => ['name' => 'area'],
        'option' => ['' => '--请选择--', 'BJ' => '北京', 'SH' => '上海', 'SZ' => '深圳',]
    ], [
        'tag' => 'textarea',
        'text' => '自我介绍：',
        'attr' => ['name' => 'declare', 'cols' => '50', 'rows' => '5']
    ], [
        'tag' => 'input',
        'attr' => ['type' => 'submit', 'value' => '提交']
    ]
];
// var_dump($_POST);
?>
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Web表单生成器</title>
    <style>
      body{margin-top:20px;}
      .box{font-family:Tahoma,simsun;font-size:12px;border:1px solid #1678BE;display:table;margin:0 auto;}
      .box-head{padding:5px 20px;background-color:#2487C9;color:#fff;font-size:14px;}
      .box-body{padding:10px 20px;}
      .box-body th{font-weight:normal;vertical-align:top;padding-top:5px;}
      .box-body td{padding-top:2px;padding-bottom:8px;}
      .box-body select{font-family:Tahoma,simsun;font-size:12px;padding:2px 5px;cursor:pointer;}
      .box-body label{margin-right:5px;cursor:pointer;}
      .box-body label input{cursor:pointer;}
      .box-body input{vertical-align:middle;font-family:Tahoma,simsun;font-size:12px;}
      .box-body input[type=text]{padding:2px;}
      .box-body input[type=radio]{margin-top:-1px;}
      .box-body input[type=submit]{padding:4px 15px;cursor:pointer;}
    </style>
  </head>
  <body>
    <!--输出定制表单-->
    <div class="box">
      <div class="box-head">个人信息</div>
      <div class="box-body">
        <form action="form.php" method="post" enctype="multipart/form-data">
          <?=generate($elements)?>
        </form>
      </div>
    </div>
  </body>
</html>
```



```php+HTML
<?php

// 生成表单的函数
function generate($elements)
{
    $items = '';
    $default = ['tag' => '', 'text'=>'', 'attr' => [], 'option' => [], 'default' => ''];
    foreach ($elements as $v) {
        $v = array_merge($default, $v);
        $v['attr'] = generate_attr($v['attr']);
        $generate = 'generate_' . array_shift($v);
        $items .= '<tr>' . call_user_func_array($generate, $v) . '</tr>';
    }
    return "<table>$items</table>";
}

// 拼接 表单元素的属性
function generate_attr($attr, $items = '')
{
    foreach ($attr as $k => $v) {
        $items .= " $k=\"$v\" ";
    }
    return $items;
}

function generate_input($text, $attr, $option, $default)
{
    if(empty($option)){
        $items = "<input $attr value=\"$default\">";
    } else {
        $items = '';
        foreach ($option as $k => $v) {
            $checked = in_array($k, (array)$default, true) ? 'checked' : '';
            $items .= "<label><input $checked $attr value=\"$k\">$v</label>";
        }
    }
    return "<th>$text</th><td>$items</td>";
}

// 拼接 文本域
function generate_textarea($text, $attr, $option, $default)
{
    $textarea = "<textarea $attr>$default</textarea>";
    return "<th>$text</th><td>$textarea</td>";
}

// 拼接 下拉列表
function generate_select($text, $attr, $option, $default)
{
    $items = '';
    foreach ($option as $k => $v) {
        $selected = ($default === $k) ? 'selected' : '';
        $items .= "<option $selected value=\"$k\">$v</option>";
    }
    $select = "<select $attr>$items</select>";
    return "<th>$text</th><td>$select</td>";
}

```

## 第7章 PHP与WEB页面交互

表单交互

```php+HTML
<?php
var_dump($_POST);
?>

<form method="post">
      用户名：<input type="text" name="username">
     密码:<input type="password" name="password">
    <input type="submit" value="登录">
</form>

```

URL交互

```php
<?php
$action = isset($_GET['action']) ? $_GET['action'] : '';
$num1 = isset($_GET['num1']) ? (float)$_GET['num1'] : 0;
$num2 = isset($_GET['num2']) ? (float)$_GET['num2'] : 0;
switch ($action) {
	case 'add':
		echo "$num1 + $num2 = ", $num1 + $num2;
		break;
	case 'sub':
		echo "$num1 - $num2 = ", $num1 - $num2;
		break;
	case 'mul':
		echo "$num1 * $num2 = ", $num1 * $num2;
		break;
	case 'div':
		echo "$num1 / $num2 = ", $num2 ? ($num1 / $num2) : '除数不能为0';
		break;
	default:
		echo '参数不正确';
}

// ① 计算 22 + 33 的结果
// 测试URL：http://localhost/calc.php?action=add&num1=22&num2=33
// ② 计算 33.2 - 22.1 的结果
// 测试URL：http://localhost/calc.php?action=sub&num1=33.2&num2=22.1
// ③ 计算 12 * 23 的结果
// 测试URL：http://localhost/calc.php?action=mul&num1=12&num2=23
// ④ 计算 50 / 25 的结果
// 测试URL：http://localhost/calc.php?action=div&num1=50&num2=25


```

数组交互

```php
<?php
print_r($_GET);
```

## 第八章 PHP操作MYSQL数据库

数据库管理

数据库的管理主要包括查看数据库、创建数据库、选择数据库和删除数据库

| **功能**   | **示例**                    | **描述**                            |
| ---------- | --------------------------- | ----------------------------------- |
| 查看数据库 | SHOW  DATABASES;            | 显示MySQL数据库服务器中已有的数据库 |
| 创建数据库 | CREATE  DATABASE `itheima`; | 创建一个名称为itheima的数据库       |
| 选择数据库 | USE  `itheima`;             | 选择数据库itheima进行操作           |
| 删除数据库 | DROP  DATABASE `itheima`;   | 删除数据库itheima                   |

```mysql
CREATE  DATABASE `itheima`; 
USE  `itheima`;  
```

创建数据表

数据表是数据库中最基本的数据对象，用于存放数据。
要选择数据库，确定是在哪个数据库中创建的数据表；
要根据项目需求创建数据表；
才能对数据表中的数据进行具体操作。

```mysql
CREATE TABLE IF NOT EXISTS `student` (
  `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT COMMENT '学号',
  `name` VARCHAR(32) NOT NULL COMMENT '姓名',
  `gender` ENUM('男', '女') DEFAULT '男' NOT NULL COMMENT '性别'
) DEFAULT CHARSET=utf8;

```

查看数据表

```mysql
SHOW TABLES;
```

添加记录

```mysql
 INSERT INTO `student` (`name`,`gender`) VALUES ('tom','男');
```

查看表中的记录

```mysql
SELECT * FROM student;
```

### 第9章 许愿墙

### 第10章 正则表达式

### 第11章 文件操作



### 期末复习

1.  歌唱比赛评分

PHP中提供了许多的数组函数，直接调用这些函数就可以很容易的实现数组的排序和查找等功能。接下来，利用数组函数实现对歌唱比赛的评分，现有10个评委对某选手的评分为：85, 92, 73, 96, 100, 89, 67, 81, 95, 88，评分规则如下：

-  节目规定最高分不能大于100分，最低分不能小于0分。

-  去掉一个最高分，去掉一个最低分，求总分和平均分（保留一位小数）。

```php+HTML
<?php
    // 分数数组
    $score = ['85', '92', '73', '96', '100', '89', '67', '81', '95', '88'];
    // 对数组进行升序排序
    sort($score);
    // 取出最小值
    $min = array_shift($score);
    // 取出最大值
    $max = array_pop($score);
    // 计算数组中元素的个数
    $num = count($score);
    // 计算数组中所有值的和
    $sum = array_sum($score);
    // 计算歌唱比赛的平均值
    $avg = round($sum / $num, 1);
?>
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>歌唱比赛评分</title>
    <style>
      .box{width:500px;height:358px;background:url('./images/back.jpg');margin:10px auto}
      .sing{border-spacing:2px;margin:0 auto;padding-top:130px;width:300px}
      .sing tr,td{border:solid #ccc 1px;padding:5px;text-align:center;background-color:#fff;opacity:0.9} 
    </style>
  </head>
  <body>
    <div class="box">
      <table class="sing">
        <tr>
          <td>最低分</td>
          <td><?php echo $min; ?></td>
        </tr>
        <tr>
          <td>最高分</td>
          <td><?php echo $max; ?></td>
        </tr>
        <tr>
          <td>总分</td>
          <td><?php echo $sum; ?></td>
        </tr>
        <tr>
          <td>平均分</td>
          <td><?php echo $avg; ?></td>
        </tr>
      </table>
    </div>
  </body>
</html>
```



2.  随机发牌

   扑克牌是一种家喻户晓的纸牌游戏。一副扑克牌有54张牌，其中52张是正牌，另2张是副牌（大王和小王）。52张正牌又均分为13张一组，并以黑桃、红桃、梅花、方块四种花色表示各组，每组花色的牌包括从1-10（1通常表示为A）以及J、Q、K标示的13张牌，玩法千变万化，多种玩法。

   ```php+HTML
   <?php
   // 建立数组保存的牌组池
   $num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
   $icon = ['♥' => 'red', '♦' => 'red', '♠' => 'black', '♣' => 'black'];
   // 生成扑克牌组
   $poker = [];
   foreach ($icon as $k => $v) {
       foreach ($num as $vv) {
           $poker[] =  "<i style=\"color:$v;\">$vv $k</i>";
       }
   }
   // 打乱牌组顺序
   shuffle($poker);
   ?>
   <!doctype html>
   <html>
     <head>
       <meta charset="UTF-8">
       <title>随机发牌</title>
       <style>
         div{margin:15px 0}
         i{font-style:normal;border:1px solid #ccc;padding:6px 3px;margin-right:10px}
       </style>
     </head>
     <body>
       <div>玩家A 牌组</div>
       <?php for ($i = 0; $i < 10; ++$i) {
           echo current($poker);
           next($poker);
       } ?>
       <div>玩家B 牌组</div>
       <?php for ($i = 0; $i < 10; ++$i) {
           echo current($poker);
           next($poker);
       } ?>
       <div>玩家C 牌组</div>
       <?php for ($i = 0; $i < 10; ++$i) {
           echo current($poker);
           next($poker);
       } ?>
     </body>
   </html>
   ```

   3.  生成颜色面板

      颜色面板是在计算机使用中经常用到的功能，如在画图软件中设置画笔颜色、填充颜色，在Word中设置文本颜色等。通过颜色面板可以直观地进行颜色选择。

      ```php+HTML
      <!doctype html>
      <html>
        <head>
          <meta charset="UTF-8">
          <title>生成颜色面板</title>
          <style>td{width:15px;height:15px}</style>
        </head>
        <body>
          <table>
            <tr>
            <?php
              $n = 1;
              $row = 36;
              for ($i = 0; $i <= 5; ++$i) {
                  for ($j = 0; $j <= 5; ++$j) {
                      for ($k = 0; $k <= 5; ++$k) {
                          $red = str_pad(dechex($i * 51), 2, '0', STR_PAD_LEFT);
                          $green = str_pad(dechex($j * 51), 2, '0', STR_PAD_LEFT);
                          $blue = str_pad(dechex($k * 51), 2, '0', STR_PAD_LEFT);
                          echo "<td style=\"background:#$red$green$blue;\"></td>";
                          echo $n++ % $row ? '' : '</tr><tr>';
                      }
                  }
              }
            ?>
            </tr>
          </table>
        </body>
      </html>
      ```


   4.  百钱白鸡

      公鸡5文钱1只，母鸡3文钱1只，小鸡1文钱买3只，现在用100文钱共买了100只鸡，问：在这100只鸡中，公鸡、母鸡和小鸡各是多少只？（设每种至少一只）

      ```php+HTML
      <?php
      /*// 用于保存结果
      $data = [];
      // 假设：100只鸡都为母鸡
      for ($mj = 1; $mj <= 100; ++$mj) {
          // 假设：100只鸡都为公鸡
          for ($gj = 1; $gj <= 100; ++$gj) {
              // 假设：100只鸡都为小鸡
              for ($xj = 1; $xj <= 100; ++$xj) {
                  // 根据条件依次进行判断
                  if (($gj + $mj + $xj == 100) && ( $gj* 5 + $mj * 3 + $xj / 3 == 100)) {
                      $data[] = [
                          'gj' => $gj,
                          'mj' => $mj,
                          'xj' => $xj
                      ];
                  }
              }
          }
      }*/
      // 方法二
      // 根据条件可得母鸡最多为33只
      for ($mj = 1; $mj <= 33; ++$mj) {
          // 根据条件可得公鸡最多为20只
          for ($gj = 1; $gj <= 20; ++$gj) {
              // 计算：小鸡 = 100 - 母鸡数量 - 公鸡数量
              $xj = 100 - $mj - $gj;
              // 根据钱数进行判断
              if ($gj * 5 + $mj * 3 + $xj / 3 == 100) {
                  $data[] = [
                      'gj' => $gj,
                      'mj' => $mj,
                      'xj' => $xj
                  ];
              }
          }
      }
      ?>
      <!doctype html>
      <html>
        <head>
          <meta charset="utf-8">
          <title>百钱白鸡</title>
          <style>
            .tbl{border-collapse:collapse;width:450px;text-align:center;margin:0 auto;border:1px solid #174464}
            .tbl tr:nth-child(1){font-weight:bold;background:#174464;color:#fff;height:30px; font-size:18px;}
          </style>
        </head>
        <body>
          <table class="tbl">
            <tr>
              <td>公鸡数量（个）</td>
              <td>母鸡数量（个）</td>
              <td>小鸡数量（个）</td>
            </tr>
            <?php foreach ($data as $v): ?>
              <tr>
                <td><img src="./images/gj.jpg"><?php echo $v['gj']; ?></td>
                <td><img src="./images/mj.jpg"><?php echo $v['mj']; ?></td>
                <td><img src="./images/xj.jpg"><?php echo $v['xj']; ?></td>
              </tr>
            <?php endforeach; ?>
          </table>
        </body>
      </html>
      ```

      

    

