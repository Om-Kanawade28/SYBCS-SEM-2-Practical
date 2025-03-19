<?php
$file = "sample.txt"; // File to read

if (file_exists($file)) {
    $content = file_get_contents($file);
    $size = filesize($file);

    echo "<h2>File Content:</h2><p>$content</p>";
    echo "<p>File Size: $size bytes</p>";
} else {
    echo "<p>File not found!</p>";
}
?>
