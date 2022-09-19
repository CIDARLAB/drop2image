//const int size = 100; // default 10x10
//int pix[100];
//int cnt = 0;
//
//void setup(){
//    pinMode(LED_BUILTIN, OUTPUT);
//    Serial.begin(9600);
//    for (int i=0; i<100; i++){
//      pix[i] = Serial.read();
//      delay(500);
//    }
//}
//
//void loop(){
////    pix[cnt] = Serial.read();
////    delay(500);
////    cnt = cnt + 1;
//  for (int i=0; i<100; i++){
//      if (pix[i] == 1){
//        digitalWrite(LED_BUILTIN, HIGH);
//      }
//      delay(1000);
//      digitalWrite(LED_BUILTIN, LOW);
//      delay(1000);
//  }
//}

int x;
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
 Serial.begin(115200);
 Serial.setTimeout(3);
}
void loop() {
 while (!Serial.available()){
   x = Serial.readString().toInt();
   if (x == 0){
    digitalWrite(13, HIGH);
   }
   delay(500);
  digitalWrite(13, LOW);
  delay(500);
 }
}
