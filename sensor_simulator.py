import requests
import random
import sys
import time
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# ThingsBoard configuration
TB_HOST = "thingsboard.cloud"
TB_TOKEN = os.getenv("TB_TOKEN")
TB_URL = f"https://{TB_HOST}/api/v1/{TB_TOKEN}/telemetry"

# Simulation settings
INTERVAL_SECONDS = 3       # How often to check for motion
MOTION_PROBABILITY = 0.4   # 40% chance of motion each interval


def send_to_thingsboard(motion, total):
    """Send telemetry data to ThingsBoard via HTTP POST."""
    payload = {
        "motion": motion,
        "total_detections": total,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        response = requests.post(TB_URL, json=payload, timeout=5)
        return response.ok
    except requests.RequestException as e:
        print(f"[ERROR] Failed to send data: {e}")
        return False


def simulate_pir_sensor():
    """Return 1 if motion detected, 0 otherwise."""
    return 1 if random.random() < MOTION_PROBABILITY else 0


def main():
    if not TB_TOKEN:
        sys.exit("[ERROR] TB_TOKEN is not set. Copy .env.example to .env and add your device token.")

    print("=== Motion Sensor Simulator Started ===")
    print(f"Sending data to ThingsBoard every {INTERVAL_SECONDS} seconds...")
    print("Press Ctrl+C to stop.\n")

    total_detections = 0
    try:
        while True:
            motion = simulate_pir_sensor()

            if motion == 1:
                total_detections += 1
                print(f"[{datetime.now().strftime('%H:%M:%S')}] MOTION DETECTED! Total: {total_detections}")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] No motion.")

            if send_to_thingsboard(motion, total_detections):
                print("  → Sent to ThingsBoard OK")
            else:
                print("  → Failed to send!")

            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print(f"\nStopped. Total detections: {total_detections}")


if __name__ == "__main__":
    main()
