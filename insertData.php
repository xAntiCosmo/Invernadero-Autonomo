<?php

$GLOBALS["conexion"] = new PDO('mysql:host=bora.teramont.net:3306; dbname=s1967_Pruebas', 'u1967_8eIJQgJtzE', '^UCbjpk66l6WuvLcAfw@r5!+');
$GLOBALS["conexion"] -> exec("set names utf8");

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header("Access-Control-Allow-Headers: X-Requested-With");

$json = file_get_contents('php://input');
$data = json_decode($json);
$id_registro = $data->id_registro;
$numero = $data->numero;

$sq = $conexion -> prepare("INSERT INTO RandNums(ID,Numero_Random) VALUES ('$id_registro','$numero')");
$sq -> execute();

echo json_encode("ok");

?>