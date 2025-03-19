<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Validation</title>
</head>
<body>
    <h2>Check if Email is Valid</h2>

    <!-- Form for email input -->
    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
        <label for="email">Enter your email:</label>
        <input type="text" id="email" name="email" value="<?php echo isset($_POST['email']) ? htmlspecialchars($_POST['email']) : ''; ?>" required>
        <input type="submit" value="Check">
    </form>

    <?php
    // Enable error reporting for debugging
    ini_set('display_errors', 1);
    error_reporting(E_ALL);

    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        // Get and sanitize the email input
        $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);

        // Validate email using filter_var
        if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
            echo "<p style='color: green;'>The email <strong>" . htmlspecialchars($email) . "</strong> is valid!</p>";
        } else {
            echo "<p style='color: red;'>The email <strong>" . htmlspecialchars($email) . "</strong> is invalid.</p>";
        }
    }
    ?>
</body>
</html>

