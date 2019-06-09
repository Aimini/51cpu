int DATA[8]={2,3,4,5,6,7,8,9};
int CLK = 10;
int RST = 11;
int _RST = 12;
int LE  = 13;
int _LE = A0;
int OE = A1;
int _OE = A2;

void setBusMode(int mode){
  for(auto x: DATA){
    pinMode(x,mode);
  }
}

String readSerial(){
  String cmd = "";
  while (Serial.available()) {
    delay(3);
    if (Serial.available())
    {
      char c = Serial.read();
      cmd += c;
    }
  }
  return cmd;
}
void setup(){
  
  pinMode(CLK,OUTPUT);
  pinMode(RST,OUTPUT);
  pinMode(_RST,OUTPUT);
  pinMode(LE,OUTPUT);
  pinMode(_LE,OUTPUT);
  pinMode(OE,OUTPUT);
  pinMode(_OE,OUTPUT);
  
  digitalWrite(CLK,LOW);
  digitalWrite(RST,LOW);
  digitalWrite(_RST,HIGH);
  digitalWrite(LE,LOW);
  digitalWrite(_LE,HIGH);
  digitalWrite(OE,LOW);
  digitalWrite(_OE,HIGH);
  Serial.begin(9600);
}


void loop() {
  String cmd = readSerial();
  

  cmd.toUpperCase();
  int first = cmd.indexOf(' ');
  int last = cmd.lastIndexOf(' ');
  if (cmd.startsWith("RE"))
  {
    Serial.print("READ 0x");
    Serial.println(outputToBus(),HEX);
  }
  if (cmd.startsWith("WR"))
  {
    int data =  strtol(cmd.substring(last).c_str(),0,16);
    loadFromBus(data);
  }
  if (cmd.startsWith("CLK"))
  {
     Serial.println("CLK SENT");
    send_clock();
  }
  if (cmd.startsWith("RST"))
  {
    reset();
  }
  if (cmd.startsWith("LEL"))
  {
    digitalWrite(LE,LOW);
  digitalWrite(_LE,HIGH);
  }
  if (cmd.startsWith("LEH"))
  {
    digitalWrite(LE,HIGH);
    digitalWrite(_LE,LOW);
  }
  
  if (cmd.startsWith("RUN"))
  {
 run();
  }
    if (cmd.startsWith("MAXCLK"))
  {
    max_clock();
  }
 
}

void send_clock()
{
    digitalWrite(CLK,HIGH);
    digitalWrite(CLK,LOW);
}

// note the object is register
void loadFromBus(int data){
  setBusMode(OUTPUT);
  digitalWrite(LE,HIGH);
  digitalWrite(_LE,LOW);
  for(int i = 0; i < 8; ++i)
  {
    digitalWrite(DATA[i],(data >> i)&1);
  }
  send_clock();
  digitalWrite(LE,LOW);
  digitalWrite(_LE,HIGH);
}

int outputToBus(){
  setBusMode(INPUT);
  digitalWrite(OE,HIGH);
  digitalWrite(_OE,LOW);
  int data = 0;
  for(int i = 0; i < 8; ++i)
  {
    data += digitalRead(DATA[i])<<i;
  }
  digitalWrite(OE,LOW);
  digitalWrite(_OE,HIGH);
  return data;
}

void reset(){
  digitalWrite(RST,HIGH);
  digitalWrite(_RST,LOW);
  digitalWrite(RST,LOW);
  digitalWrite(_RST,HIGH);
}

void run(){
  
  while(1){
    
    String cmd = readSerial();
    cmd.toUpperCase();
    if(cmd.length()!=0)
      break;
    for( int x = 0; x < 8; ++x)
  {
     loadFromBus(1 <<x);
     delay(60);
  }
  }
  
}



void max_clock(){
  
  while(1){
    
    String cmd = readSerial();
    cmd.toUpperCase();
    if(cmd.length()!=0)
      break;
    send_clock();   
  
  }}
