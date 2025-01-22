import RPi.GPIO as GPIO
import time

# Configuración de pines GPIO
TRIG = 23
ECHO = 24

# Configuración inicial de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Desactiva las advertencias sobre pines ya configurados
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_distance() :
    """Mide la distancia usando el HC-SR04."""
    try :
        # Enviar pulso de disparo
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Medir tiempo de respuesta
        start_time = time.time()
        stop_time = time.time()

        # Esperar a que ECHO se ponga en alto
        while GPIO.input(ECHO) == 0 :
            start_time = time.time()

        # Esperar a que ECHO vuelva a bajo
        while GPIO.input(ECHO) == 1 :
            stop_time = time.time()

        # Calcular distancia
        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2
        return round(distance, 2)

    except RuntimeError as e :
        print(f"Error al medir la distancia: {e}")
        return None


def cleanup_gpio() :
    """Limpia los pines GPIO."""
    GPIO.cleanup()


if __name__ == "__main__" :
    try :
        while True :
            dist = get_distance()
            if dist is not None :
                print(f"Distancia: {dist} cm")
            time.sleep(1)
    except KeyboardInterrupt :
        print("\nFinalizando el programa.")
    finally :
        cleanup_gpio()
