
#!/usr/bin/with-contenv bashio

CONFIG_PATH=/data/options.json

export MQTT_HOST=$(jq -r '.mqtt_host' $CONFIG_PATH)
export MQTT_PORT=$(jq -r '.mqtt_port' $CONFIG_PATH)
export MQTT_USER=$(jq -r '.mqtt_user' $CONFIG_PATH)
export MQTT_PASSWORD=$(jq -r '.mqtt_password' $CONFIG_PATH)
export BASE_TOPIC=$(jq -r '.base_topic' $CONFIG_PATH)
export HA_DISCOVERY_PREFIX=$(jq -r '.ha_discovery_prefix' $CONFIG_PATH)

python3 /app/app/main.py
