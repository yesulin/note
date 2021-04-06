<?php
function test(){
    global $sum; //global是全局变量
    $sum=36;
    return $sum;
}
$sum=0;
echo test();
echo '<br>'.$sum;