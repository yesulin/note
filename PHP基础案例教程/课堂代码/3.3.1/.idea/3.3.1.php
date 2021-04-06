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