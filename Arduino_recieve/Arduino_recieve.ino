#include <Process.h>
int pix[110];

void setup() {
    Bridge.begin();
    Serial.begin(9600);
    while (!Serial);
    runCurl();
}

void loop() {

}

void runCurl() {
    Process p;
    p.begin("curl");
    p.addParameter("http://10.192.13.179:8888/pix.txt"); // this need to be changed to "http:// your IP of PC:8888/pix.txt
    p.run();
    int cnt = 0;
    while (p.available()>0) {

        char c = p.read();
        Serial.print(c);
        if (c - '0'  >= 0 && c - '0' <= 9){
            pix[cnt] = c - '0';
            cnt++;
        }
    }
    Serial.flush();
}
