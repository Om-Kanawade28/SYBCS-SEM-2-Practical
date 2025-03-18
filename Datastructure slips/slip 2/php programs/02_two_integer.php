<?php
$num1 = $_GET['n1'];
$num2 = $_GET['n2'];
//a. find the sum of first n numbers(considering first number as n)
function sum_nth_number($num1){
    $sum = 0;
    for($i = 1;$i <= $num1;$i++){
        $sum = $sum + $i;
    }
    return $sum;
}
$sum = sum_nth_number($num1);
echo "the sum of first n numbers(considering first number as n):-$sum";
echo "<br>";
//b.find the factorial of the second number
function factorial($num2){
    $fact = 1;
    for($i = 1;$i <= $num2;$i++){
        $fact = $fact * $i;
    }
    return $fact;
}
$fact = factorial($num2);
echo "the factorial of the second number:-$fact";
echo "<br>";
 
?>