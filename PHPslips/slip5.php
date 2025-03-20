<?php
    $big = $_GET['big_string'];
    $small = $_GET['small_string'];
    $operation = $_GET['operation'];
    $n = $_GET['n'] ?? 0;

    function startsWith($big, $small) {
        return strpos($big, $small) === 0;
    }

    function findPosition($big, $small) {
        $pos = strpos($big, $small);
        return $pos;
        // return ($pos !== false) ? $pos + 1 : "Not found";
    }

    function compareFirstN($big, $small, $n) {
        return strncasecmp($big, $small, $n) == 0;
    }

    echo "<h3>Result: ";
    if ($operation == "starts_with") echo startsWith($big, $small) ? "Yes" : "No";
    elseif ($operation == "position") echo findPosition($big, $small);
    elseif ($operation == "compare") echo compareFirstN($big, $small, $n) ? "Match" : "No Match";
    else echo "Invalid selection!";
    echo "</h3>";
?>
        