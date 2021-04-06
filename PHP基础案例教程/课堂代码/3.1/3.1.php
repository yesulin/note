<!doctype html>
<html>
<head>
    <title>自定义函数</title>
    <style>
        table{border:2px solid #CFCFCF;width:500px;border-collapse:collapse;}
        td,th{border:2px solid #CFCFCF;}
        th,td{height:40px;}
    </style>
</head>
<body>
<?php

function generate_table($row, $col) //自定义函数
{
    $html = '<table>';
    for ($i = 1; $i <= $row; ++$i) {
        $html .= '<tr>';
        for ($j = 1; $j <= $col; ++$j) {
            $html .= '<td></td>';
        }
        $html .= '</tr>';
    }
    return $html.'</table>';
}
echo generate_table(4, 8);
echo '<br>';
echo generate_table(10,10);


?>
</body>
</html>