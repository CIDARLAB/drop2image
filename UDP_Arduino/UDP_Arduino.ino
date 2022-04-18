#include <WiFi.h>

const char ssid[] = "myssid"; // SSID here
const char password[] = "mypassword"; // password here
const int port = 8080;


const IPAddress local_ip(, , , ); // Arduino IP Address here
const IPAddress server_ip(, , , ); // Host IP Address here
const IPAddress subnet(255, 255, 255, 0); // subnet

const int size = 100; // default 10x10
int pix[size];
int cnt = 0;

WiFiClient client;

void setup(){
    Serial.begin(115200);

    WiFi.softAP(ssid, password);
    delay(100);
    WiFi.softAPConfig(local_ip, local_ip, subnet);

    IPAddress myIP = WiFi.softAPIP();

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED){
        delay(500);
    }

    client.connect(server_ip, port);
}

void loop(){
    if (client.available()){
        pix[cnt] = client.read();
        cnt++;
    }
}