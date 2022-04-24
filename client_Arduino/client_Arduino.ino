#include <Bridge.h>
#include <BridgeClient.h>
#include <YunClient.h>

YunClient client;
byte ip[] = {192, 168, 1, 136 };
int port = 8080;
bool clientActive = false;

void setup(){
    pinMode(13, OUTPUT);
    digitalWrite(13,HIGH);
    Bridge.begin();
    digitalWrite(13,LOW);
    Serial.begin(9600);
}

void loop(){
    client.connect(ip,port);
    if (client.connected()){
        if (!clientActive){
            Serial.println("New Client connection.");
        }
        clientActive = true;

        if (client.available()){
            char c = client.read();
            Serial.print("From client: \"");
            while(client.available()){
                Serial.print((char)client.read());
            }
            Serial.println("\"");
        }
    }
    else{
        if (clientActive){
            client.stop();
            Serial.println("Client disconnected.");
        }
        clientActive=false;
        client.connect(ip,port);
    }
}
