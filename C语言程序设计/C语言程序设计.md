# C语言程序设计

[toc]



## 第一章 引言 

### 1.1 C语言的发展过程

### 1.2 C语言的特点



> 关键字：C语言在开发过程中保留下来的有特殊意义的单词。例如if,for,char,int等。



### 1.3 简单的C语言程序

**Dev-c++使用方法**

- 新建 ctrl+n
- 英文状态
- 保存 ctrl+s,保存类型为.c
- 运行 F11

```c
//编写程序的框架 1
#include <stdio.h> //导入标准输入输出头文件
void main(){
	printf("我的第一个程序。。。");//打印函数 
} 
```



```c
#include <stdio.h>
int main(){
	printf("Hello,World");
	return 0; 
}
```

程序说明：

- #include文件包含，（导入）
- 扩展名.h，头文件
- main()主函数，（必须有一个而且只能是一个）。因为C语言执行时是从主函数开始，从主函数结束
- printf("我的第一个程序。。。"); 输出函数，

```c
#include <stdio.h>
#include <math.h>
void main(){
	double x,s;
	printf("输入x：");
	scanf("%lf",&x);
	s=cos(x);
	printf("cos(%lf)=%lf",x,s);
}
```

程序说明：

- 两个头文件<stdio.h>标准输入输出库，<math.h>数学库
- double数据类型，双精度浮点型
- scanf("%lf",&x); 输入函数，%lf格式控制符，&取地址



```c
/* example1_3 两数相加的加法器*/
#include<stdio.h>
int add(int x, int y);
void main()
{ 
	int a, b, c;
	printf ("please input value of a and b:\n");
	scanf("%d %d", &a, &b);
	c=add(a,b);
	printf ("max=%d\n",c);
}
int add(int x, int y)
{
	return(x+y);
}
```

程序说明：

- 主函数体分为两部分：说明部分和执行部分。

- 语句c=add(a,b)；是通过调用加法器add()来完成a+b的计算，并将计算结果赋给变量c。

- 屏幕上显示字符串：“please input value of a and b:”是提示用户从键盘输入a和b的值，用户从键盘上键入两个数，屏幕上会显示出这两个数的和。

**编译和解释**

### 1.4 C语言程序的结构

通常，C语言程序可由下面几个部分组合而成：

1．文件包含部分；

2．预处理部分；

3．变量说明部分；

4．函数原型声明部分；

5．主函数部分；（必须有且仅有一个函数）

6．自定义函数部分。(0个或多个)

###  1.5 C语言程序的执行

编译器：

- 词法分析器
- 语法分析器
- 代码生成器



### **2.2** 基本数据类型及取值范围

5种基本数据类型：

- int整数型 1 2 3 11 
- char字符型 'a' 'b' 'c' '1' '2'
- float单精度实数型(单精度浮点型)
- double双精度浮点型
- void空类型(无返回值)

整数型的四种修饰：

- signed（有符号）  
- unsigned（无符号）
- long（长型）
- short（短型）

> C语言中的注释，有 //和/* */两种方式，编译器会忽略注释语句
>
> // 是单行注释     /* */ 是多行注释

### 2.3 标识符、变量和常量

#### 标识符

标识符是对变量名、函数名、标号和其他各种用户定义的对象命名。

标识符的**第1个字符必须是字母或下划线**，标识符的长度可以是一个或多个字符，最长不允许超过32个字符。`int a1,b1,1c;`

标识符区分大小写  `int a,A;`

标识符不能和C语言的关键字相同 `int INT;`

标识符不能和用户自定义的函数或C语言库函数同名 `int printf;`

#### 变量和常量

变量

其值可以改变的量称为变量

C 语言规定：变量在使用之前必须定义

变量定义的一般形式是：

​        <类型名> <变量列表>;

<类型名>必须是有效的C数据类型，如：int、char、float、double、void

<变量列表>可以由一个或多个由逗号分隔的多个标识符名构成。

常量

常量的值是不可变的

在C语言中，有整型常量、实型常量、字符常量、字符串常量、和枚举常量等。

- 整型常量

十进制 八进制 十六进制

