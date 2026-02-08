
from flask import Flask, jsonify
from flask_cors import CORS

def create_web_app(mqtt_manager):
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def index():
        return "MQTT Dynamic Entities Add-on"

    @app.route("/devices")
    def devices():
        return jsonify(mqtt_manager.get_devices())

    return app
