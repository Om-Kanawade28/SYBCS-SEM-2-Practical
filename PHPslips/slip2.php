<?php

$n1 = $_GET['n1'];
$n2 = $_GET['n2'];

// a.

function sumOfN($n){
    $sum = 0;
    for($i=1; $i <= $n; $i++){
        $sum += $i;
    }
    return $sum;
}

function fact($n){
    if($n == 0){
        return 1;
    }
    return $n* fact($n -1);
}

echo "sum of first $n1 numbers is ". sumOfN($n1);
echo "<br>";

echo "factorial of  $n1 no. is ". fact($n2);

?>