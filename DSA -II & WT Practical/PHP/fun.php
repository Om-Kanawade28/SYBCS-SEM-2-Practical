<?php
$a=$_GET['n1'];
$b=$_GET['n2'];
$ch=$_GET['a1'];
switch($ch)
{
  case 1 : mod($a, $b);
  break;
  case 2 : power($a, $b);
  break;
  case 3 : sumN($a);
  break;
  case 4 : fact($b);
  break;
}
 Function mod($a, $b)
{
 $c=$a%$b;
 echo "mod of no =";
 echo $c;
}
function power($a, $b)
{
  $finalnum=1;
  $n1=$b;
  while($n1>0)
  {
  $finalnum=$finalnum * $a;
  $n1--;
  }
 echo"$a raised to the power $b= $finalnum\n";
}
Function sumN($a)
{
 $num=$a;
 $n=$num;
 $sum=0;
 while($n>0)
 {
  $sum=$sum+$n;
  $n--;
 }
echo"sum of $num number is = $sum";
}
function fact($b)
{
 $num=$b;
 $fact=1;
 for($x=$num; $x>=1; $x--)
  {
   $fact=$fact*$x;
 }
 echo"factorial of $num= $fact";
}

?>
