import RPi.GPIO as GPIO
import time

# Configuración de pines GPIO
TRIGGER_PIN = 23
ECHO_PIN = 24

# Constantes configurables
SOUND_SPEED_CM_S = 34300  # Velocidad del sonido en cm/s
TIMEOUT = 0.02  # Tiempo límite en segundos (20 ms)

# Configurar la numeración de pines y los modos de entrada/salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


def medir_distancia(debug=False) :
    """
    Mide la distancia usando un sensor ultrasónico HC-SR04.
    :param debug: Modo de depuración (True para imprimir mensajes de error)
    :return: Distancia en cm (float) o None en caso de error
    """
    try :
        # Asegurarse de que el Trigger esté en LOW antes de iniciar
        GPIO.output(TRIGGER_PIN, GPIO.LOW)
        time.sleep(0.05)  # Breve pausa para estabilizar el sensor

        # Enviar un pulso de Trigger (10 microsegundos)
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001)  # 10 microsegundos
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

        # Esperar el inicio del pulso en Echo
        start_time = time.time()
        while GPIO.input(ECHO_PIN) == GPIO.LOW :
            if time.time() - start_time > TIMEOUT :
                if debug :
                    print("Error: Tiempo de espera excedido para LOW.")
                return None

        # Medir la duración del pulso en Echo
        start_time = time.time()
        while GPIO.input(ECHO_PIN) == GPIO.HIGH :
            if time.time() - start_time > TIMEOUT :
                if debug :
                    print("Error: Tiempo de espera excedido para HIGH.")
                return None

        # Calcular la duración del pulso
        duration = time.time() - start_time

        # Calcular la distancia (distancia = velocidad del sonido * tiempo / 2)
        distancia = duration * SOUND_SPEED_CM_S / 2
        return round(distancia, 2)

    except Exception as e :
        if debug :
            print(f"Error en medir_distancia: {e}")
        return None

# Función principal
if __name__ == "__main__" :
    try :
        print("Iniciando medición de distancia...")
        while True :
            distancia = medir_distancia(debug=True)
            if distancia is not None :
                print(f"Distancia: {distancia} cm")
            else :
                print("Error al medir la distancia.")
            time.sleep(1)  # Pausa de 1 segundo entre mediciones

    except KeyboardInterrupt :
        print("Medición interrumpida por el usuario.")

    finally :
        GPIO.cleanup()  # Limpiar configuración GPIO
