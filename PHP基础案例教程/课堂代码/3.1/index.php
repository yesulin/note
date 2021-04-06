<?php
    $row = 10;    // 行数
    $col = 10;    // 列数
?>
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>国际象棋棋盘</title>
    <style>
      table{border:1px solid #000;border-collapse:collapse}
      td{width:20px;height:20px}
      .black{background:#000}
    </style>
  </head>
  <body>
    <table>
    <?php
        for ($i = 0; $i < $row; ++$i) { // 行数
            echo '<tr>';
            for ($j = 0; $j < $col; ++$j) { // 列数
                if (($i + $j) % 2) { // if (($i + $j) % 2!=0)
                    echo '<td></td>';//不等0
                } else {
                    echo '<td class="black"></td>'; //等于0
                }
            }
            echo '</tr>';
        }
    ?>
    </table>
  </body>
</html>