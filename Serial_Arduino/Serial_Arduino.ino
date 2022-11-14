String x;
int cnt;
int len = 0;
int pix[30];
int done = 0;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 delay(1000);
 while (!Serial.available());
 while (len < 25){
   x = Serial.readString();
   if (x.length() == 25){
    //  Serial.println(x);
     parse(x);
    //  done++;
   }
   len += x.length();
   Serial.println(len);
   delay(2000);
 }
 Serial.println("Done");
}
void loop() {
  if (cnt < 25){
  Serial.print(pix[cnt]);
  cnt++;
  }
}

// void parse(String in){

//   int x=0;
//   if (done!=0){ x=61; }
//   int l=in.length();
//   for (int i=x; i<l+x; i++){
//     if (in.length() == '\n'){
//       continue;
//     }
//     else{
//       pix[i] = in[i-x]-'0';
//     }
//   }
// }

void parse(String in){
  for (int i=0; i<in.length(); i++){
    pix[i] = in[i]-'0';
    // Serial.print("here");
    // Serial.print(in[i]);
  }
}