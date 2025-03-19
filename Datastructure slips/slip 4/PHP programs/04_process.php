<?php
$string = $_GET['string'];
$choice = $_GET['choice'];
switch($choice){
    case 1:
         counts($string);
    case 2:
        $rev = strrev($string);
        echo "Your reverse String:-$rev";
    case 3:
        echo trim($string);
    default:
       exit(0);

}
function counts($string){
    $s = str_split($string);
    $sum = 0;
    for($i = 0;$i < count($s);$i++){
        if($s[$i] == 'o' || $s[$i] == 'e' || $s[$i] == 'u' || $s[$i] == 'a' || $s[$i] == 'i'){
            $sum++;
        }
    }
    echo "Total Length of the String:-$sum";
}
?>