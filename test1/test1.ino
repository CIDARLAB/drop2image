String x;
int cnt;
int len = 0;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 delay(5000);
 while (!Serial.available());
 Serial.print('Start printing');
 while (len < 120){
   x = Serial.readString();
   Serial.print("length");
   Serial.print(x);
   Serial.println(x.length());
   len += x.length();
   delay(100);
 }
 Serial.println("Done");
}
void loop() {
//  while (!Serial.available());
//  if (cnt < 10){
//   x = Serial.readString();
//   Serial.print(x);
//  }
//  else{
//    String hello = "hey";
//    Serial.print(hello);
//  }
//   cnt++;
  if (cnt <100){
  Serial.print("loop");
  cnt++;
  }
}