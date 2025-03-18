<?php
$num1 = $_GET['n1'];
$num2 = $_GET['n2'];
// a.find mod of the two numbers
function mod($num1, $num2){
    return $num1 % $num2;
}
$mod = mod($num1, $num2);
echo "mod of the two numbers:-$mod";
echo "<br>";
//b.find the power of first number to second number
function power($num1, $num2){
    return pow($num1, $num2);
}
$power = power($num1, $num2);
echo "power of the first number to second number:-$power";  
?>