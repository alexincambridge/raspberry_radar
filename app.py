from flask import Flask, jsonify, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO Pin Setup
TRIGGER_PIN = 23
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


def medir_distancia() :
    """Measure distance using HC-SR04."""
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    start_time = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW :
        start_time = time.time()
        if time.time() - start_time > 0.02 :  # Timeout for LOW
            return None

    while GPIO.input(ECHO_PIN) == GPIO.HIGH :
        end_time = time.time()
        if time.time() - start_time > 0.02 :  # Timeout for HIGH
            return None

    duration = end_time - start_time
    distance = duration * 17150  # Speed of sound: 34300 cm/s divided by 2
    return round(distance, 2)


@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/api/distance')
def api_distance() :
    distance = medir_distancia()
    if distance is not None and distance < 200 :  # Limit to 200 cm
        return jsonify({"distance" : distance})
    else :
        return jsonify({"distance" : None})


if __name__ == '__main__' :
    try :
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt :
        GPIO.cleanup()
