from flask import Flask
from routes.main import main_routes
from routes.api import api_routes

# Crear instancia de Flask
app = Flask(__name__)

# Registrar rutas
app.register_blueprint(main_routes)
app.register_blueprint(api_routes)

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0')
