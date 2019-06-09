byte _WE = 2;
byte _OE = 3;
byte CLK = 4;
int datastart = 5;
int datalen = 8;
int addrstart = 22;
int addrlen = 8;
void setup() {
  Serial.begin(9600);
  pinMode(_WE,OUTPUT);
  pinMode(_OE,OUTPUT);
  pinMode(CLK,OUTPUT);
  
  for(int i = 0; i < addrlen; ++i){
    pinMode(addrstart+i,OUTPUT);
  }
  for(int i = 0; i < datalen; ++i){
    pinMode(datastart+i,INPUT);
  }
}

void loop() {
  String cmd = "";
  while (Serial.available()) {
    delay(3);
    if (Serial.available())
    {
      char c = Serial.read();
      cmd += c;
    }
  }
  cmd.toUpperCase();
  int first = cmd.indexOf(' ');
  int last = cmd.lastIndexOf(' ');
  if (cmd.startsWith("RA")){
    readall();
  }
  else if (cmd.startsWith("R"))
  {
    int addr = strtol(cmd.substring(first).c_str(),0,16);
    int data = read(addr);
    Serial.print("READ 0x");
    Serial.print(addr,HEX);
    Serial.print(" : 0x");
    Serial.println(data,HEX);
  }
  else if (cmd.startsWith("W"))
  {

    int addr = strtol(cmd.substring(first, last).c_str(),0,16);
    int data =  strtol(cmd.substring(last).c_str(),0,16);
    write(addr, data);
//    int data_confirm = read(addr);
//    if (data_confirm == data)
//    {
//      Serial.print("WRITE 0x");
//      Serial.print(addr, HEX);
//      Serial.print(" : 0x");
//      Serial.println(data, HEX);
//    }
//    else
//    {
//      Serial.print("WRITE FAILED ADDR 0x");
//      Serial.print(addr, HEX);
//      Serial.print(" : 0x");
//      Serial.print(data_confirm, HEX);
//      Serial.print("(0x");
//      Serial.print(data, HEX);
//      Serial.println(" is the expected value)");
//    }
  }
}

void setAddr(int addr){
    for(int i = 0; i < addrlen; ++i){
    digitalWrite(addrstart + i,(addr >> i)&1);
  }
}

int read(int addr){
  setAddr(addr);
  int data = 0;
  for(int i = 0; i < datalen; ++i){
    pinMode(datastart+i,INPUT);
  }
  
  digitalWrite(_WE,HIGH);
  digitalWrite(_OE,LOW);
  for(int i = 0; i < datalen; ++i){
    data += (digitalRead(datastart + i) << i);
  }
  digitalWrite(_OE,HIGH);
  return data;
}

void write(int addr,int data){
  setAddr(addr);
  digitalWrite(_OE,HIGH); 
  for(int i = 0; i < datalen; ++i){
    pinMode(datastart+i,OUTPUT);
  }


  
  for(int i = 0; i < datalen; ++i){
    digitalWrite(datastart+i, (data >> i)&1);
  }
   digitalWrite(_WE,LOW);
   digitalWrite(CLK,HIGH);
   digitalWrite(CLK,LOW);
   digitalWrite(_WE,HIGH);
}
void  readall(){
  for(int i = 0; i < 128; ++i){
    write(i,i*i + i);
  }
  for(int i = 0; i < 128; ++i){
    if(i% 8 == 0){
      Serial.println();  
    }
    Serial.print("0x");
    String s = String(read(i),HEX);
    if( s.length() < 2)
      s = '0' + s;
    Serial.print(s);
    Serial.print(' ');
  }
}
