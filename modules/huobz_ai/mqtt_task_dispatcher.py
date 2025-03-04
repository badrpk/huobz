import paho.mqtt.client as mqtt
import json
import time

# MQTT Broker Configuration
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "huobz/ai/tasks"

# Initialize MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Send multiple AI tasks
for i in range(5):  # Dispatching 5 tasks
    task = {
        "task_id": str(i + 100),
        "type": "image_processing",
        "data": f"https://example.com/sample_image_{i}.jpg"
    }
    task_json = json.dumps(task)
    client.publish(MQTT_TOPIC, task_json)
    print(f"📤 Task sent: {task_json}")
    time.sleep(1)  # Simulating task dispatch delay

client.disconnect()
