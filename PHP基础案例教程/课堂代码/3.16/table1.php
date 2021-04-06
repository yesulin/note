<!doctype html>
<html>
<head>
<title>x行y列的表格</title>
<style>
  table{border:2px solid #CFCFCF;width:500px;border-collapse:collapse;}
  td,th{border:2px solid #CFCFCF;}
  th{background:grey}  /*标题栏颜色*/
  th,tr{height:40px;}
  .white{background:#FFF;}
  .gray{background:#EEE;}
  .title{background:#7D8BA5;}
</style>
</head>
<body>
<?php
// 自定义行和列的数值
$row = 5;
$col = 10;
echo '<table>';

// 生成表格标题行
echo '<tr>';
for ($i = 1; $i <= $col; ++$i) {
    echo '<th></th>';
}
echo '</tr>';

for ($i = 1; $i <= $row; ++$i) {        // 控制表格的行
    //echo '<tr>';
	
	$color = ($i % 2 == 0) ? 'gray' : 'white';
	echo '<tr class="' . $color . '">';
	
    for ($j = 1; $j <= $col; ++$j) {    // 控制表格的列
        echo '<td></td>';
    }
    echo '</tr>';
}
echo '</table>';
?>
</body>
</html>