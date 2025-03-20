<!DOCTYPE html>
<html lang="en">
<head>
    <title>Weather Report</title>
</head>
<body>
    <h2>Spring Month Weather Report</h2>
    <?php
    $temps = [20, 22, 19, 21, 23, 25, 26, 28, 29, 30, 27, 24, 22, 21, 20, 18, 19, 23, 25, 28, 30, 32, 33, 35, 31, 29, 27, 26, 24, 22];

    $avgTemp = array_sum($temps) / count($temps);

    sort($temps);
    $coolest = array_slice($temps, 0, 5);
    $warmest = array_slice($temps, -5);

    echo "<p>Average High Temperature: " . round($avgTemp, 1) . "&deg;C</p>";
    echo "<p>Five Coolest Days: " . implode(", ", $coolest) . "&deg;C</p>";
    echo "<p>Five Warmest Days: " . implode(", ", $warmest) . "&deg;C</p>";
    ?>
</body>
</html>
