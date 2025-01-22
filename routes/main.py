from flask import Blueprint, render_template
from services.sensor import get_distance
from services.alerts import check_alert

main_routes = Blueprint('main', __name__)


@main_routes.route('/')
def index() :
    """Página principal que muestra la distancia y la gráfica."""
    distance = get_distance()
    alert_message = check_alert(distance)
    return render_template('index.html', distance=distance, alert=alert_message)


@main_routes.route('/alert')
def alert_page() :
    """Página para alertas."""
    return render_template('alert.html')
