# 语言程序设计

[toc]



## 第1章 引言 

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
int add(int x, int y); //函数声明
void main()
{ 
	int a, b, c;
	printf ("please input value of a and b:\n");
	scanf("%d %d", &a, &b);
	c=add(a,b); //函数的调用
	printf ("max=%d\n",c);
}
int add(int x, int y) //自定义函数
{
	return(x+y);
}
```

程序说明：

- 主函数体分为两部分：说明部分和执行部分。
- 语句c=add(a,b)；是通过调用加法器add()来完成a+b的计算，并将计算结果赋给变量c。
- 屏幕上显示字符串：“please input value of a and b:”是提示用户从键盘输入a和b的值，用户从键盘上键入两个数，屏幕上会显示出这两个数的和。

例：输入正方形的边长，输出正方形的周长,面积和边长。

```c
# include<stdio.h> 
void main()
{   float c,zc,mj;
    printf("输入你的正方形：");  
	scanf("%f",&c);   
	zc=4*c; 
    mj=c*c; 
    printf("周长%f，面积%f，边长%f",zc,mj,c);
}

```



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

## 第2章 基本的程序语句

### 2.2 基本数据类型及取值范围

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

作业：编写程序，输入华氏温度h，输出摄氏温度c。（摄氏温度=5/9*（华氏温度-32）

```c
/*sy2_2.c*/
#include<stdio.h>
int main()
{
     float h, c;
     printf("请输入华氏温度：");
     scanf("%f",&h);
     c=5.0/9*(h-32);
     printf("\n摄氏温度：%f\n",c);
	 return 0;
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



### 2.5标准输入/ 输出函数简介

#### 2.5.1 scanf函数

scanf(格式控制字符串，变量地址列表)

通过标准输入设备（键盘、写字板等），按照格式控制字符串中的格式要求为变量地址列表中的变量输入数据。

#### 2.5.2 printf函数

printf(格式控制字符串，输出列表)

将输出列表中的各个表达式的值按照格式控制字符串中对应的格式输出到标准输出设备（显示屏）

作业：从键盘输入一个3位正整数，要求输出该数的逆序数。例如输入123，输出321  

```c
/*sy2_4.c*/
#include<stdio.h>
int main()
{
  int a,b,c,x,y;
  printf("请输入一个3位的正整数：\n");
  scanf("%d",&x);
  a=x/100;				/*求x的百位数*/
  b=(x-a*100)/10;		/*求x的十位数*/
  c=x%10;				/*求x的个位数*/
  y=c*100+b*10+a;
  printf("%d: %d\n",x,y);
  return 0;
}

```



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

字符输出函数

## 第3章 程序的简单算法设计



## 第4章 分支结构

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

作业： 输入3个数，找出最小数并输出。 

```c
/*sy4_1.c*/
#include<stdio.h>
int main()
{
    int a,b,c,min;
    printf("input a,b,c:");
    scanf("%d%d%d",&a,&b,&c);
    if(a<b)
        min=a;
    else 
        min=b;
    if(c<min) min=c;
        printf("The minimum number is %d\n",min);
    return 0;
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



## 第5章 循环结构

### 5.1for语句

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

### 5.2-3while语句与do-while

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

```c
/*example5_7.c 统计从键盘输入的字符个数*/
#include <stdio.h>
void main()
{
	char ch;
	unsigned count=0; //无符号整型，只能正数 
	printf("please enter your words:\n");
	while((ch=getchar())!=EOF) //当有EOF结束标志符 ，回车符算一个字符 
		count=count+1;          //\n字符串结束标志符 ，回车符不算一个字符 
	printf("count=%u\n",count); //!，回车符不算一个字符 
}

```

题目：while和do-while两者的区别？当i=11时，分别的sum是多少？

```c
#include <stdio.h>
main()
{
	int sum=0,i=1;
	while(i<=10)
	{
		sum=sum+i;
		i++;
	}
	printf("%d\n",sum);//0
}
```

```c
#include <stdio.h>
main()
{
	int sum=0,i=1;	
	do
	{
		sum=sum+i;
		i++;		
	}while(i<=10);	
	printf("%d\n",sum);//
}
```

作业：水仙花数

```c
/*5.3.2  用while循环语句实现循环*/ 
/*实验练习2　求水仙花数*/ 

#include <stdio.h>
main ( )
{ 
       int x, y, z;
       int k=100;
      while(k<=999);           /* while循环条件，水仙花数是一个3位数*/
       {
          x=k/100;
          y=(k/10)%10;
          z=k%10;
          if (k==x*x*x+y*y*y+z*z*z)          /*水仙花数应当满足的条件*/
             printf("%d\n", k);
          k++;
       }
}
```



### 5.4break和continue语句

break语句

break使程序运行时中途退出switch结构或者一个循环体。

作业：编写程序实现，输入一个整数判断此数是否为素数。

```c
#include <stdio.h>
main(){
	int i,m;
	scanf("%d",&m);
	for(i=2;i<=m-1;i++)
	{
		if(m%i==0)
			break;//跳当前循环 
	}
	
	if(i<=m-1)
		printf("该数不是素数!\n");
	else
		printf("该数是素数!\n");
}
```
作业：输出10-100的全部素数。

```c
#include <stdio.h>
main(){
	int i,j;
	for(i=11;i<=100;i+=2)
	{
		for(j=2;j<=i-1;j++)			
			if(i%j==0)
				break;			
			
			if(j>=i)
			{
				printf("%4d",i);				
			}		
	}
}
```

continue语句

结束本次循环，跳过continue语句下面未执行的语句，继续进行下一次循环。

例：当跑到第3圈的时候,剩下部分不用跑,继续从第4圈开始跑 . 

```c
#include <stdio.h>
main(){
	int i;
	for(i=1;i<=10;i++)
	{
		if(i==3)
			continue; //break;
			printf("现在跑第%d圈\n",i);
			
	}	
}
```

作业：编写程序实现，输出100～200之间不能被3整除的数。（要用continue语句）

算法：

1. 循环100-200（for,while)
2. 判断i除以3不等0，输出i
3. 否则跳过，继续下一轮判断

```c
//方法1
#include<stdio.h>
main()
{
	int x;
	for(x=100;x<=200;x++)
	{
		if(x%3!=0)
		printf("%d\n",x);
	}
}
//方法2
#include<stdio.h>
main()
{
	int x;
	for(x=100;x<=200;x++)
	{
		if(x%3==0)
		continue;		
		printf("%d\n",x);
	}
}
//方法3
#include<stdio.h>
void main()
{
	int x=99; //x=100;
	while(x<=200)
	{
		++x; //x++;
		if(x%3==0)
			continue;
		printf("x=%d\n",x);		
	}
}
```



### 5.5for语句嵌套

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
#include <stdio.h>
void main()
{
	int i,j;	
		for(i=1;i<=5;i++)
		{	
//			for(j=1;j<=(5-i);j++)
//				printf(" ");
			for(j=1;j<=i;j++) //注意此处 
				printf("*");
			printf("\n");
		}

}

/*
*
**
***
****
*****
*/
```



```c
#include <stdio.h>
void main()
{
	int i,j;	
		for(i=1;i<=5;i++)
		{	
			for(j=1;j<=(5-i);j++)
				printf(" ");
			for(j=1;j<=i;j++) //注意此处 
				printf("*");
			printf("\n");
		}

}

/*
    *
   **
  ***
 ****
*****

*/
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

##　第６章　函数与宏定义

###　6.1函数的概念

C语言的函数分为两类：

1. 标准函数，又称为库函数。
2. 自定义函数 (C语言的核心)

```
自定义函数的形式：
[存储类型符] [返回值类型符]  函数名([形参说明表])
{
     <函数语句体> 
}
```

几点说明：

1. [存储类型符]指的是函数的作用范围，只有两种形式：static和extern。

   static说明的函数称为内部函数，只能作用于其所在的源文件，

   extern说明的函数称为外部函数，可被其他源文件中的函数调用。

   缺省情况为extern

2. [返回值类型符]指的是函数体语句执行完成后，函数返回值的类型。

   如int，float，char等。

   若函数无返回值，则用空类型void来定义函数的返回值。

   默认情况为int型（有些编译器不支持默认情况）。

3. 函数名由任何合法的标识符构成。

4. [形参说明表]是一系列用逗号分开的形参变量说明。

    如：int x, int y, int z

5. 函数语句体是放在一对花括号{ }中，由局部数据类型描述和功能实现两部分组成。

例：设计一个加法器

```c 
//自定义函数方法1
#include <stdio.h>
int add(int x,int y);//函数声明 
main(){
	int a,b,c;
	scanf("%d %d",&a,&b);
	c=add(a,b);//调用函数，实参 
	printf("c=%d",c);
}

int add(int x,int y){ //自定义函数，形参 
	return x+y;		
    
//自定义函数方法2
#include <stdio.h>
int add(int x,int y){ //自定义函数，形参 
	return x+y;		
}
main(){
	int a,b,c;
	scanf("%d %d",&a,&b);
	c=add(a,b);//调用函数，实参 
	printf("c=%d",c);
} 
```

例如，编写自定义函数abs_sum()，求两个任意整数的绝对值的和。

```c
/*example6_1.c 自定义函数，求两整数绝对值的和*/
#include <stdio.h>
int abs_sum(int m,int n);  /*函数声明，求m和n的绝对值之和*/
void main()
{
	int x,y,z;
	scanf("%d%d",&x,&y);
	z=abs_sum(x,y);      /*函数调用*/  
	printf("|%d|+|%d|=%d\n",x,y,z);
}

int abs_sum(int m,int n)   /*函数定义*/
{
	if(m<0)
		m=-m;
	if(n<0)
		n=-n;
	return m+n;
}

//
/*example6_1a.c 自定义函数，求两整数绝对值的和*/
#include <stdio.h>
int abs_sum(int m,int n)   /*函数定义*/
{
	if(m<0)
		m=-m;
	if(n<0)
		n=-n;
	return m+n;
}
void main()
{
	int x,y,z;
	scanf("%d%d",&x,&y);
	z=abs_sum(x,y);      /*函数调用*/
	printf("|%d|+|%d|=%d\n",x,y,z);
}
```

函数先后关系：

- 这样把abs_sum写在上面，是因为C的编译器是自上而下顺序分析代码。
- 当abs_sum写在上面的时候，编译器就知道需要几个参数，参数类型
- 当abs_sum写在下面的时候，代码前面需要函数(原型)声明

函数(原型)声明：

- 函数头，以分号‘;’
- 函数声明的目的告诉编译器自定义函数长什么样子，包括名称，参数，返回类型

作业：求和,1到10，20到30，35到45他们的和。

> 代码复制：是程序质量不良的表现

```c
#include <stdio.h>
void sum(int begin,int end); //函数原型声明 
main(){
	sum(1,10); //函数调用，实参 
	sum(20,30);
	sum(35,45);
	
}
void sum(int begin,int end) //自定义函数，形参 
{
	int i,sum=0;
	for(i=begin;i<=end;i++)
	{
		sum+=i;
	}
	printf("sum=%d\n",sum);
}

```

#### 函数的定义类型

- 无返回值无参数

```c
void Hello( )            //自定义函数
{ 
     printf ("Hello world!\n"); 
} 
main()                     //主函数
{
	Hello();
}

```

- 无返回值有参数

```c
void sum(int a,int b)   //自定义函数
{
      int s;
      s=a+b;
      printf("s=%d\n",s);
} 
main()                      //主函数
{
        int x=2,y=3;
        sum(x,y);
}

```

- 有返回值无参数

``` c
int sum()                  //自定义函数
{
      int a,b,s;
      scanf("%d%d",&a,&b);
      s=a+b;
      return s;
} 
main()                       //主函数
{
        int s;
        s=sum();
        printf("s=%d\n",s);
}

```

- 有返回值有参数

```c
int sum(int a,int b )    //自定义函数
{
      int s;
      s=a+b;
      return s;
} 
main()                       //主函数
{
        int x,y,s;
        scanf("%d%d",&x,&y);
        s=sum(x,y);
        printf("s=%d\n",s);
}

```

#### 函数的嵌套调用

函数嵌套就是**函数调用其它函数**

例：利用函数嵌套实现程序设计，求1！+2！+…+5！

```c
#include <stdio.h>
int fact(int n){
	int f=1,i;
	for(i=1;i<=n;i++)
		f=f*i;
	return f;
}
int sum(int h){
	int i,s=0;
	for(i=1;i<=h;i++)
		s=s+fact(i); //调用fact求阶乘 
	return s;

}
main(){
	int s;
	s=sum(5);
	printf("s=%d\n",s);	
}

```

#### 函数的递归调用

```c
#include <stdio.h>
// n! 递归 
int fact(int n);//函数声明 

main(){
	int s;
	s=fact(5);//函数调用 
	printf("s=%d\n",s);
}

int fact(int n){//函数定义 n=5 n=4 n=3 n=2
	if(n==1)
		return 1;
	else
		return n*fact(n-1); // n=5*fact(4)  n=4*fact(3) n=3*fact(2) n=2*fact(1)
							// n=5*24  n=4*6 n=3*2 n=2*1
}
```

#### 局部变量和全局变量(作用域)

```c
//局部变量
#include <stdio.h>
void f(int a,int b)
{
    int i,j;
    i=a+2;
    j=b-1;
    printf("函数f中:a=%d,b=%d\n",a,b);
    printf("函数f中:i=%d,j=%d\n",i,j);
}
main()
{
    int i=4,j=5;
    f(i,j);
    printf("主函数中:i=%d,j=%d\n",i,j);
} 

```

```
//全局变量
#include <stdio.h>
float s; //全局变量 

float ls(float r)
{
    float len; //局部变量 
    len=2*3.14*r;
    s=3.14*r*r;
    return len;//返回周长len 
}

main()
{
    float c,r;
    printf("请输入圆的半径:");
    scanf("%f",&r);
    c=ls(r);
    printf("圆的周长为:%f\n",c);
    printf("圆的面积为:%f\n",s);
} 

```

#### 动态变量和静态变量（存储类型）

```c
f(int a)          
{
   auto int b,c=3; //动态变量，函数f执行完以后自动释放a,b,c的空间     
   …… 
} 

```

```c
#include <stdio.h>
f(int a) //a=1 a=1
{
    auto b=2; //动态变量，局部变量  b=2 b=2
    static c=3; // 静态变量  c=3 c=4
    b=b+1; //b=3 b=3
    c=c+1;  //c=4 c=5
    return a+b+c; //8 9
} 
main() 
{
    int a=1,i; 
    for(i=1;i<=2;i++) 
      printf("第%d次调用后结果：%d\n",i,f(a));   //i=1 a=1 (结果是8),i=2  a=1(结果是9)   
} 

//（1）静态变量属于静态存储类别，在静态存储区内分配, 存储单元，在程序整个运行期间都不释放。 
//（2）静态变量在编译时赋初值，即只赋初值一次。
//定义：变量的值在函数调用结束后保留原值，用关键字static进行声明，称为静态变量。
```

#### 宏定义

```c
#define PI 3.14 //符号常量 
main()
{
    float l,s,r;
    printf("请输入半径:");
    scanf("%f",&r);
    l=2.0*PI*r;
    s=PI*r*r;
    printf("l=%.2f s=%.2f\n",l,s);
} 

```

#### 条件编译

宏定义标识符为编译条件    

```c
#define DEBUG
main()
{
   int x,y;
   x=2;
   y=3;
   x*=x+2;//x=x*(x+2) x=8
   y/=y-2;//y=y/(y-2) y=3
   #ifdef DEBUG
      printf("x=%d,y=%d\n",x,y); 
   #endif
   printf("x+y=%d\n",x+y); 
} 

```

常量表达式值为编译条件

```c
#define R 0  
main()
{
   char web[50];
   int i=0;
   gets(web);
   while(web[i]!='\0')
   {
        #if(R==1)   
          if(web[i]>='A'&&web[i]<='Z')
          {web[i]=web[i]+32;  i++;}
        #else
           if(web[i]>='a'&&web[i]<='z')
           {web[i]=web[i]-32; i++;}
        #endif
    }  
    puts(web);
} 
```



## 期中复习

1. 简单的程序，比如输出函数 printf("Hello world!")
2. 运算符及优先级
3. 取余，取整（运算），其它输入和输出函数。
4. 流程图
5. 判断，找最大或最小数
6. 分支判断if-else或switch,简单的计算器
7. 循环语句，求和，求积
8. 循环语句，判断，取余取整运算
9. 素数
10. 可能用自定义函数，相加或绝对值



## 数组

### 一维数组

定义：一维数组用来存放多个相同类型数据组成的一个集合。 

格式：类型说明符 数组名[长度]；

说明：

1. 数组名的命名规则必须遵循**标示符**的命名规则。

2. 长度必须是整数，整型常量或整型常量表达式来表示，不能使用变量或含有变量的表

   达式，长度必须用方括号括起来。

3. 数据类型说明符可以是基本类型，也可以是构造类型。

4. 数组中的元素用数组名和下标相结合来区分，下标是从0开始。

5. 数组名等价于数组的首地址，也就是数组中第一个元素的地址。即a与&a[0]等价。  

```
int b[3+4];//是合法的。 
float c[n];  double d[n+1];// 是非法的。
a[2]//是数组中的第3个元素。
```

初始化：

1. 在定义数组时，赋给数组各元素的初值。`int d[3]={3,1,5};`
2. 数组的长度可以省略不写。`int d1[]={3,1,5};`
3. 数组中部分元素初始化，则长度不能省略，其他没有赋值的元素的初始值为0`int e[5]={3,1,5};`
4. 数组中的元素初始化时，括号中只有一个零 `int f[5]={0};`

引用：

数组名[下标]

下标为整数，从0开始，最大值为长度-1，下标要用方括号括起来

```c
//数组的简单输入输出
#include<stdio.h>
main(){
	int a[10],i,max,min;
	printf("请输入10位同学的成绩：\n");
	for(i=0;i<10;i++)
		scanf("%d",&a[i]);	
	printf("输出10位同学的成绩：\n");	
	for(i=0;i<10;i++)
		printf("%d\t",a[i]);
}  
```

实例：输入10个学生的某一门功课成绩，求出这些学生该门功课的平均成绩、最高分和最低分?

```c
#include<stdio.h>
main(){
	int a[10],i,max,min;
	float avg=0;
	printf("请输入10位同学的成绩：\n");
	for(i=0;i<10;i++)
		scanf("%d",&a[i]);//&a[0] &a[1]....&a[9]
	
	max=a[0];min=a[0];	
	for(i=0;i<10;i++){
		avg=avg+a[i];
		if(a[i]>max)
			max=a[i];
		if(a[i]<min)
			min=a[i];
	}	
	printf("10位同学的平均值：%.2f,最高分%d,最低分%d",avg/10,max,min);

}  
```

实例：用冒泡算法对5个数进行从小到大排列。

180,150,170,160,120

第1轮 i=0

j=0                    1                     2                 3

a[0]>a[0+1]    a[1]>a[2]      a[2]>a[3]     a[3]>a[4]

180>150

150,180,170,160,120

150,170,180,160,120

150,170,160,180,120

150,170,160,120,180

第2轮 i=1

j=0                    1                     2                 

a[0]>a[0+1]    a[1]>a[2]      a[2]>a[3]     

150,170,160,120,180

150,160,170,120,180

150,160,120,170,180

第3轮 i=2

j=0                    1

a[0]>a[0+1]    a[1]>a[2]

150,160,120,170,180

150,120,160,170,180

第4轮 i=3

j=0

a[0]>a[0+1]

120,150,160,170,180



```c
#include<stdio.h>
main(){
	int a[5]={180,150,170,160,120},i,j,t;
	for(i=0;i<=3;i++) 
		{
			for(j=0;j<=3-i;j++)
				if(a[j]>a[j+1])
					{
						t=a[j];
						a[j]=a[j+1];
						a[j+1]=t;
					}		
		}
	for(i=0;i<=4;i++) 
        printf("%d ",a[i]);
}  
```

#### 字符数组

定义：其数组元素的数据类型为字符型变量，关键字为char。

char 数组名[长度]； 
char  ch[5];

初始化：

1. char ch[5]={‘h’,‘e’,‘l’,'l','o'}; 
2. 字符数组的长度也可以省略不写  `char ch[]={‘h’,‘e’,‘l’,'l','o'};`
3. 字符数组中部分元素初始化，其中ch[4]的初值为‘\0’ `char ch[5]={‘h’,‘e’,‘l’,'l'};`

引用：

ch[2]=ch[3];

#### 字符串

定义：字符串一般使用字符数组来处理，字符串的结束标志’\0’也要存放在该字符数组中。

char ch[6]={‘h’,‘e’,‘l’，‘l’，‘o’，‘\0’ }; 

char ch[6]=“hello”; 同上面赋值方法等价，系统自动在末尾加‘ \0‘

常见的函数：

1. 输出函数  `	puts(ch);`  也可以通过for语句输出
2. 输入函数 gets(ch);
3. 连接函数 strcat(a,b);   注意导入#include<string.h>
4. 字符串复制函数strcpy(a,b) ;
5. 字符串比较函数strcmp(a,b); 
6. 求字符串长度函数strlen(a); 不包括字符串结束的标志’\0’   
7. 大写字母转换小写字母函数strlwr();
8. 小写字母转换大写字母函数strupr();

例：将输入的大写字符串转换成小写输出

```c
#include <stdio.h>
#include <string.h>

main()
{
	char a[20];
	printf("请输入一个字符串：");
	gets(a);
	strlwr(a);
	printf("字符串转换后：");
	puts(a);	
}
```



#### 二维数组

`数据类型说明符 数组名[常量表达式1][常量表达式2]; `

`int a[2][3]`

说明：

1. 二维数组中的每个元素都有2个下标，都必须分别放在单独的方括号内。 
2. 二维数组定义中常量表达式1表示该数组具有的行数，常量表达式2表示该数组具有的列数；两个数字的乘积是该数组的元素的个数。 
3. 二维数组的存放规律是**按行存储的**。 `int b[2][3]; 存储过程：a[0][0]→a[0][1]→a[0][2]→a[1][0]→a[1][1]→a[1][2]`

初始化：

1. 按行给二维数组所有元素初始化。`int b[3][2]={{1,6},{2,5},{3,4}}; `
2. 按存储顺序给二维数组所有元素初始化 `int d[4][3]={1,2,3,4,5,6,7,8,9,10,11,12};  `
3. 二维数组第1维长度可以省略。 `int array[][3]={1,3,9,2,4,6,5,7,8};  `
4. 对部分元素赋初值 `int array[2][3]={1,3,9}; `

引用：

数组名[下标] [下标]

实例：

打印出以下的杨辉三角形（要求打印出10行）;

```
杨辉三角形：
     1
     1     1
     1     2     1
     1     3     3     1
     1     4     6     4     1
     1     5    10    10     5     1
     1     6    15    20    15     6     1
     1     7    21    35    35    21     7     1
     1     8    28    56    70    56    28     8     1
     1     9    36    84   126   126    84    36     9     1
```

第一行

i=0   j=0

`a[0][0]=1`

第二行

i=1 j=0 1

`a[1][0]=1,a[1][1]=1`

第三行

i=2  j= 0 1 2

`a[2][0]=1,a[2][1]=a[1][0]+a[1][1]=2,a[2][2]=1`

其它略

```c
#include <stdio.h>
#define M 10
main()
{
	int a[M][M],i,j;
	for(i=0;i<M;i++)
		for(j=0;j<=i;j++)
		{
			if(j==0 || i==j)
				a[i][j]=1;
			else
				a[i][j]=a[i-1][j-1]+a[i-1][j];
		}			
	printf("杨辉三角形：\n");
	for(i=0;i<M;i++)
	{
		for(j=0;j<=i;j++)
			printf("%6d",a[i][j]);
		printf("\n");
	}
}
```

作业：利用数组计算斐波那契数列的前10个数，即1，1，2，3，5，8，13，21，34，55

算法：
1.  int fib[10]={1,1}
2. 通过循环生成剩余的8个数  fib[i]=fib[i-1]+fib[i-2]
3. 最后输出

```c
#include <stdio.h>
main(){
	int a[10],i;
	a[0]=1;
	a[1]=1;
	for(i=2;i<=10;i++)
	{
		a[i]=a[i-1]+a[i-2];		    
	}
	printf("l输出斐波那契数列：");
	for(i=0;i<10;i++)
		printf("%d ",a[i]);
	
}
```



## 指针

指针就是保存地址的变量

### 相关知识

获取变量空间大小sizeof

```c
#include<stdio.h>
int main(){
	int a;
	a=6;
	printf("sizeof(int)=%ld\n",sizeof(int));
	printf("sizeof(a)=%ld\n",sizeof(a));
	printf("sizeof(double)=%ld\n",sizeof(double));
}
```



打印地址

```c
#include<stdio.h>
int main(){
	int a=0;
	printf("0x%x\n",&a);
	printf("%p\n",&a);
}
```

打印相邻的两个地址

```c 
#include<stdio.h>
int main(){
	int i=0;
	int p;
	printf("%p\n",&i); //十六进制 
	printf("%p\n",&p);
}
```

数组的地址

```c
#include<stdio.h>
int main(){
	int a[10];
	printf("%p\n",&a);
	printf("%p\n",a);
	printf("%p\n",&a[0]);
	printf("%p\n",&a[1]);
}
```

### 指针的定义

```c
int *p;
```

### 指针的赋初值

```c
#include<stdio.h>
int main(){
 	int a=3,b=7,*p,*q;
 	p=&a; //p-->a
	q=&b; //q-->b	
	char a1='b',*p1=&a1; //p-->a
	printf(" a=%p\n",&a);
	printf("*p=%p\n",p);
}
```

### 引用

```
#include<stdio.h>
int main(){
	int a=7,b=9,*p;
	p=&a;
	*p=*p+b;
	printf("%d,%d\n",a,*p);
}
 	
```

例：采用指针变量对两个整数进行从小到大排序

````c
#include <stdio.h>
main()
{
	int a,b,*t,*p,*q;
	p=&a;
	q=&b;
	printf("请输入两个整数：");
//	scanf("%d%d",p,q); //等价写法 
	scanf("%d%d",&a,&b); //7 3 
	if(*p>*q) //*p 指针变量所指向变量的值 
	{
		t=p; //t p 是存放地址 
		p=q;
		q=t;
	}
	printf("两个整数从小到大排序为：%d，%d\n",*p,*q);
}
````

### 指针变量指向一维数组

```c
#include <stdio.h>
main()
{
	int a[5],*p;
	p=&a[0];
}
```

### 指针变量指向一维数组的引用

```c
#include <stdio.h>
main()
{
	int a[5],*p;
	p=&a[0];
}
/* 引用地址
下标法           地址法     指针法 
 &a[0]            a+i        p+i
   引用数值 
  a[0]            *(a+i)    *(p+i)
*/ 
```

### 指针的移动

```c
#include <stdio.h>
main()
{
	int a[10]={5,2,0,1,3},*p;
	p=a; //等价p=&a[0]
	printf("%d\t",*p);
	printf("%p\n",p);
	p=p+2;
	printf("%d\t",*p);
	printf("%p\n",p);
	p++;
	printf("%d\t",*p);
	printf("%p\n",p);
	++p;
	printf("%d\t",*p);
	printf("%p\n",p);

}
```

```c
#include <stdio.h>
main()
{
	int a[10]={5,2,0,1,3},*p;
	p=a; //等价p=&a[0]
	printf("%d\t",*p);
	printf("%p\n",p);
	p=p+2;
	printf("%d\t",*p);
	printf("%p\n",p);
//	p++;
//	printf("%d\t",*p);
	printf("%p\n",p++); //先打印地址，再地址加4个字节
	
//	++p;
//	printf("%d\t",*p);
	printf("%p\n",++p);//先加四个字节地址，再打印地址。总共移动了8个字节。

}
```

### 字符指针

```c
#include<stdio.h>
main(){
	char *p="l love china!";
	printf("%s\n",p);
	printf("%s\n",p+7);	
}
```

例：用字符指针实现求字符串长度

```c
#include<stdio.h>
main(){
	char str[100],*p;
	int k=0;
	p=str;
	printf("请输入一个字符串：");
	gets(p);
	for(;*p!='\0';p++)
	     k++;
	printf("该字符串的长度为%d\n",k);
	
}
```


### 指针作为函数参数 

例：定义一个函数，用指针对两个数进行从小到大排序

```c
#include <stdio.h>

void exchange(int *p,int *q);//指针作为参数列表 

main()
{
	int a,b;
	printf("请输入两个数："); 
	scanf("%d%d",&a,&b);
	if(a>b)
		exchange(&a,&b); //调用时需要& 
	printf("排序结果为：%d，%d\n",a,b);	
}

void exchange(int *p,int *q){
	int t;
	t=*p;
	*p=*q;
	*q=t;
}
```

例：定义一个函数，用指针实现两个数字的交换

```c
#include <stdio.h>
void exchange(int *p,int *q)
{
	int t;
	t=*p;
	*p=*q;
	*q=t;
}
main()
{
	int a,b;
	printf("请输入两个数：");
	scanf("%d%d",&a,&b);	
	exchange(&a,&b);
	printf("交换后：%d，%d\n",a,b);
}

```





例：

```c
#include<stdio.h>
void f(int *p);
void g(int k);
int main(){
	int i=6;
	printf("&i=%p\n",&i);
	f(&i); //按地址 
	g(i); // 按数值 
	return 0;
}

void f(int *p)
{
	printf("p=%p\n",p);//地址 
	printf("*p=%d\n",*p); //值
	*p=26; //*p就等于i，*是一个单目运算符，用来访问指针的值所表示的地址上的变量
}

void g(int k)
{
	printf("k=%d\n",k);
}
```

### 指向数组的指针作为函数的参数

例：定义一个函数，用指针实现数组元素从小到大排序。 

```c
#include <stdio.h>

void sort(int *p,int n);

main()
{
	int a[10],i;
	for(i=0;i<5;i++)
		scanf("%d",&a[i]);
	sort(a,5);
	for(i=0;i<5;i++)
		printf("%4d",a[i]);
}

void sort(int *p,int n){
	int i,j,t;
	for(i=0;i<n-1;i++)
		for(j=0;j<n-1-i;j++)
			if(p[j]>p[j+1])
				{
					t=p[j];
					p[j]=p[j+1];
					p[j+1]=t;
				}
}
```

### 指向字符串的指针作为函数的参数

例：定义一个函数，用指针将一个字符串复制到另外一个字符串中。

```c
#include <stdio.h>

void StringCopy(char *p,char *q);

main()
{
	char a[20],b[20];
	printf("请输入一个字符串：");
	gets(b);
	StringCopy(a,b);
	printf("数组a为：%s\n",a);
}

void StringCopy(char *p,char *q){
	for(;*q!='\0';q++,p++)
		*p=*q;
	*p='\0';
	
		
}
```

## 构造类型

###  结构体类型定义

struct 结构体名 

 { 

   数据类型1 成员列表1； 

   数据类型2 成员列表2； 

​     … 

   数据类型n 成员列表n； 

 }； 

注意说明：



```c
#include <stdio.h>
main(){
	//结构体类型定义 
	struct  student{
		 int number；
	     char name[8]； 
	     char sex； 
	     int age；
	     float c_program
	};	
}
```



## 结构体变量定义

1. 先定义结构体类型，再定义结构体变量一般形式如下：

`struct student st1,st2;//st1,st2变量的定义`

2. 定义结构体类型的同时定义结构体变量

```c
	struct  student{ //student结构体名称 
		 int number；
	     char name[8]； 
	     char sex； 
	     int age；
	     float c_program
	}st1,st2;
```

3. 使用结构体变量定义结构体

```c
#include <stdio.h>
main(){
struct date 
{ 
	int month; 
	int day; 
	int year; 
}; 
    
struct student
{ 
   int number;
   char name[8]; 
   char sex; 
   int age;
   struct date birthday;
}st1,st2;

}
```

###  变量引用  

1.  定义结构体类型同时定义结构体变量时，给结构体变量st1、st2赋初值

```c
#include <stdio.h>
main(){
	struct student{
		int number;
		char name[8];
		char sex;
		int age;
		float c_program;
	}st1={35013101,"王 迪",'F',20,90},st2={35013112,"杨 光",'M',19,80};
}
```

2. 先定义结构体类型struct student，再定义结构体变量st1、st2，然后赋初值。 

```c
#include <stdio.h>
main(){
	struct student{
		int number;
		char name[8];
		char sex;
		int age;
		float c_program;
	};
	struct student st1={35013101,"王 迪",'F',20,90},st2={35013112,"杨 光",'M',19,80};
}
```

作业：假设学生的基本信息包括学号，姓名，三门课程成绩以及个人平均成绩。输入n个学生的成绩信息，计算并输出平均分最高的学生信息。

```c
#include "stdio.h"
struct student //结构体类型定义 
{ 
	int num; //学号 
	char name[10]; //姓名 
	int computer,english,math; //计算机，英语，数学 
	double average;	//平均成绩 
}; 
main()
{
	int i,n;
	struct student s1,max;
	printf("请输入n:");
	scanf("%d",&n);	
	printf("请输入学生信息（学号、姓名、计算机、英语、数学）:\n");
	for(i=1;i<=n;i++){
		printf("NO.%d:",i);
		scanf("%d %s %d %d %d",&s1.num,s1.name,&s1.computer,&s1.english,&s1.math);
		s1.average=(s1.math+s1.computer+s1.english)/3.0;
		if(i==1) //假设序号1的同学平均成绩最高，把它赋值给max 
			max=s1;
		if(max.average<s1.average)
			max=s1; 
	}	
	//输出平均分最高的学生信息,包含学号，姓名，平均成绩 
	printf("平均分最高的学生:\n");
	printf("num:%d name:%s avg:%.2lf",max.num,max.name,max.average);
	
}

```

### 结构体数组

例：计算某班级学生的C语言课程平均成绩？

```c
#include "stdio.h"
struct student 
{ 
    int number;
    char name[8]; 
    char sex; 
    int age;
    float c_program; 
}stu[5]={
	      {35013101,"王 迪",'F',20,90},
		  {35013105,"赵晶晶",'F',21,95},
		  {35013112,"杨 光",'M',19,80},
		  {35013125,"周腾巍",'M',21,93},
		  {35013130,"孙益龙",'M',20,100}
        }; 
main()
{
	int i; 
    float ave,sum=0; 
    for(i=0;i<=4;i++) 
       sum=sum+stu[i].c_program; 
    ave=sum/5; 
    printf("ave=%.1f\n",ave);
}

```

作业：尝试输出某一班级的记录

`printf("%4d\t%s\t%c\t%4d\t%f\n",stu[i].number,stu[i].name,stu[i].sex,stu[i].age,stu[i].c_program);`

结构体变量与函数

作业：设某团体要进购一批书籍，共4种。缩写程序，从键盘输入书名、购买数量、书的单价，计算每种书的总金额和所有要购书的总金额，输出购书清单。

```c
/*example9_2.c  输出购书清单，函数的参数为结构类型*/
#include <stdio.h>
#include <conio.h> //控制台输入输出
#include <stdlib.h>
struct BookLib //结构体定义 
{
	char name[12];
	int num;
	float price;
	float SumMoney; //单本书的总价 
};
void list(struct BookLib StuBook);//函数声明 
main()
{
	struct BookLib Book[4];//结构体变量定义 
	int i,sum=0;//整型变量定义，sum用来求总数量 
	float Total=0;//全部书的总价 
	printf("请输入4本要购进的书籍信息：书名  数量  单价\n");
	for(i=0;i<4;i++)
	{
		scanf("%s",Book[i].name);  /* 输入书名 */
		scanf("%d%f",&Book[i].num,&Book[i].price);   /* 输入数量和单价 */
		Total=Total+Book[i].num*Book[i].price;
		sum+=Book[i].num; //全部书的总价 
	}
	printf("\n----------------------------------------------\n");
	printf("购书清单：\n");
	printf("书名\t\t\t数量\t单价\t合计\n");
	for(i=0;i<4;i++)
		list(Book[i]);    /* 输出购书清单 */ //函数调用 
	printf("共%d本书，购书金额总计：%.2f\n",sum,Total);//输出购书数量和总价 
	
}
void list(struct BookLib StuBook)//自定义函数 ，参数是结构体 
{
	StuBook.SumMoney=StuBook.num*StuBook.price;//单本书的总价 
	printf("%-24s%d\t%.2f\t%.2f\n",StuBook.name,
		  StuBook.num,StuBook.price,StuBook.SumMoney); //输出书名 数量 单价 总价 
}
```

### 共用体

```c
#include <stdio.h>
union data{ //共用体类型定义 
		char ch; //1
		int i;  //4
		float f; //8
	}; //共用体变量定义 

main(){
	union data a,b,c;
	a.ch='a';
	a.i=10;
	a.f=289.2;
	printf("%c \t%d\t %.2f",a.ch,a.i,a.f); 
	//a 10 289.2
}
/*
结构体与共用体区别：
1.空间大小不一样，结构体全部相加，共用体是最大成员的空间 
2.数据可见性， 结构体全部可见，共用体是对最后一个可见
3.结构体变量可以进行初始化，共用体变量不能进行初始化
*/ 

```

### 枚举类型

```c
#include <stdio.h>
main(){
	enum weekday{sun,mon,tue,wed,thu,fri,sat}a,b,c; 
	//a=0;  //枚举元素是常量，不需要双引号，也不需要单引号，不是变量 
	a=(enum weekday)0;
	b=mon;
	c=tue; //不能把数据直接赋值给枚举变量 
	printf("sun=%d,mon=%d,tue=%d",a,b,c);
	
}
```

### 类型定义符

```c
#include <stdio.h>
main(){
	//类型定义符 typedef 
	int a,b;
	typedef int INT;
	INT c,d;
	
	char name[10];
	
	typedef char NAME[20]; 
	NAME a100,a2,a3; //char a100[20],a2[20],a3[20]
	
	typedef struct stu{
		char name[10];
		int age;
		char sex; 
	}STU; //STU是别名 
	STU b1,b2; //struct stu b1,b2		
}
```

### 链表

#### 分配内存函数       

格式：

(类型说明符*)malloc(size)

pc=(char *)malloc(5);  //返回空间的首地址

#### 释放内存函数

free(void*ptr); 

#### 链表

定义：

可在第一个结点的指针域内存入第二个结点的首地址，在第二个结点的指针域内又存放第三个结点的首地址，如此串连下去直到最后一个结点。（空间不连续） 

```c
#include <stdio.h>
#include <stdlib.h>
main(){
struct stu 
{  
    int number; 
    float c_program; 
    struct stu *next; //自引用 指针类型 
}; 

	struct stu *pf;//结构体指针变量定义，指针类型 
	//pf->number=10;
	pf=(struct stu*)malloc(sizeof(struct stu));// 分配内存函数
	(*pf).number=10; //成员引用 
	pf->c_program=12.1;
	pf->next;
	
}
```



例：（单链表）编写程序，创建一个链表，该链表可以存放从键盘输入的任意长度的字符串，以按下回车键作为输入的结束。统计输入的字符个数并将其字符串输出。

```c
/* example9_7.c   创建字符串链表并将其输出 */
#include <stdlib.h>
#include <stdio.h>
struct string
{
   char ch;
   struct string *nextPtr;
};
struct string *creat(struct string *h);
void print_string(struct string *h);
int num=0;
main()
{
   struct string *head;                 	/*定义表头指针*/
   head=NULL;                     			/*创建一个空表*/
   printf("请输入一行字符（输入回车时程序结束）:\n");
   head=creat(head);                			/*调用函数创建链表*/
   print_string(head);                 			/*调用函数打印链表内容*/
   printf("\n输入的字符个数为：%d\n",num);
}
struct string *creat(struct string *h)
{
   struct string *p1,*p2;
   p1=p2=(struct string*)malloc(sizeof(struct string)); 	/*申请新结点*/
   if(p2!=NULL)
   {
      scanf("%c",&p2->ch); 	/*输入结点的值*/
      p2->nextPtr=NULL;    	/*新结点指针成员的值赋为空*/
   }
   while(p2->ch!='\n')
   {
      num++;       			/*字符个数加1 */
      if(h==NULL)
        h=p2;       		/*若为空表，接入表头*/
      else
        p1->nextPtr=p2; 	/*若为非空表，接入表尾*/
      p1=p2;
      p2=(struct string*)malloc(sizeof(struct string));	/*申请下一个新结点*/
      if(p2!=NULL)
      {
        scanf("%c",&p2->ch);	/*输入结点的值*/
         p2->nextPtr=NULL;
      }
   }
   return h;
}
void print_string(struct string *h)
{
   struct string *temp;
   temp=h;                	/*获取链表的头指针*/
   while(temp!=NULL)
   {
        printf("%-2c",temp->ch);  /*输出链表结点的值*/
        temp=temp->nextPtr;       /*移到下一个结点*/
   } 
}

```

#### 链表案例（公交线路站点信息）

编写程序，用链表的结构建立一条公交线路的站点信息，从键盘依次输入从起点到终点的各站站名，以单个“#”字符作为输入结束，统计站的数量并输出这些站点。

```c
/* example9_8.c   创建公交线路站名链表并将其输出 */
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
struct station
{
   char name[20];
   struct station *nextSta;
};
struct station *creat_sta(struct station *h);
void print_sta(struct station *h);
int num=0;
main()
{
    struct station *head;
    head=NULL;
    printf("请输入站名:\n");
    head=creat_sta(head);
    printf("---------------------------\n");
    printf("共有%d个站点:\n",num);
    print_sta(head);
}
struct station *creat_sta(struct station *h)
{
   struct station *p1,*p2;
   p1=p2=(struct station*)malloc(sizeof(struct station));
   if(p2!=NULL)
   {
       scanf("%s",&p2->name);
       p2->nextSta=NULL;
   }
   while(p2->name[0]!='#')
   {
        num++;
        if(h==NULL)
           h=p2;
        else
           p1->nextSta=p2;
        p1=p2;
        p2=(struct station*)malloc(sizeof(struct station));
        if(p2!=NULL)
        {
        scanf("%s",&p2->name);
           p2->nextSta=NULL;
        }
   }
   return h;
}
void print_sta(struct station *h)
{
   struct station *temp;
   temp=h;           
   while(temp!=NULL)
   {
      printf("%-s, ",temp->name);  
      temp=temp->nextSta;       
   }
}

```

从键盘输入一个要删除的站点名，并将删除后的站点依次输出

```c
/* example9_9.c   删除链表中的一个结点并将结果输出 */
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>
struct station
{
   char name[8];
   struct station *nextSta;
};
struct station *creat_sta(struct station *h);
void print_sta(struct station *h);
struct station *del_sta(struct station *h,char *str);
int num=0;
main()
{
   struct station *head;
   char name[50],*del_stas=name;
   head=NULL;
   printf("请输入站名:\n");
   head=creat_sta(head);  /* 建立链表 */
   printf("---------------------------\n");
   printf("站点数为：%d\n",num);
   print_sta(head);      /* 输出链表中的站点信息 */
   printf("\n请输入要删除的站名:\n");
   scanf("%s",name);
   head=del_sta(head,del_stas);  /* 删除链表中的一个站点 */
   printf("---------------------------\n");
   printf("新的站点为：\n");
   print_sta(head);  /* 输出删除站点后链表中的站点信息 */
   printf("\n");
}
/* 建立由各站点组成的链表 */
struct station *creat_sta(struct station *h)
{
   struct station *p1,*p2;
   p1=p2=(struct station*)malloc(sizeof(struct station));
   if(p2!=NULL)
   {
      scanf("%s",&p2->name);
      p2->nextSta=NULL;
   }
   while(p2->name[0]!='#')
   {
      num++;
      if(h==NULL)
         h=p2;
      else
         p1->nextSta=p2;
      p1=p2;
      p2=(struct station*)malloc(sizeof(struct station));
      if(p2!=NULL)
      {
      scanf("%s",&p2->name);
          p2->nextSta=NULL;
      }
   }
   return h;
}
/* 输出链表中的信息 */
void print_sta(struct station *h)
{
   struct station *temp;
   temp=h;           		/*获取链表的头指针*/
   while(temp!=NULL)
   {
      printf("%-8s",temp->name);  		/*输出链表结点的值*/
      temp=temp->nextSta;       		/*移到下一个结点*/
   }
}
/* 修改链表中指针的指向，删除的站点名为str所指的字符串*/
struct station *del_sta(struct station *h,char *str)
{
   struct station *p1,*p2;
   p1=h;
   if(p1==NULL)
   {
     printf("The list is null\n");
     return h;
   }
   p2=p1->nextSta;
   if(!strcmp(p1->name,str))
   {
     h=p2;
     return h;
   }
   while(p2!=NULL)
   {
     if(!strcmp(p2->name,str))
     {
       p1->nextSta=p2->nextSta;
       return h;
     }
     else
     {
       p1=p2;
       p2=p2->nextSta;
     }
   }
   return h;
}
```

键盘输入一个要加入的站点名，并将加入后的站点依次输出

```c
/*example9_10.c   在链表中增加一个结点并将结果输出 */
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>
struct station
{
   char name[8];
   struct station *nextSta;
};
struct station *creat_sta(struct station *h);
void print_sta(struct station *h);
struct station *add_sta(struct station *h,char *stradd, char *strafter);
int num=0;
main()
{
	struct station *head;
	char add_stas[30],after_stas[30];
	head=NULL;
	printf("请输入线路的站点名:\n");
	head=creat_sta(head); /* 建立站点线路的链表 */
	printf("---------------------------\n");
	printf("站点数为：%d\n",num);
	print_sta(head);     /* 输出站点信息 */
	printf("\n请输入要增加的站点名：\n");
	scanf("%s",add_stas);
	printf("请输入要插在哪个站点的后面：");
	scanf("%s",after_stas);
	head=add_sta(head,add_stas,after_stas);
	printf("---------------------------\n");
	printf("增加站点后的站名为：\n");
	print_sta(head);   /* 将新增加的站点插入到链表中 */
	printf("\n");
}
/* 建立站点线路的链表： */
struct station *creat_sta(struct station *h)
{
   struct station *p1,*p2;
   p1=p2=(struct station*)malloc(sizeof(struct station));
   if(p2!=NULL)
   {
      scanf("%s",&p2->name);
      p2->nextSta=NULL;
   }
   while(p2->name[0]!='#')
   {
      num++;
      if(h==NULL)
        h=p2;
      else
         p1->nextSta=p2;
      p1=p2;
      p2=(struct station*)malloc(sizeof(struct station));
      if(p2!=NULL)
      {
     scanf("%s",&p2->name);
         p2->nextSta=NULL;
      }
   }
   return h;
}
/* 输出站点信息： */
void print_sta(struct station *h)
{
   struct station *temp;
   temp=h;           			/*获取链表的头指针*/
   while(temp!=NULL)
   {
      printf("%-8s",temp->name);  	/*输出链表结点的值*/
      temp=temp->nextSta;       	/*移到下一个结点*/
   }
}
/* 将stradd所指的站点插入到链表h中的strafter站点的后面 */
struct station *add_sta(struct station *h,char *stradd, char *strafter)
{
   struct station *p1,*p2;
   p1=h;
   p2=(struct station*)malloc(sizeof(struct station));
   strcpy(p2->name,stradd);
   while(p1!=NULL)
   {
      if(!strcmp(p1->name,strafter))
      {
        p2->nextSta=p1->nextSta;
        p1->nextSta=p2;
        return h;
      }
      else
        p1=p1->nextSta;
   }
   return h;
}

```

## 文件

概念：

所谓“文件”是指一组相关数据的有序集合。

分类：

编码：二进制文件和ASCII码

用户角度：普通文件和设备文件 

### 文件指针

格式：

FILE *指针变量标识符；

`FILE *fp；    `

注：其中FILE应为大写，它实际上是由系统定义的一种结构，该结构中含有文件名、文件状态和文件当前位置等信息。 

文件打开与关闭

打开

```c
FILE *fp；
fp=fopen("file.txt","r"); 
```

打开方式：

```
r 只读	w 写   a 追加

t 文本文件 b 二进制文件

\+ 读和写
```

关闭

关闭格式：

fclose(文件指针)； 

正常完成关闭文件操作时，fclose()返回值为0。如返回非零值则表示有错误发生。 

### 文件的读写操作

#### 字符读函数fgetc(fp)

例:读取文件c1.txt中的内容，并在屏幕上输出。

```c
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void main()
{
  FILE *fp; //文件指针 
  char ch; 
  if((fp=fopen("c1.txt","rt"))==NULL)    //以只读方式打开文件
  {
    printf("\nCannot open file press any key exit!");
    getch();//从键盘上任意输入一个字符 ，但不在屏幕上显示。该行的作用是等待 
    exit(1);//退出 
  }
  ch=fgetc(fp);                       //循环读取文件里面的每一个字符并显示
  while(ch!=EOF)                                //判断文件是否结束
  {
    putchar(ch); //输出字符                               
    ch=fgetc(fp);  //循环读取文件里面的每一个字符并显示
  }
  fclose(fp);       //关闭                            
}
```

例：将当前目录下的某个文本文件的内容输出到屏幕上（文本文件名请通过键盘输入）

```c
/*example10_2.c  读取文件方法  */
#include <stdio.h>
#include <conio.h>
void main()
{
    FILE *fp;
    char ch,name[30],*filename=name;
    printf("please imput filename: ");
    gets(name);
    fp=fopen(filename,"rt");
    if (fp==NULL)
		printf("error\n");
    else
		while((ch=fgetc(fp))!=EOF)
			putchar(ch);
		fclose(fp);
}
```

字符写函数fputc(ch,fp)

```c
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void main()
{
FILE *fp;
char ch;
if((fp=fopen("c2.txt","wt"))==NULL)
{   printf("\nCannot open file!");
    getch();exit(1);
}
ch=getchar(); 
while (ch!='\n') 
{   fputc(ch,fp); 
    ch=getchar();
}
fclose(fp); 
                     
}
```

作业：从键盘输入一行字符，写入C2文件，再把该文件内容读取到屏幕上。（拓展以追加方式at+）

算法：

1. 头文件，主函数
2. 建立文件指针，判断打开是否成功
3. 写入字符到c2文件
4. rewind(fp);
5. 读取c2文件到屏幕

```c
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void main()
{
  FILE *fp;
  char ch;
  if((fp=fopen("c2.txt","wt+"))==NULL)  //以读写方式打开文件
  {
    printf("Cannot open file press any key exit!");
    getch();
    exit(1);
  }
  printf("input a string:\n");
  ch=getchar();                     //循环从键盘输入字符
  while (ch!='\n')                  //遇到回车结束
  {
    fputc(ch,fp);                   //将该字符写入文件
    ch=getchar();
  }
  rewind(fp);                       //将文件内部指针移至文件首
  ch=fgetc(fp);
  while(ch!=EOF)                    //循环读取文件里面每一字符并显示
  {
	putchar(ch);
    ch=fgetc(fp);
  }
  printf("\n");
  fclose(fp);
}
```

#### 字符串读函数

```c
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void main()
{
  FILE *fp;
  char str[11];
  if((fp=fopen("c2.txt","rt"))==NULL)     //以只读方式打开文件
  {
    printf("\nCannot open file press any key exit!");
    getch();
    exit(1);
  }
  fgets(str,3,fp);            //读取字符串，从文件中读取字符，然后按3-1个字符放入数组str
  printf("\n%s\n",str);        //输出数组内容
  fclose(fp);
}
```

例：用字符串读取方式将某个文本的内容输出到屏幕上，并计算有多行，最后输出其行数。

```c
/*example10_4.c  从文件按行读取字符串*/
#include <stdio.h>
void main()
{
    FILE *fp;
    char w[81],name[30],*filename=name;
    int lines=0;
    printf("please imput filename: ");
    gets(name);
    fp=fopen(filename,"r");
    if (fp==NULL)
       printf("File open error\n");
    else
	{
		while (fgets(w,80,fp)!=NULL)
		{
			lines=lines+1;
			printf("%s",w);
		}
		printf("文件的总行数=%d\n",lines);
		fclose(fp);
	 }
}
```



#### 字符串写函数

文件c2.txt中追加一个字符串。

```c
#include<conio.h>
#include<stdlib.h>
#include <stdio.h>
main(){
FILE *fp;
char st[20];
if((fp=fopen("c2.txt","at+"))==NULL)
{   printf("\nCannot open file!");
    getch();
    exit(1);
}
gets(st); 
fputs(st,fp); 
fclose(fp);

} 
```

#### 格式化读写函数

例：现有两个文件file1.txt和file2.txt，文件file1.txt中记录的数据为人的姓名，住址。文件file2.txt中记录的是姓名,联系方式。现在将两个文件中同一个姓名的数据合并放到另一个文件file3.txt中。

file1.txt

```
aa 111
bb 222
cc  333
```

file2.txt

```
ee 444
aa 555
cc 666
```

```c
/*example10_10.c  文件操作应用，将两文件的信息合并 */
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void main()
{
    FILE *fp1,*fp2,*fp3;
    char temp1_1[10],temp1_2[20],temp2_1[10],temp2_2[10];
    if((fp1=fopen("file1.txt","r"))==NULL)  /* 打开第1个文件 */
    {
        printf("文件file1.txt不存在!\n");
        exit(0);
    }
    if((fp2=fopen("file2.txt","r"))==NULL)  /* 打开第2个文件 */
    {
        printf("文件file2.txt不存在!\n");
        exit(0);
    }
    if((fp3=fopen("file3.txt","w"))==NULL)  /* 打开第3个文件 */
    {
        printf("无法建立文件file3.txt!\n");
        exit(0);
    }
    while(!feof(fp1))
    {
        fscanf(fp1,"%s %s",temp1_1,temp1_2);  /* 从第1个文件中读取数据 */
        do
        {
            fscanf(fp2,"%s %s",temp2_1,temp2_2);  /* 从第2个文件中读取数据 */
            if(strcmp(temp1_1,temp2_1)==0)
                fprintf(fp3,"%s, %s, %s\n",temp1_1,temp1_2,temp2_2);  
                                              /* 将数据写入到第3个文件中 */
        }while(!feof(fp2)); 
        rewind(fp2); 
    }
    fclose(fp1);
    fclose(fp2);
    fclose(fp3);
}
```

## 位运算

位运算定义：

二进制由0和1组成，每一个0和1的状态称为位状态。位与位之间的运算称为位运算。 

位运算符及含义：

```
& 按位与
| 按位或
^ 按位异或
~ 按位取反
<< 左移
>> 右移
位运算符中除~以外，均为二目运算符
运算量只能是整型或字符型数据，不能为实型数据
```

例：位运算符使用

```c
#include <stdio.h>
void main()
{
	unsigned char a,b,c,r1,r2,r3,r4;//无符号字符型 
	a=0x23; //0x23十六进制   00100011 
	b=0x45; //01000101 
	c=0x55; //01010101
	r1=a&b; 
	r2=a|b;
	r3=a^b;
	r4=~c;
   /*以十六进制形式输出变量的值*/
	printf("a=%x,b=%x,c=%x\n",a,b,c);   
	printf("a&b=%x\n",r1);
	printf("a|b=%x\n",r2);
	printf("a^b=%x\n",r3);
	printf("~c=%x\n", r4);
	
}

/*
a&b
00100011
01000101
00000001
a|b
00100011
01000101
01100111
a^b
00100011
01000101
01100110
~c
01010101
10101010
*/
```

  作业：在互联网中，计算机都是通过IP地址进行通信的，计算机中的每一个IP地址都用一个32位的unsigned long型变量保存，它分别记录了这台计算机的网络ID和主机ID。请编写程序，从一个正确的IP地址中分离出它的网络ID和主机ID。

分析：ipv4，4个网段，32位，配合子网掩码可以得出网络ID和主机ID

网络ID=IP&子网掩码

主机ID=IP-IP&子网掩码）

```c
/*example11_7.c   位运算实例：模拟分离IP地址*/
#include <stdio.h>
#include <conio.h>
unsigned long getIP();
main()
{
	unsigned int sect1,sect2,sect3,sect4; //无符号整型，分别代表四个网段，从高到低 
	unsigned long IP,netmask,netid,hostid;//无符号长整型，IP地址，子网掩码，网络ID和主机ID 
	printf("请输入一个合理的IP地址：\n");
	IP=getIP(); /*调整getIP()函数，完成模拟生成IP的值*/
	printf("请输入一个合理的子网掩码：\n");
	netmask=getIP();	/*完成模拟生成子网掩码变量netmask的值*/
	printf("---------------------------\n");
	netid=IP&netmask;   	/*获取网络ID*/
	hostid=IP-netid;    	/*获取主机ID*/
	printf("32位IP的值为：%lu\n",IP);
	printf("子网掩码的值: %lu\n",netmask);
	/* 分离网络IP */
	sect1=netid>>24; //网络ID右移24位得到最高位网段 
	sect2=(netid>>16)-((long)sect1<<8); //网络ID右移16位减去最高位网段左移8位 
	sect3=(netid>>8)-((long)sect1<<16)-((long)sect2<<8);
	sect4=0;                    /*完成分离IP地址变量各IP段的值*/
	printf("网络IP：%d.%d.%d.%d\n",sect1,sect2,sect3,sect4);
	printf("主机IP：%lu\n",hostid);
}

unsigned long getIP()
{
	unsigned int ip;
	unsigned int sect1,sect2,sect3,sect4;//无符号整型，分别代表四个网段，从高到低 
	scanf("%d.%d.%d.%d",&sect1,&sect2,&sect3,&sect4); //202.197.96.1 
	ip=sect1;
	ip=ip<<8;//先将ip地址202转换成二进制11001010后左移8位， 
	ip+=sect2; //和左移后的ip地址相加 
	ip=ip<<8;
	ip+=sect3;
	ip=ip<<8;
	ip+=sect4;    
	return ip;
}



```

​                      

```
ip地址
‭11001010‬‭11000101‬‭011000000000‬0001‬   

202      197
‭11001010‬ 00000000
         11000101‬
‭11001010 11000101

子网掩码
11111111111111111111111100000000

 网络ID=ip地址&子网掩码                                                     
‭11001010‬‭11000101‬‭011000000000‬0001‬ 
11111111111111111111111100000000
--------------------------------
‭11001010‬‭11000101‬‭0110000000000000
sect1=netid>>24 网络ID右移24位得到最高位网段
‭00000000000000000000000011001010‬‭
```

## 期末复习

1.  简单的程序，求正方形的周长和面积。
2. 数组的基础知识，假设从键盘上输入5个数，求平均分是多少？
3. 数组的高级应用，尝试输出杨辉三角形
4.  编写程序实现，输出以下图形（p100 ）。
5.  用冒泡算法对180，150，170，160，120个数进行从小到大排列
6.  定义一个函数，用指针实现两个数字的交换
7.  读取（写入）文件c1.txt中的内容（hello world!），并在屏幕上输出。
8.  将输入的大写字符串转换成小写输出
9.  用字符指针实现求字符串长度