- 实型常量

浮点表示法 `123.456000`  小数点后长度有6位，不足用0补

科学计数法 `1.234560E+004`

- 转义字条

\n 换行 \t 空格 \a 响铃

- 字符常量

在C语言中，字符是按其所对应的ASCII的值来存储的，一个字符占一个字节。

ASCII美国标准信息交换码

a-->97    A-->65

注意，字符常量可以和整型常量运算 '3'+3=54

- 符号常量

```c
#include <stdio.h>"
/*
符号常量，其值是不可以改变的 
C89 预处理命令 #define 
C99 const修饰符 
*/ 

//#define PI 3.1415926
const float PI=3.1415926;

main(){     
      printf("%f\n",PI);//在代码中遇到PI时用3.1415926，PI的值是不可以改变的 
}

```

### 2.4 基本运算符、表达式及运算的优先级

基本表达式的常用运算符有：

（1）算术运算符。

（2）关系运算符。

（3）逻辑运算符。

（4）赋值运算符。

另外，条件运算符、自反赋值运算符、逗号运算符、指针运算符、位运算符等均可构成基本表达式。

优先级：

**()>单目运算符(!)>算术运算符>关系运算符>逻辑运算符(不包括！)>条件运算符>赋值运算符>逗号运算符**

#### 2.4.1算术运算符

表达式是由操作数和操作符组成

操作数通常由变量或常量表示；

操作符由各种运算符表示

前置++/−−和后置++/−−

- ++<变量>; 先将变量的值加1，再使用变量
- <变量>++; 先使用变量，再将变量的值加1

```c
#include <stdio.h>
//后置++   =赋值号 
//<变量>++; 先使用（赋值）变量，再将变量的值加1。
//前置++ 
//++<变量>; ? 先将变量的值加1，再使用变量。
//不能用于常量 

main(){
	int a=1,b;
//	b=a--;
	b=--a;
	printf("a=%d，b=%d",a,b);	
}
```

#### 2.4.2关系运算符及关系表达式

`> >= < <=`  高

`== !=`  低

```c
#include<stdio.h>
main()
{  
	int a,b;
//	a=2+3>3+4;
	//优先级 
	b=((23-9) != (18-6));
	printf("%d",b); 

}

```



#### 2.4.3逻辑运算符及逻辑表达式

略

#### 2.4.4条件运算符

表达式1? 表达式2:表达式3;

条件表达式的语法规则：

 当表达式1的值为1（真）时，其结果为表达式2的值；

 当表达式1的值为0（假）时，其结果为表达式3的值。

```c
/*example2_15.c 了解三目运算符的语法规则*/
#include <stdio.h>
#include <stdlib.h>
void main()
{
	int a=3,b=5,c;
	c=(a>b)?(a+b):(a-b);
	/*
	表达式1?表达式2:表达式3;
    条件表达式的语法规则：
   当表达式1的值为1（真）时，其结果为表达式2的值；
   当表达式1的值为0（假）时，其结果为表达式3的值。
	*/ 
	printf("The max value of a and b is: %d\n",c);
	a=6;
	b=2;
	c=(a>b)?(a-b):(a+b);
	printf("The max value of a and b is: %d\n",c);
}
```

#### 2.4.5逗号表达式

逗号表达式可以扩充到具有*n*个表达式的情况：

 表达式1，表达式2，…，表达式*n*；

 整个逗号表达式的结果为表达式n的值。



#### 2.4.6赋值运算符

符号“=”为赋值运算符，作用是将赋值运算符右边的表达式的值赋给其左边的变量。 

#### 2.4.7数据类型转换

自动类型规则

1. 若参与运算量的类型不同，则先转换成同一类型，然后进行运算。 

2. 转换按数据长度增加的方向进行，以保证精度不降低。如int 型和long 型运算时，

   先把int量转成long型后再进行运算。

3. 所有的浮点运算都是以双精度进行的，即使仅含float单精度量运算的表达式，也要

   ​     先转换成double 型，再作运算。

4. char型和short型参与运算时，必须先转换成 int 型。

