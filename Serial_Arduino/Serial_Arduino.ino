int x;
int size = 121; // set size
int pix[121];
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  for (int i=0; i<100; i++){
    pix[i] = Serial.readString().toInt();
    Serial.print(pix[i]);
  }
}
void loop() {
}
