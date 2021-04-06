<?php
for ($i = 1, $sum = 0; $i <= 100; ++$i) {
    if ($i % 2 == 0) {      // 若为偶数，则不累加
        continue;           // 结束本次循环
    }
    $sum += $i;             // 累加奇数
}
echo '$sum = ' . $sum;