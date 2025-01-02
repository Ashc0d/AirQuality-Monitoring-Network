import requests
import time

pico_ips = ["http://192.168.104.215", "http://192.168.104.174"]
requests.post("https://ntfy.example.net/test",
    data="test on".encode(encoding='utf-8'))

while True: 
    for ips in pico_ips:
        try: 
            response = requests.get(ips)
            data = response.text.strip().split(":")[1].strip()
            
            data_value = float(data) 
            print(f"Fetched from {ips}: {data_value}")
            
            if data_value > 40:
                print(f"Danger alert from {ips}: {data_value}")

                message = f"Danger from {ips}: {data_value}"
                requests.post("https://ntfy.example.net/test",
                    data=message.encode(encoding='utf-8'))
            else: 
                print(f"Safe from {ips}: {data_value}")
                
        except requests.RequestException as e:
            print(f"Failed to fetch from {ips}: {e}")
        except (IndexError, ValueError) as e:
            print(f"Error processing data from {ips}: {e}")
        
    time.sleep(5)
