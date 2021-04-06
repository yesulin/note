<?php
$name = 'PHP';
$heredoc = <<<EOD
<ul>
  <li>$name 是世界上最好的语言！</li>
  <li>$name is the best programming language in the world !</li>
</ul>
EOD;
echo $heredoc;

$nowdoc = <<<'EOD'
<ul>
  <li>$name 是世界上最好的语言！</li>
  <li>$name is the best programming language in the world !</li>
</ul>
EOD;
echo $nowdoc;
?>


