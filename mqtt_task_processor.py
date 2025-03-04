import paho.mqtt.client as mqtt
import json

# MQTT Broker Configuration
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
TASK_TOPIC = "huobz/ai/tasks"
RESULT_TOPIC = "huobz/ai/results"

# Callback when connected
def on_connect(client, userdata, flags, rc, properties):
    print("✅ Connected to MQTT Broker")
    client.subscribe(TASK_TOPIC)

# Callback when a task is received
def on_message(client, userdata, msg):
    task = json.loads(msg.payload.decode())
    print(f"📩 Received task: {task}")

    # Simulate AI processing (e.g., analyzing an image)
    result = {"task_id": task["task_id"], "status": "completed", "output": "Processed image successfully"}

    # Send result back to MQTT
    result_json = json.dumps(result)
    client.publish(RESULT_TOPIC, result_json)
    print(f"📤 Sent result: {result_json}")

# Initialize MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

# Connect and listen for tasks
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
