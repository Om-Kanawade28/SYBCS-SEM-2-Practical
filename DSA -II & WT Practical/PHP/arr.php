<?php
$array = $_GET['a'];
echo $array;
$t = preg_split("/ /", $array);
rsort($t);

$newarray=array_slice($t,0,4);
$highavg=array_sum($newarray);
echo"average of first 5 high temp is:<br>";
print_r($highavg/5);
echo"&degC";
echo"<br>";

$newarray1=array_slice($t,5,9);
$lowavg=array_sum($newarray1);
echo"average of first 5 low temp is:<br>";
print_r($lowavg/5);
echo"&degC";
echo"<br>";
?>
