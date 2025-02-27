# AirQuality Monitoring Network

The **AirQuality Monitoring Network** is an open-source project designed to monitor air quality using a distributed network of sensors. This repository contains the software and configuration files needed to set up and operate the monitoring network effectively.

## Features

- **Real-Time Monitoring**: Collects and processes air quality data in real time.
- **Networked Sensor Nodes**: Utilizes Arduino-based nodes for data collection.
- **Data Export**: Python scripts to export and analyze collected data.
- **Notification System**: Automated notifications based on air quality thresholds.
- **Prometheus Integration**: Monitors and visualizes metrics using Prometheus.
- **Containerized Deployment**: Simplified setup with Docker Compose.

![Grafana Dashboard](/assets/images/image-1.jpg)

## Getting Started

### Prerequisites

- [Arduino IDE](https://www.arduino.cc/en/software) for programming the sensor nodes.
- Python 3.6 or higher.
- Docker and Docker Compose installed.
- Prometheus monitoring system.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ashc0d/AirQuality-Monitoring-Network.git
   cd AirQuality-Monitoring-Network
   ```

2. **Set Up Sensor Nodes:**
   - Open `node.ino` in the Arduino IDE.
   - Configure the Wi-Fi credentials and upload the code to your Arduino board.

3. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Prometheus:**
   - Update `prometheus.yml` as needed.
   - Use Docker Compose to launch Prometheus:
     ```bash
     docker-compose up -d
     ```

5. **Run Scripts:**
   - Start the data exporter:
     ```bash
     python data-exporter.py
     ```
   - Enable notifications with:
     ```bash
     python notify.py
     ```

## Repository Structure

```
AirQuality-Monitoring-Network/
├── node.ino               # Arduino code for sensor nodes
├── data-exporter.py       # Script for exporting and processing data
├── notify.py              # Notification script
├── prometheus.yml         # Prometheus configuration
├── docker-compose.yml     # Docker Compose file for Prometheus
└── README.md              # Project documentation
```

## License

This project is licensed under the [Apache-2.0 License](LICENSE). You are free to use, modify, and distribute the code, provided that you comply with the terms of the license.
