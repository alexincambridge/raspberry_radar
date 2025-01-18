# raspberry_radar
radar con sensor HC-SR04 para niños 

Para implementar un radar usando el sensor de distancia HC-SR04 en una Raspberry Pi Zero, 
autilizaremos una raspberrypi zero y un HC-SR04 los pines GPIO 23 (Trigger) y 24 (Echo).
El sensor HC-SR04 funciona enviando un pulso ultrasónico desde el pin Trigger, y luego mide el tiempo que tarda en recibir el eco en el pin Echo. A partir de ese tiempo, puedes calcular la distancia del objeto.

Implementamos un script en Python para controlar el HC-SR04 y calcular la distancia, además de realizar un escaneo en un rango de 0 a 260 grados con el servo motor:

Descarga el script de radar con HC-SR04 y servo motor.

Necesitamos una resistencia 1k Ohm y 2k Ohm para no danar la rpi. 

