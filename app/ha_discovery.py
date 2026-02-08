
import json
import os
import paho.mqtt.publish as publish

def publish_discovery(device_key, device_name, device_id, device_type, field, value):
    prefix = os.getenv("HA_DISCOVERY_PREFIX", "homeassistant")

    entity_id = f"{device_key}_{field}".lower().replace(" ", "_")

    config_topic = f"{prefix}/sensor/{entity_id}/config"
    state_topic = f"dynamic_entities/{entity_id}/state"

    unit = ""
    if isinstance(value, dict):
        unit = value.get("unit", "")

    payload = {
        "name": f"{device_name} {field}",
        "state_topic": state_topic,
        "unique_id": entity_id,
        "device": {
            "identifiers": [device_key],
            "name": device_name,
            "model": device_type,
            "manufacturer": "Dynamic MQTT"
        }
    }

    if unit:
        payload["unit_of_measurement"] = unit

    publish.single(
        config_topic,
        json.dumps(payload),
        hostname=os.getenv("MQTT_HOST"),
        port=int(os.getenv("MQTT_PORT", 1883))
    )
