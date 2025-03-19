<?php

    function generateGreeting($name , $college , $message) {
        return "Hello $name from $college! $message";
    }

    echo "<h3>" . generateGreeting($_GET['name'] ? : "Miss/Mr", $_GET['college'] ? : "Sangamner College" , $_GET['message'] ? : "Welcome!") . "</h3>";
 
?>