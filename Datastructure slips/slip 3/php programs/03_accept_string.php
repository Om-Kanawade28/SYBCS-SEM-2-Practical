<?php
$string = $_GET['string'];
function length($a)
{
$s=str_split($a);
$cnt=count($s);
echo "length of $a =>".$cnt;
}
$length = length($string);
echo" length of string is $length";
echo "<br>";
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
$countv = countv($string);
echo" No of vowels in string is $countv";
echo "<br>";

?>