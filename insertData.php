<?php

$GLOBALS["conexion"] = new PDO('mysql:host=bora.teramont.net:3306; dbname=Pruebas2', 'u1967_8eIJQgJtzE', '^UCbjpk66l6WuvLcAfw@r5!+');
$GLOBALS["conexion"] -> exec("set names utf8");

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header("Access-Control-Allow-Headers: X-Requested-With");

$json = file_get_contents('php://input');
$data = json_decode($json);
$TEMPERATURA = $data->TEMPERATURA;
$ENCENDIDO = $data->ENCENDIDO;

$sq = $conexion -> prepare("INSERT INTO Registro(TEMPERATURA, ENCENDIDO) VALUES ('$TEMPERATURA', '$ENCENDIDO')");
$sq -> execute();

echo json_encode("ok");

?>
