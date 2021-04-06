<?php //引用赋值
$number=10; // =名字赋值号（不是等号），作用是将右侧的值传递给左边的变量
$result=&$number;  //&是引用赋值，$number为10，$result为100
$number=100; //$number为100
echo '$number=',$number;
echo '<br>';
echo '$result=',$result;