5. 在赋值运算中，两边的数据类型不同时，赋值号右边量的类型将转换为左边量的类型。

强制类型转换

(数据类型符)表达式; 



### **2.5** **标准输入** **/** 输出函数简介

#### 2.5.1 scanf函数

scanf(格式控制字符串，变量地址列表)

通过标准输入设备（键盘、写字板等），按照格式控制字符串中的格式要求为变量地址列表中的变量输入数据。

#### 2.5.2 printf函数

printf(格式控制字符串，输出列表)

将输出列表中的各个表达式的值按照格式控制字符串中对应的格式输出到标准输出设备（显示屏）

#### 2.5.3 getchar函数

从标准输入设备输入一个字符。

```c
#include <stdio.h>
main(){
	char ch;//定义一个字符变量 
	ch=getchar();//从键盘上获得一个字符 ，getchar()没有参数 
	printf("ch=%c",ch);//按字符格式输出 
}
```

#### 2.5.4 putchar函数

## 第3章 程序的简单算法设计



# 第4章 分支结构

## 4.1if 结构

例1：从键盘任意输入两个整数a和b，要求a的值总是小于或等于b的值，然后输出这两个数a和b的值。

```
#include <stdio.h>
main(){
	int a,b;
	printf("请输入两个整数:");
	scanf("%d%d",&a,&b);
	//if语句
	if(a<=b)
		printf("a=%d,b=%d",a,b); 
}
```

例2：从键盘输入一个整数，求该数的绝对值(利用abs()函数)。

```c
/*example4_2.c 求整型数的绝对值 */
#include <stdio.h>
#include <math.h>
main()
{
	int num;
	printf("请输入一个整数：");
	scanf("%d",&num);
	if(num<0)
//		num=-num;
		num=abs(num); //利用绝对值函数 
	printf("The absolute value is:%d\n",num);
}
```





```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
int main()
{
    int i;
     
    srand(time(NULL));//设置随机数种子。
     
    for(i = 0; i < 10; i ++)//运行10次。
        printf("%d\n", rand());//每次获取一个随机数并输出。
     
    return 0;
}
```

4.1.2 if....else语句

例1：从键盘任意输入两个整数a和b，要求a的值总是小于或等于b的值，然后输出这两个数a和b的值，否则输出“错误”两字。

```c
#include <stdio.h>
main(){
	int a,b;
	printf("请输入两个整数:");
	scanf("%d%d",&a,&b);
	
	if(a<=b)
	//语句1
		printf("a=%d,b=%d",a,b); 
	else
	//语句2
		printf("错误"); 
}
```

## 4.2 switch结构
例6：某班级准备周末举行一个班级活动，但活动内容要根据表中所示的天气情况来决定：

```c
/*example4_8.c  根据天气情况决定活动内容*/
#include <stdio.h>
main( )
{  
	int weather;
	printf("Please enter a weather:\n");
	scanf("%d",&weather);
	switch (weather) //假设输入3 
	{
	case 1:  printf ("晴天----活动内容：登山\n");
		     break;
	case 2:  printf ("有风无雨----活动内容：郊游\n");
	         break;
	case 3:  printf ("下雪----活动内容：堆雪人\n");
	         break;
	case 4:  printf ("下雨----不举行班级活动\n");
	         break;
	default: printf ("其他天气----活动内容：参观博物馆\n");
	}
}

```

作业：

编程实现，输入考试成绩，其中90-100分属于A级别，80-89分属于B级别，70-79分属于C级别，60-69分属于D级别，低于60分属于E级别，将成绩转化为相应五级制级别并输出。

作业：

模拟一个简单的计算器，进行两个数的加，减，乘，除四则运算

算法：

1. 编写简单的框架
2. 输入两个数字，一个字符
3. 利用switch分支结构进行字符判断
4. 输出结果

