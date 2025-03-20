<?php
// PostgreSQL Database Connection
$conn = pg_connect("host=localhost port=5432 dbname=your_database user=your_user password=your_password");

// Check connection
if (!$conn) {
    die("Database connection failed!");
}

// SQL queries to create tables
$queries = [
    "CREATE TABLE Event (
        eno INT PRIMARY KEY,
        title VARCHAR(255),
        date DATE
    );",

    "CREATE TABLE Committee (
        cno INT PRIMARY KEY,
        name VARCHAR(255),
        head VARCHAR(255),
        from_time TIME,
        to_time TIME,
        status VARCHAR(50) DEFAULT 'Pending'
    );",

    "CREATE TABLE Event_Committee (
        eno INT REFERENCES Event(eno),
        cno INT REFERENCES Committee(cno),
        PRIMARY KEY (eno, cno)
    );"
];

foreach ($queries as $query) {
    $result = pg_query($conn, $query);
    if (!$result) {
        echo "Error creating table: " . pg_last_error($conn) . "<br>";
    }
}

// Insert dummy data
$insert_queries = [
    "INSERT INTO Event (title, date) VALUES ('Hackathon', '2025-04-01')",
    "INSERT INTO Event (title, date) VALUES ('Tech Meetup', '2025-05-01')",
    "INSERT INTO Committee (name, head, from_time, to_time, status) VALUES 
        ('Planning Committee', 'Alice', '09:00', '12:00', 'Pending'),
        ('Logistics Committee', 'Bob', '10:00', '14:00', 'Pending')
    ON CONFLICT (name) DO NOTHING;",
    "INSERT INTO Event_Committee (eno, cno) VALUES (1, 1), (2, 2) ON CONFLICT DO NOTHING;"
];

// Execute insert queries
foreach ($insert_queries as $query) {
    $result = pg_query($conn, $query);
    if (!$result) {
        echo "Error inserting data: " . pg_last_error($conn) . "<br>";
    }
}

echo "Tables created and dummy data inserted successfully!";

// Close connection
pg_close($conn);
?>
