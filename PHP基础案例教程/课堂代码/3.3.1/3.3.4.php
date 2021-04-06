<?php
$c=100; //外部变量
$sum=function($a,$b) use($c){//匿名函数，使用use关键字，访问外部变量
    return $a+$b+$c;
};
echo $sum(100,200);