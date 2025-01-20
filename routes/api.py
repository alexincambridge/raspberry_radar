from flask import Blueprint, jsonify
from services.sensor import get_distance

api_routes = Blueprint('api', __name__)


@api_routes.route('/api/distance', methods=['GET'])
def api_distance() :
    """Devuelve la distancia medida en JSON."""
    distance = get_distance()
    return jsonify({'distance' : distance})
