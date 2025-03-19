<?php
$a=$_GET['n1'];
$b=$_GET['n2'];
echo $a;
echo"<br>";
echo $b;
echo"<br>";
appear($a, $b);
position($a, $b);
compare($a, $b);
function appear($a, $b)
{
  if(strstr($a, $b))
  { echo"$a is present in $b";
  }
  else
    echo"$a is not present in $b";
}

function position($a, $b)
{
 echo"<br>"."$b is present in $a at". strpos($a, $b) ."position"."<br>";
}
function compare($a, $b)
{
  if($a==$b)
  {
    echo"both strings are equal";
  }
  else
    echo"both strings are not equal";
}
?>
