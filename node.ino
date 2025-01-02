#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>

const char* ssid = "ssid";
const char*  pass = "password";

 
WebServer server(80);

 
const int sensorpin = A0;  
int sensorval = 0;

void setup() {
  Serial.begin(115200);
  
   
  WiFi.begin(ssid,  pass);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nconnected to wifi");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

   
  server.on("/", HTTP_GET, []() {
    String data = String(sensorval);
    server.send(200, "text/plain", "mq-135 sensor value: " + data);
  });
  
  server.begin();
  Serial.println("web server started");
}

void loop() {
   
  sensorval = analogRead(sensorpin);
  
  Serial.print("mq-135 sensor value: ");
  Serial.println(sensorval);

  server.handleClient();
  
  delay(2000);   
}
