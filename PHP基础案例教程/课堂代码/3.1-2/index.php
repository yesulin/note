<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>函数中变量的作用域</title>
    <style>
      h1{font-size:18px;text-align:center}
      .box{width:350px;border:2px dotted #FE0D0B;padding:0 10px 10px 10px;margin:20px auto}
    </style>
  </head>
  <body>
    <div class="box">
    <h1>函数中变量的作用域</h1>
    <?php
        function getArea()
        {
            global $radius;
            // $radius = $GLOBALS['radius'];
            $area = round(pi() * pow($radius, 2), 2); //round(x,2)小数点后面保留两位，pi()是3.1415，pow（）求幂运算
            return $area;
        }
        $radius = 4;    // 圆的半径
        echo '圆的面积：' . getArea();
        
    ?>
    </div>
  </body>
</html>