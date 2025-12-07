import time
import random
import os
import json
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message


if os.getenv("ENV") != "production":
    load_dotenv()

def generate_data():
    """Generate simulation data"""
    data = {
        "ice_thickness": round(random.uniform(0.0, 50.0), 2),
        "surface_temperature": round(random.uniform(-30.0, 25.0), 2),
        "snow_accumulation": round(random.uniform(0.0, 100.0), 2),
        "external_temperature": round(random.uniform(-30.0, 25.0), 2)
    }
    return data

def send_data():
    con_str = os.getenv("DEVICE_CONNECTION_STRING")
    if con_str is None:
        raise ValueError("DEVICE_CONNECTION_STRING environment variable is not set")
    
    device_client = IoTHubDeviceClient.create_from_connection_string(con_str)
    try:
        while True:
            payload = generate_data()
            message = Message(json.dumps(payload))
            message.content_type = "application/json"
            message.content_encoding = "utf-8"
            device_client.send_message(message)
            print(f"sent message: {message}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("stop sending data")
    finally:
        device_client.disconnect()

if __name__ == "__main__":
    send_data()