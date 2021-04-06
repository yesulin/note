<?php
//求0-4的和 0+1 +2 +3 +4
$i = $sum = 0;      // 初始化变量
while ($i < 5) {    // 循环条件
    echo ' $i=' . $i;
    $sum += $i;
    ++$i;           // 设置循环出口
}
echo '<br> $sum=' . $sum;