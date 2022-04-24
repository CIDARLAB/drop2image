const int size = 100; // default 10x10
byte pix[100];
int cnt = 0;

void setup(){
    Serial.begin(9600);
}

void loop(){
    pix[cnt] = Serial.read();
    delay(500);
    cnt = cnt + 1;
}

// send the entire array
// need serial monitor open
// write to SD on Arduino
// ethernet でもオッケー
// need to be able to reset and start from the top