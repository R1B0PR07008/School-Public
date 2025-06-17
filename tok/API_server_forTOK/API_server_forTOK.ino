#include <WiFiS3.h>
#include <Arduino_LED_Matrix.h>

ArduinoLEDMatrix matrix;

char ssid[] = "HIGH_SCHOOL"; // your network SSID
char pass[] = "hs.MDM.2024";    // your network password

WiFiServer server(81);

void setup() {
  Serial.begin(9600);
  while (!Serial);

  matrix.begin();

  int status = WL_IDLE_STATUS;
  while (status != WL_CONNECTED) {
    Serial.println("Trying to connect");
    status = WiFi.begin(ssid, pass);
    delay(5000);
  }

  Serial.print("Connected. IP: ");
  Serial.println(WiFi.localIP());
  server.begin();

  // PIN setup 
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);

}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("Client connected");

    String reqLine = "";
    int contentLength = 0;
    bool isPost = false;

    // === READ HEADERS ===
    while (client.connected()) {
      String line = client.readStringUntil('\n');
      line.trim();
      if (line.length() == 0) break; // End of headers
      if (line.startsWith("POST")) isPost = true;
      if (line.startsWith("Content-Length")) {
        contentLength = line.substring(15).toInt();
      }
    }

    // === READ BODY ===
    String body = "";
    int bytesRead = 0;
    unsigned long timeout = millis();
    while (bytesRead < contentLength && millis() - timeout < 1000) {
      if (client.available()) {
        char c = client.read();
        body += c;
        bytesRead++;
      }
    }

    Serial.print("Received body: ");
    Serial.println(body);

    // === RESPONSE ===
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/plain");
    client.println("Connection: close");
    client.println();
    client.println(body);

    if (body == "red") {
      digitalWrite(5, HIGH);
      delay(1000);
      digitalWrite(5, LOW);
    }
    else if (body == "green") {
      digitalWrite(6, HIGH);
      delay(1000);
      digitalWrite(6, LOW);
    }
    else if (body == "blue") {
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
    }
    else if (body == "yellow") {
      digitalWrite(9, HIGH);
      delay(1000);
      digitalWrite(9, LOW);
    };
  
    client.stop();
    Serial.println("Client disconnected");
  }
}