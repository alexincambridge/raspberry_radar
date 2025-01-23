from flask import Flask, jsonify, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# Configuración de pines GPIO
TRIGGER_PIN = 23
ECHO_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


def medir_distancia() :
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    start_time = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW :
        start_time = time.time()
        if time.time() - start_time > 0.02 :
            return None

    while GPIO.input(ECHO_PIN) == GPIO.HIGH :
        end_time = time.time()
        if time.time() - start_time > 0.02 :
            return None

    duration = end_time - start_time
    distancia = duration * 17150
    return round(distancia, 2)


@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/api/distance')
def api_distance() :
    distancia = medir_distancia()
    if distancia is not None :
        return jsonify({"distance" : distancia})
    else :
        return jsonify({"error" : "No se pudo medir la distancia"}), 500


if __name__ == '__main__' :
    try :
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt :
        GPIO.cleanup()
