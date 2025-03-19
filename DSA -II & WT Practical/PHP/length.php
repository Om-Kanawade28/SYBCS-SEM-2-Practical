<?php
$a=$_GET["t1"];
$ch=$_GET["op"];
echo $a;
switch($ch)
{
case '1' : length($a);
break;
case '2' : countv($a);
break;
case '3' : lowercase($a);
break;
case '4' : rmwhite($a);
break;
case '5' : reverse($a);
break;
}
function length($a)
{
$s=str_split($a);
$cnt=count($s);
echo "length of $a =>".$cnt;
}

function countv($a)
{
$v=0;
$s=str_split($a);
for($i=0;$i<count($s);$i++)
{
if($s[$i]=="a"||$s[$i]=="e"||$s[$i]=="u"||$s[$i]=="i"||$s[$i]=="o")
$v++;
}
echo "No of vowels.$v";
}

function lowercase($a)
{
$b=strtolower($a);
echo $b;
//$c=ucword($b);
//echo $c;
}
function rmwhite($a)
{
echo trim($a);
}
function reverse($a)
{
$b=strrev($a);
echo "reverse of enter string =>";
echo $b;
} 
?>
