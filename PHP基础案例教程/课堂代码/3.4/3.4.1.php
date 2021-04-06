<?php
$url = 'C:\web\apache2.4\htdocs\cat.jpg';
$pos=strrpos($url,'\\');//转义字符，求最后一次出现的位置

echo $pos,'<br>';
echo substr($url,$pos+1),'<br>';
echo substr($url,0,23),'<br>';//substr(字符串，起始位置，长度)；
//作业：要求截取htdocs
echo substr($url,17,6);
echo '<br>';

$tel='18810881888';
$len=4;
$replace=str_repeat('*',$len);
echo substr_replace($tel,$replace,3,$len);
echo '<br>';

$str='    今天 天气 真好！    ';
echo '原字符串:'.$str.'<br>';
echo '去空白后的字符串:'.trim($str);
echo '<br>';

if(strcmp('ye_PHP','yePHP')){
    echo '不成立';
}else
    echo '成立';
echo '<br>';

$str1='abcd';
$str2='php程序设计基础教程';
echo strlen($str1),'<br>';
echo strlen($str2),'<br>';//一个中文当前三个英文字符
echo mb_strlen($str2,'UTF-8');