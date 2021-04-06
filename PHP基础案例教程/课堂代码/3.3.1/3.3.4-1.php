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