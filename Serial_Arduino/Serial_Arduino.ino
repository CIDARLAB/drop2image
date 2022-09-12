const int size = 100; // default 10x10
int pix[100];
int cnt = 0;

void setup(){
    Serial.begin(9600);
    for (int i=0; i<100; i++){
      pix[i] = Serial.read();
      delay(500);
    }
    delay(10000);
    Serial.print("Done");
    for (int i=0; i<100; i++){
      Serial.println(pix[i]);
    }
}

void loop(){
//    pix[cnt] = Serial.read();
//    delay(500);
//    cnt = cnt + 1;
}
