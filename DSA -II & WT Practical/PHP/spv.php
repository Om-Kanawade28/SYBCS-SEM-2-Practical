<?php
$a=$_GET['n1'];
$b=$_GET['n2'];
echo $a;
$ch=$_GET['a1'];
echo $ch;

switch($ch)
{
case 1:add($a, $b);       
break;
case 2:sub($a,$b);   
break;
case 3:mul($a,$b);    
break;
case 4:div($a,$b);      
break;
}
function add($a, $b)
{
$c=$a+$b;
echo "Addition of no= ".$c;
}

?>
