<?php
function generateGreeting($student_name,$college_name,$greeting_meassage)
{
    if($student_name == ''){
        return $greeting_meassage."Onkar from".$college_name;
    }else{
        return $greeting_meassage." ".$student_name." from ".$college_name;
    }
}

//Get input from the form
$student_name = insset($_GET['student_name']) ?//