String x;
int cnt;
int len = 0;
int pix[130];
int done = 0;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 delay(3000);
 while (!Serial.available());
 while (len < 121){
   x = Serial.readString();
   if (x.length() != 0){
     parse(x);
     done++;
   }
   len += x.length();
   delay(200);
 }
 Serial.println("Done");
}
void loop() {
  if (cnt < 121){
  Serial.print(pix[cnt]);
  cnt++;
  }
}

void parse(String in){
  int x=0;
  if (done!=0){ x=61; }
  int l=in.length();
  for (int i=x; i<l+x; i++){
    if (in.length() == '\n'){
      continue;
    }
    else{
      pix[i] = in[i-x]-'0';
    }
  }
}