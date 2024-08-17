#include <ESP8266WiFi.h>
#include <WebSocketsClient.h>

const char* ssid = "tu_SSID";
const char* password = "tu_PASSWORD";
const char* websockets_server_host = "IP_DE_TU_RASPBERRY_PI";
const uint16_t websockets_server_port = 8765;

WebSocketsClient webSocket;

void setup() {
  Serial.begin(100);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");

  webSocket.begin(websockets_server_host, websockets_server_port, "/");
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  webSocket.loop();
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  switch (type) {
    case WStype_DISCONNECTED:
      Serial.println("Disconnected!");
      break;
    case WStype_CONNECTED:
      Serial.println("Connected to server");
      webSocket.sendTXT("Hello from ESP8266");
      break;
    case WStype_TEXT:
      Serial.printf("Message received: %s\n", payload);
      break;
    case WStype_ERROR:
      Serial.println("Error");
      break;
    default:
      break;
  }
}
