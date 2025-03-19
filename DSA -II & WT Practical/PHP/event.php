<?php
$connect=pg_connect("host=localhost dbname=sri port=5432 user=postgres password=postgres");
if($connect)
echo "connection ok";
else
echo "error";
$t='birthday';
$s=' notwor';
$result=pg_query($connect,"update com set status='$s' from event1,eve_com where event1.eno=eve_com.en and com.cno=eve_com.cn and title='$t';");
if($result)
echo"record updted";
?>
