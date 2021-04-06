<?php  //常量
    define('PAI','3.14');//define('常量名','值');
    define('R','5',true);//define('常量名','值','是否区分大小写');
    echo '圆周率=',PAI;
    echo '半径=',R;
    echo '半径=',r;
    echo '<br>';

    const R=6; //const 是关键字，它可以是表达式
    const P=2*R;
    echo 'P=',P;