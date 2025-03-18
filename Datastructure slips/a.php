<?php
$num1 = $_GET('n1');
$num2 = $_GET('n2');
// a. find the sum of first n numbers(considering first number as n)
$sum = 0;
for($i = 1;$i <= $num1;$i++){
    $sum = $sum + $i;
}
echo "the sum of first n numbers(considering first number as n):-$sum"
?>