<?php
$item=$_GET['n1'];
$p=$_GET['a1'];
echo $item."<br>";
echo $p;

$prod=array("sugar", "oil", "rice", "pulses");
switch($p)
{
case 'a': array_push($prod, $item);
print_r($prod);
break;
}
?>


