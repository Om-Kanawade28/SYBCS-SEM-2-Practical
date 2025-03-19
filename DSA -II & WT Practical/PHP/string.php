<?php
$a=$_GET['n1'];
$b=$_GET['n2'];
function appear($a,$b)
{
if(strstr($a,$b))
{
echo "$a is present in $b";
}
else
echo "$a is not present in $b";
}
function posititon($a,$b)
{
echo "<br>"."$b is present in $a at".strpos($a,$b)."position"."<br>";
}
function compare($a,$b)
{
if($a==$b)
{
echo"<br>both string are equal";
}
else
echo"<br>"both string are not equal";
}
appear($a,$b);
position($a,$b);
compare($a,$b);
?>
