#Ecanep de equoipos activos en una subred
#
#Determinando gateway
$subred= (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-host "== Determinando tu gateway ..."
Write-Host "Tu Gateway: $subred"
#
# Determinando rango de la subred
#
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host "== Deteminando tu rango de subred ..."
echo $rango
#
## Determinando si $rango termina en "."
## En ocasiones el rango de subred no termina en punto, necesitamos forzarlo 
#
$punto = $rango.EndsWith('.')
if ($punto -like "False"){
    $rango = $rango + '.' #Agregamos el punto en caso de que no estuviera.
}
#
## Creamos un array de 254 numeros (1 a 254) y se almacenan
## en una variable que se llama $rango_ip
#
$rango_ip = @(1..254)
#
## Generamos bucle foreach para validar hosts activos en nuestra subred
#
Write-Output ""
Write-Host "-- subred Actual: "
Write-Host "Escaneando: " -NoNewline; Write-Host $rango -ForegroundColor Red
Write-Output ""

foreach( $r in $rango_ip){
    $actual = $rango + $r # se genera direccion ip
    $responde = Test-Connection $actual -Quiet -Count 1 # Validamos conexion contra ip en $actual
    if ( $responde -eq "True"){
        Write-Output ""
        Write-Host "Host responde : " -NoNewLine; Write-Host $actual -ForegroundColor Green
    }
}
#
## Fin del script
#