
import json
import os
import paho.mqtt.client as mqtt
from ha_discovery import publish_discovery

class MQTTManager:

    def __init__(self):
        self.devices = {}
        self.client = mqtt.Client()

        user = os.getenv("MQTT_USER")
        pwd = os.getenv("MQTT_PASSWORD")

        if user:
            self.client.username_pw_set(user, pwd)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def start(self):
        host = os.getenv("MQTT_HOST")
        port = int(os.getenv("MQTT_PORT", 1883))

        self.client.connect(host, port, 60)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        base_topic = os.getenv("BASE_TOPIC", "physec/#")
        client.subscribe(base_topic)

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
        except:
            return

        topic_parts = msg.topic.split("/")

        try:
            tenant = topic_parts[3]
        except:
            tenant = "unknown"

        sensor = payload.get("sensor", {})
        message = payload.get("message", {})

        device_id = sensor.get("deviceId", "unknown")
        device_type = sensor.get("type", "unknown")
        device_name = sensor.get("alias", device_id)

        device_key = f"{tenant}_{device_id}"

        if device_key not in self.devices:
            self.devices[device_key] = {
                "tenant": tenant,
                "device_id": device_id,
                "type": device_type,
                "name": device_name,
                "entities": []
            }

        for field, value in message.items():
            entity_id = f"{device_key}_{field}".lower().replace(" ", "_")

            if entity_id not in self.devices[device_key]["entities"]:
                publish_discovery(
                    device_key,
                    device_name,
                    device_id,
                    device_type,
                    field,
                    value
                )
                self.devices[device_key]["entities"].append(entity_id)

            self.publish_state(entity_id, value)

    def publish_state(self, entity_id, value):
        state_topic = f"dynamic_entities/{entity_id}/state"

        if isinstance(value, dict):
            val = value.get("value")
        else:
            val = value

        self.client.publish(state_topic, val)

    def get_devices(self):
        return self.devices
