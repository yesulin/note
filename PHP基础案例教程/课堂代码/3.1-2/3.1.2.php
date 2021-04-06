<?php
//function hello(){ //无参数 ，函数定义
//    echo 'hello world!';
//}
//hello(); //函数调用
//echo '<br>';
//
////按值传递
//function add($a,$b){ //有参数
//    $a=$a+$b;
//    return $a;
//}
//
//echo add(4,5);
//echo '<br>';
//$x=3;
//$y=4;
//echo add($x,$y);
//echo '<br>';

//引用传参
//function extra(&$str){
//    $str.=' and some extra ';
//}
//$var='food';
//extra($var);
//echo $var;
//
////设置参数的默认值
//function say($p,$con='你真帅！'){
//    return "$p $con";
//}
//echo say('小王','你好漂亮!');

//指定参数类型
function sum1(int $a,int $b){ // 这种方式支持php7.0以上
    return $a+$b;
}
echo sum1(4.4,5.5);

















