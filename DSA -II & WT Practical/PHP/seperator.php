<?php
$a=$_GET['n'];
$b=$_GET['select'];
echo $a;
print_r(preg_split("/$b/",$a));
echo"<br>";
print_r(preg_replace($b,'world',$a));
//echo"<br>";
//function last($a)
//{
//echo last($a);
//}
//last($a);
?>
