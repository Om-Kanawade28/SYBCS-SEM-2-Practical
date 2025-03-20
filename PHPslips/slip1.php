<?php
$num1 = $_GET['n1'];
$num2 = $_GET['n2'];

//a. mod
function mod($num1, $num2){
    return $num1 % $num2;
}

$mod = mod($num1, $num2);
echo "mod of the 2 numbers are- $mod";
echo "<br>";

//b. power of first raise to second
function power($num1, $num2){
    return pow($num1, $num2);
}

$power = power($num1, $num2);
echo "power of the first number to second number:- $power";
?>