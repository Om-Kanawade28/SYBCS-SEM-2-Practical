<?php
$a=$_GET["s"];
$ch=$_GET["ch"];
echo $a;
switch($ch)
{
case '1':length($a);
break;
case '2':vowel($a);
break;
case '3':lowercase($a);
break;
case '4':padding($a);
break;
/*case 5:whitespace($s);
break;
case 6:reverse($s);
break;*/
/*default:echo"ENTER VALID CHOICE!!!";
break;*/
}
function length($a)
{
$s=str_split($a);
 for($i=0;$i<count($s);$i++)
{
$cnt++;
}
echo "LENGTH OF STRING $a:".$cnt;
}

function vowels($a)
{
$v=0;
$s=str_split($a);
for($i=0;$i<count($s);$i++)
{
if($s[$i]=="a"||$s[$i]=="e"||$s[$i]=="u"||$s[$i]=="i"||$s[$i]=="o")
$v++;
}
echo"COUNT VOWELS.$v";
}
/*
function lowercase($a)
{
$b=strtolower($a);
echo $b;
$c=ucword($b);
echo $c;
}
*/
function wspace($a)
{
echo trim($a);
}
function pad($s)
{
echo"PADDING:".str_pad($a,6,STR_PAD_BOTH)."***"."\n";
}
?>
