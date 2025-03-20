<?php
        $inputString = $_GET['input_string'];
        $operation = $_GET['operation'];

        function findLength($str) {
            $count = 0;
            while (isset($str[$count])) {
                $count++;
            }
            return $count;
        }

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

        function convertToTitleCase($str) {
            return ucwords(strtolower($str));
        }

        echo "<h3>Result: ";
        if ($operation == "length") {
            echo findLength($inputString);
        } elseif ($operation == "vowel_count") {
            echo countVowels($inputString);
        } elseif ($operation == "convert_case") {
            echo convertToTitleCase($inputString);
        }
        echo "</h3>";
    ?>