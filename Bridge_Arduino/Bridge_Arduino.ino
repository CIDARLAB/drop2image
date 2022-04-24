#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>
#include <BridgeServer.h>
#include <BridgeClient.h>

BridgeServer server;

void setup() {
    Serial.begin(9600);
    pinMode(13,OUTPUT);
    digitalWrite(13, LOW);
    Bridge.begin();
    digitalWrite(13, HIGH);
    Serial.println("Bridge begins");
    server.listenOnLocalhost();
    server.begin();
}

void loop() {
    BridgeClient client = server.accept();
    if (client){
        Serial.println("Yay");
        char c = client.read();
        Serial.println(c);
        client.write(1);
        client.stop();
    }
    else{
      Serial.println("Not Yet");
    }
    delay(100);
}
