# Low-cost IoT Air Quality Monitor

Arduino/ESP32 based low-cost sensor node for monitoring PM2.5, PM10, temperature, and humidity.

## Overview
This project implements a affordable IoT air quality sensor using ESP32 or Arduino with sensors like PMS5003, DHT22, or SDS011. Data can be sent to cloud platforms or local dashboards for citizen science and local AQI monitoring in places like Hyderabad or Ongole.

## Features
- Real-time PM2.5 and PM10 measurement
- Temperature and humidity sensing
- WiFi connectivity for data upload (MQTT/HTTP)
- Low power design suitable for battery operation
- Calibration guidelines for accuracy
- Sample code for ESP32

## Tech Stack
- **Hardware**: ESP32 / Arduino, PMS5003 or similar PM sensor, DHT22
- **Software**: Arduino IDE / PlatformIO, Python for data processing
- **Protocols**: MQTT, HTTP REST
- **Visualization**: Optional Grafana or custom dashboard

## Getting Started
1. Assemble the hardware as per wiring diagram (see docs if added)
2. Flash the firmware using Arduino IDE
3. Configure WiFi and MQTT broker credentials
4. Monitor serial output or cloud dashboard
5. For analysis: pip install -r requirements.txt && python analysis.py

## Sample Data
See `sample_aqi_data.csv` for example sensor readings.

## License
MIT
