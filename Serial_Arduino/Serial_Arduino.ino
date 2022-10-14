int x = 0;
int size = 121; // set size
int pix[121];
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  while (!Serial.available());
  for (int i=0; i<121; i++){
    pix[i] = Serial.readString().toInt();
  }
  Serial.end();
  Serial.begin(115200);
}
void loop() {
  Serial.print("hello world");
  x++;
  delay(1000);
}
