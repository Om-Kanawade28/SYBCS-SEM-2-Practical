<?php
    $n1 = $_GET['n1'];
    $n2 = $_GET['n2'];
    $operation = $_GET['operation'];


    function mul($n, $m){
        return $n * $m;
    }
    function div($n, $m){
        return $n / $m;
    }

    echo "<h3>Result: ";
    if ($operation == "mul") echo mul($n1, $n2);
    elseif ($operation == "div") echo div($n1, $n2);
    else echo "Invalid selection!";
    echo "</h3>";
?>