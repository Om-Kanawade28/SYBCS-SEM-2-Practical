<?php
    $n1 = $_GET['n1'];
    $n2 = $_GET['n2'];
    $operation = $_GET['operation'];


    function add($n, $m){
        return $n + $m;
    }
    function sub($n, $m){
        return $n - $m;
    }

    echo "<h3>Result: ";
    if ($operation == "add") echo add($n1, $n2);
    elseif ($operation == "sub") echo sub($n1, $n2);
    else echo "Invalid selection!";
    echo "</h3>";
?>
        