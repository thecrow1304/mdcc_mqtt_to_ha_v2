
from flask import Blueprint, jsonify

def create_api(mqtt_manager):
    api = Blueprint("api", __name__)

    @api.route("/api/devices")
    def devices():
        return jsonify(mqtt_manager.get_devices())

    return api
