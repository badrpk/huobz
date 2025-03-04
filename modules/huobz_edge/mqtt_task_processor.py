import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT Broker Configuration
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
TASK_TOPIC = "huobz/ai/tasks"
RESULT_TOPIC = "huobz/ai/results"

# Generate a unique Edge Device ID
DEVICE_ID = f"EdgeDevice-{random.randint(1000, 9999)}"

# Callback when connected to MQTT Broker
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f"✅ {DEVICE_ID} Connected to MQTT Broker")
        client.subscribe(TASK_TOPIC)
    else:
        print(f"❌ Connection failed with error code {rc}")

# Callback when a task is received
def on_message(client, userdata, msg):
    try:
        task = json.loads(msg.payload.decode())
        print(f"📩 {DEVICE_ID} Received task: {task}")

        # Simulate AI processing (random processing time)
        time.sleep(random.randint(2, 5))  # Simulated processing delay
        result = {
            "device_id": DEVICE_ID,
            "task_id": task["task_id"],
            "status": "completed",
            "output": f"Processed {task['type']} successfully"
        }

        # Send result back to MQTT
        result_json = json.dumps(result)
        client.publish(RESULT_TOPIC, result_json)
        print(f"📤 {DEVICE_ID} Sent result: {result_json}")

    except Exception as e:
        print(f"⚠️ {DEVICE_ID} Error processing task: {e}")

# Initialize MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
print(f"🚀 {DEVICE_ID} Connecting to MQTT Broker...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Keep listening for tasks
client.loop_forever()
