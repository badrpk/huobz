import paho.mqtt.client as mqtt
import json

# MQTT Broker Configuration
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "huobz/ai/tasks"

# Initialize MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Define an AI Task (Example: Image Processing)
task = {
    "task_id": "12345",
    "type": "image_processing",
    "data": "https://example.com/sample_image.jpg"
}

# Publish the AI task
task_json = json.dumps(task)
client.publish(MQTT_TOPIC, task_json)
print(f"📤 Task sent: {task_json}")

# Disconnect
client.disconnect()
