# raspberry_radar
radar con sensor HC-SR04 para niños 

Para implementar un radar usando el sensor de distancia HC-SR04 en una Raspberry Pi Zero, 
autilizaremos una raspberrypi zero y un HC-SR04 los pines GPIO 23 (Trigger) y 24 (Echo).
El sensor HC-SR04 funciona enviando un pulso ultrasónico desde el pin Trigger, y luego mide el tiempo que tarda en recibir el eco en el pin Echo. A partir de ese tiempo, puedes calcular la distancia del objeto.

Implementamos un script en Python para controlar el HC-SR04 y calcular la distancia, además de realizar un escaneo en un rango de 0 a 260 grados con el servo motor:

Descarga el script de radar con HC-SR04 y servo motor.

Necesitamos una resistencia 1k Ohm y 2k Ohm para no danar la rpi. 

project/
│
├── app.py                  # Archivo principal para iniciar la aplicación Flask
├── routes/
│   ├── __init__.py         # Inicializa el módulo de rutas
│   ├── main.py             # Rutas principales
│   ├── api.py              # API REST para obtener datos del sensor
├── services/
│   ├── __init__.py         # Inicializa el módulo de servicios
│   ├── sensor.py           # Función para manejar el HC-SR04
│   ├── alerts.py           # Gestión de alertas según la distancia
├── templates/
│   ├── index.html          # Página principal
│   ├── alert.html          # Página para alertas
├── static/
│   ├── js/
│   │   ├── chart.js        # Gráfica en tiempo real
│   ├── css/
│       ├── style.css       # Estilos CSS
└── requirements.txt        # Dependencias del proyecto
