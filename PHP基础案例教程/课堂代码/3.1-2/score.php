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