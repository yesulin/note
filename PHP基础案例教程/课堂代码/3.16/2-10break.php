<?php
for($i=1;$i<=5;$i++){
    echo '$i='.$i;
    if($i==3){
        break;//跳出整个循环
    }
}
echo 'ending';