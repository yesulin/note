<?php
function sum($a,$b){
    return $a+$b;
}
call_user_func('sum',4,5);//回调函数，可以把函数当成参数