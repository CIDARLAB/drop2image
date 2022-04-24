#include <YunClient.h>
#include <Bridge.h>
#include <BridgeClient.h>
#include <WiFi.h>
#include <SPI.h>

YunClient client;
IPAddress ip(192,168,1,136);
int port = 8080;
bool clientActive = false;

void setup(){
    Serial.begin(9600);
}

void loop(){
    client.connect(ip, port);
    if (client.connected()){
      if (!clientActive) {
        Serial.println("New Client Connected");
      }
      while (client.available()){
        char val = client.read();
        Serial.print("Reading is: ");
        Serial.println(val);
      }
      clientActive = true;
    }
    else{
      if (clientActive){
        client.stop();
        Serial.println("Client disconnected");
      }
      clientActive=false;
      client.connect(ip,port);
    }
    delay(1000);
}
