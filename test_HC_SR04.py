import RPi.GPIO as GPIO
import time

# Configuración de pines GPIO
TRIGGER_PIN = 23
ECHO_PIN = 24

# Configurar la numeración de pines y los modos de entrada/salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def medir_distancia():
    try:
        # Asegurarse de que el Trigger esté en LOW antes de iniciar
        GPIO.output(TRIGGER_PIN, GPIO.LOW)
        time.sleep(0.05)  # Breve pausa para estabilizar el sensor

        # Enviar un pulso de Trigger (10 microsegundos)
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001)  # 10 microsegundos
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

        # Esperar el inicio del pulso en Echo
        start_time = time.time()
        while GPIO.input(ECHO_PIN) == GPIO.LOW:
            start_time = time.time()
            if time.time() - start_time > 0.02:  # Tiempo límite de 20 ms
                print("Error: Tiempo de espera excedido para LOW.")
                return None

        # Medir la duración del pulso en Echo
        while GPIO.input(ECHO_PIN) == GPIO.HIGH:
            end_time = time.time()
            if time.time() - start_time > 0.02:  # Tiempo límite de 20 ms
                print("Error: Tiempo de espera excedido para HIGH.")
                return None

        # Calcular la duración del pulso
        duration = end_time - start_time

        # Calcular la distancia (distancia = velocidad del sonido * tiempo / 2)
        distancia = duration * 17150  # 34300 cm/s / 2
        return round(distancia, 2)

    except Exception as e:
        print(f"Error en medir_distancia: {e}")
        return None

# Función principal
try:
    print("Iniciando medición de distancia...")
    while True:
        distancia = medir_distancia()
        if distancia is not None:
            print(f"Distancia: {distancia} cm")
        else:
            print("Error al medir la distancia.")
        time.sleep(1)  # Pausa de 1 segundo entre mediciones

except KeyboardInterrupt:
    print("Medición interrumpida por el usuario.")

finally:
    GPIO.cleanup()  # Limpiar configuración GPIO
