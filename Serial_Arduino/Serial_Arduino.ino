const int size = 100; // default 10x10
byte pix[100];
int cnt = 0;

void setup(){
    Serial.begin(9600);
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
}

void loop(){
    pix[cnt] = Serial.read();
    switch(pix[cnt]){
      case '0':
        digitalWrite(2, HIGH);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        break;
      case '1':
        digitalWrite(3, HIGH);
        digitalWrite(2, LOW);
        digitalWrite(4, LOW);
        break;
      case '2':
        digitalWrite(4, HIGH);
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        break;
      default:
        digitalWrite(2, HIGH);
        digitalWrite(3, HIGH);
        digitalWrite(4, HIGH);
        break;
    }
    delay(1000);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    delay(500);
    cnt = cnt + 1;
}
