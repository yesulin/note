<?php
//举例：对一个学生的考试成绩进行等级的划分，若分数在90~100分为优秀，
//分数在80~90分为优秀为良好，分数在70~80分为中等，
//分数在60~70分为及格，分数小于60则为不及格。

$score=72;

switch((int)($score/10)){
    case 10:
    case 9:
        echo '优';break;
    case 8:
        echo '良';break;
    case 7:
        echo '一般';break;
    case 6:
        echo '及格';break;
    default:
        echo '不及格';

}

