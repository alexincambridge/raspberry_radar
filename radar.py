import RPi.GPIO as GPIO
import time

# Configuración de pines GPIO
TRIGGER_PIN = 23
ECHO_PIN = 24
SERVO_PIN = 17

# Configurar la numeración de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configuración del PWM para el servo
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz para servo
pwm.start(0)

# Función para medir la distancia con el HC-SR04
def medir_distancia():
    # Enviar pulso de 10us en el Trigger para iniciar medición
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)  # 10 microsegundos
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    
    # Esperar hasta que el Echo reciba el pulso
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    
    # Calcular el tiempo que tardó el pulso en ir y regresar
    pulse_duration = pulse_end - pulse_start
    
    # Calcular la distancia (distancia = velocidad del sonido * tiempo / 2)
    distancia = pulse_duration * 17150  # 34300 cm/s / 2
    distancia = round(distancia, 2)  # Redondear a 2 decimales
    return distancia

# Función para ajustar el ángulo del servo
def set_servo_angle(angle):
    duty = (angle / 260) * 10 + 5  # Convertir ángulo a ciclo de trabajo
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.02)  # Breve espera para asegurar que el servo se mueva

# Función para barrer el radar
def radar_scan():
    try:
        while True:
            for angle in range(0, 261, 10):  # Barrido de 0 a 260 grados
                set_servo_angle(angle)
                print(f"Escaneando {angle} grados...")
                
                # Medir distancia
                distancia = medir_distancia()
                print(f"Distancia: {distancia} cm")
                
                time.sleep(0.5)  # Espera entre mediciones

    except KeyboardInterrupt:
        print("Escaneo interrumpido.")
    
    finally:
        pwm.stop()
        GPIO.cleanup()  # Limpiar la configuración de GPIO

# Iniciar el escaneo
radar_scan()
