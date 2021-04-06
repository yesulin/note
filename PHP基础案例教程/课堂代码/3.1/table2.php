<!doctype html>
<html>
<head>
<title>九九乘法表</title>
<style>
  table{border:2px solid #CFCFCF;width:500px;border-collapse:collapse;}
  td,th{border:2px solid #CFCFCF;}
  th{height:40px;}
  .white{background:#FFF;}
  .gray{background:#EEE;}
  .title{background:#7D8BA5;}
</style>
</head>
<body>
<?php
echo '<table>';
for ($i = 1; $i <= 9; ++$i) {       // 九九乘法表的层数
    echo '<tr>';
    for ($j = 1; $j <= $i; ++$j) {  // 单元格个数
        //echo '<td></td>';
        echo "<td>{$j}×{$i}=" . $j * $i . '</td>';
    }
    echo '</tr>';
}
echo '</table>';
?>
</body>
</html>