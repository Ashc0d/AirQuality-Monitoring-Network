import requests
import time
from prometheus_client import start_http_server, Gauge

pico_ips = ["http://192.168.104.215", "http://192.168.104.174"]

sensors = {ip: Gauge(f"mq135_sensor_data_{i+1}", "MQ-135 Sensor Value", ["ip"]) for i, ip in enumerate(pico_ips)}
def fetch_sensor_data():
    for pico_ip in pico_ips:
        try:
            response = requests.get(pico_ip)
            response.raise_for_status()
            data = response.text.strip().split(":")[1].strip()
            data = float(data)
            
            sensors[pico_ip].labels(ip=pico_ip).set(data)
            
            print(f"Fetched data from {pico_ip}: {data}")
        
        except requests.RequestException as e:
            print(f"Failed to fetch data from {pico_ip}: {e}")

if __name__ == "__main__":
    start_http_server(8000)
    print("Prometheus exporter running on port 8000")

    while True:
        fetch_sensor_data()
        time.sleep(10)

