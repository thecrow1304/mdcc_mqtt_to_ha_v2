
import threading
from mqtt_manager import MQTTManager
from api import create_api
from flask import Flask, send_from_directory
from flask_cors import CORS

mqtt = MQTTManager()

def start_mqtt():
    mqtt.start()

if __name__ == "__main__":
    t = threading.Thread(target=start_mqtt)
    t.daemon = True
    t.start()

    app = Flask(__name__, static_folder="../frontend")
    CORS(app)
    app.register_blueprint(create_api(mqtt))

    @app.route("/")
    def serve_frontend():
        return send_from_directory(app.static_folder, "index.html")

    app.run(host="0.0.0.0", port=8099)
