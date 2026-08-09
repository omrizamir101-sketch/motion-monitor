# Motion Monitor

A Python service that simulates a PIR motion sensor and streams telemetry to a [ThingsBoard](https://thingsboard.cloud) cloud dashboard via REST API, built for a university embedded-systems course.

## How it works

- `sensor_simulator.py` simulates PIR motion detection at a configurable interval and probability, then sends each reading (motion state + running total) as an HTTP POST to ThingsBoard's telemetry endpoint.
- `generate_doc.py` generates the project documentation.

## Running locally

```bash
pip install -r requirements.txt
```

Create a `.env` file (see `.env.example`):
```
TB_TOKEN=your-thingsboard-device-access-token
```

Then run:
```bash
python sensor_simulator.py
```

## Tech Stack

Python, ThingsBoard (IoT platform), REST API