```c
#include <stdio.h>
void main()
{   
    int a,b;
	char ch;
//    scanf("%d",&a);
//	ch=getchar();
//	scanf("%d",&b);
	scanf("%d%c%d",&a,&ch,&b);
	switch (ch)
	{
		case '+':
			printf("%d%c%d=%d",a,ch,b,a+b);break;
		case '-':
			printf("%d%c%d=%d",a,ch,b,a-b);break;
		case '*':
			printf("%d%c%d=%d",a,ch,b,a*b);break;
		case '/':
//			printf("%d%c%d=%d",a,ch,b,a/b);break;
				if(b!=0){
					printf("%d%c%d=%d",a,ch,b,a/b);break;
				}else{
					printf("除数为零");break;
				}
	    default :  printf("输入表达式有错!\n");
	}
}
```



## 第五章 循环结构

### for语句

for语句是一种计数循环。循环次数由循环变量来控制。

 for语句的一般形式为：

 for (<初始表达式>;<条件表达式>;<循环表达式>)

 {

​    <循环体语句>   

 }

Efor语句的3个重要的组成部分：

 1．初始表达式——初始化循环控制变量。

 2．条件表达式——测试循环条件。

 3．循环表达式——更新循环控制变量的值。

```c
//求0-100的和 
#include <stdio.h>
main(){
	int i,sum=0;
	for(i=0;i<=100;i++)
	{
//		sum+=i;
		sum=sum+i; 		
	}
	printf("%d\n",sum);
}

```

作业：

求输出1-100之间能被2整除的数。（拓展1.所有偶数之和。2.所有奇数）

算法：

1. for语句生产1-100数
2. if语句判断i%2==0
3. 如果能被整除就输出i，否则继续循环

```c
#include <stdio.h>
main()
{
	int i,sum=0;
	for(i=1;i<=100;i++)
	{
		if(i%2==0)
		sum+=i;
	}
	printf("%d",sum);
}
```

### for语句嵌套

例3：编写程序，从键盘输入*m*和*n*的值，用符号“*”在屏幕上打印出如下所示具有*m*行*n*列的矩形图案。

```
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *
```

```c
/* example5_3.c 用*打印几何图案 */
#include <stdio.h>
void main()
{
	int i,j;	
		for(i=1;i<=5;i++)
		{	
			for(j=i;j<=5;j++) //注意此处 
				printf("*");
			printf("\n");
		}

}

/*

*****
*****
*****
*****
*****

*
**
***
****
*****
*****
****
***
**
*

*/ 

 
```



作业1：求5！（阶乘）

```c
#include <stdio.h>
main(){
	int i,sum=1;
	for(i=1;i<=5;i++)
	{
//		sum+=i;
		sum=sum*i; 		
	}
	printf("%d\n",sum);
}
 
```

作业2：求1！+2！+3！+4！+5！..100!的值

```c
#include<stdio.h>
main(){
	int a,b,c=1,sum=0;
	for(a=1;a<=5;a++){
		for(b=1;b<=a;b++)
			c*=b;//c=c*b		    
		    printf("%d\n",c);
		sum+=c;//sum=sum+c
		c=1;//复位 
	}
	printf("%d",sum); 
    
}

#include<stdio.h>
main(){
	int a,b,c,sum=0;
	for(a=1;a<=5;a++){
		c=1; 
		for(b=1;b<=a;b++)
			c*=b;//c=c*b		    
		    printf("%d\n",c);
		sum+=c;//sum=sum+c
		//复位 
	}
	printf("%d",sum); 
}
```

### while语句

```c
#include <stdio.h>
main(){
	int sum=0,i=1;
	while(i<=100) //i=101  
	{
		sum=sum+i;
		i++;
		printf("%d\n",sum);			
	}
}
```

注意的地方：

1. sum,i要有初始值
2. i要有增量
3. 表达式要真

作业1：求5！（要求用while语句）

```c
#include <stdio.h>
main(){
	int sum=1,i=1;
	while(i<=5) //i=101  
	{
		sum=sum*i;
		i++;
		printf("%d\n",sum);			
	}
}
```

例【5-7】编写程序，统计从键盘输入的字符个数（回车换行符也是一个字符），当遇到结束标志时程序结束。

分析：关键是循环计数。

 设置一个累加器count（初值为0），每次从键盘输入一个字符，只要该字符的值不等于结束标志，累加器的值就增1：count=count+1；

