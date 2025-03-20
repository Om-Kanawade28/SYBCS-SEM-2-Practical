<?php
    $str = $_GET['input_string'];
    $op = $_GET['operation'];
        
    function countVowels($str) {
        $vowels = ['a', 'e', 'i', 'o', 'u'];
        $str = strtolower($str);
        $count = 0;
        for ($i = 0; isset($str[$i]); $i++) {
            if (in_array($str[$i], $vowels)) {
                $count++;
            }
        }
        return $count;
    }

    function trimSpaces($str) {
        return ltrim($str);
    }

    function reverseString($str) {
        return strrev($str);
    }
    echo "<h3>Result: ";
        if ($op == "vowel_count") echo countVowels($str);
        elseif ($op == "trim_spaces") echo trimSpaces($str);
        elseif ($op == "reverse") echo reverseString($str);
        echo "</h3>";
?>