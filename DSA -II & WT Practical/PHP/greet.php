<?php
function generateGreeting($student_name, $college_name, $greeting_message)
{
    // Check if student name is empty
    if ($student_name == '') {
        return $greeting_message . " Onkar from " . $college_name;
    } else {
        return $greeting_message . " " . $student_name . " from " . $college_name;
    }
}
// Get input from the form
$student_name = isset($_GET['student_name']) ?$_GET['student_name'] : null;
$college_name = isset($_GET['college_name']) ? $_GET['college_name'] : null;
$greeting_message = isset($_GET['greeting_message']) ?$_GET['greeting_message'] : null;

// Generate the greeting message
$greeting = generateGreeting($student_name, $college_name, $greeting_message);

// Display the result
echo "<h2>Your Greeting Message: </h2>";
echo "<p>$greeting</p>";
?>


