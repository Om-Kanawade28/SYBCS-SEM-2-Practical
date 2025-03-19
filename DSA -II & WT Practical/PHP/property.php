<?php
$connect=pg_connect("host=localhost dbname=sri port=5432 user=postgres password=postgres");
if($connect)
echo "connection ok";
else
echo "error";
$t='abc';

$result=pg_query($connect,"select pno, description, area from property, owner where owner.oname=property.name and oname='$t';");
while($row=pg_fetch_row($result))
{

echo"$row[0] $row[1]";

}
?>
