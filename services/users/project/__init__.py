# services/users/project/__init__.py

import os # <-- nuevo
from flask import Flask, jsonify


# instanciando la app
app = Flask(__name__)

# estableciendo configuración
app_settings = os.getenv('APP_SETTINGS')  # <-- nuevo
app.config.from_object(app_settings)      # <-- nuevo

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'estado': 'satisfactorio',
        'mensaje': 'pong!!!'
    })
