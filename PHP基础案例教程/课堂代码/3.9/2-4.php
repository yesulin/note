<?php
$number=100;
echo '$number=',$number; // $number=100 单引号，原样输出
echo '<br>';

echo "$number=",$number; //100=100 双引号，类似代替的功能
echo '<br>';

echo ' \' '; //转义字符
echo '<br>';

$str='方向的';
echo "PHP{$str}程序员";