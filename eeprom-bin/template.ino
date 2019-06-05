// AT28C EEPROM Programmer for Arduino Mega
// Colin Maykish (cmaykish.com)
// 04/17/2016
// Width in bits of address bus (64K has 13, 256K has 15)
//2019-04-06 21:26:50
// AI Reference from (https://github.com/crmaykish/AT28C-EEPROM-Programmer-Arduino)
// add SDP /page write /verfiy
#include <avr/pgmspace.h>
const int ADDR_BUS_WIDTH = 13;

// Chip Enable
const int CE = 2;
// Ouput Enable
const int OE = 3;
// Write Enable
const int WE = 4;
// Data bus pins
const int I[] = { 22, 23, 24, 25, 26, 27, 28, 29 };
// Address bus pins
const int A[] = { 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42 };

const int hex_len  = {size};
const byte hex_data[hex_len] PROGMEM  = {{content}};


void setup() {
  Serial.begin(9600);

  // Define control pins and turn them all off
  pinMode(OE, OUTPUT);
  pinMode(WE, OUTPUT);
  pinMode(CE, OUTPUT);
  digitalWrite(OE, HIGH);
  digitalWrite(WE, HIGH);
  digitalWrite(CE, HIGH);
  // Set address bus to outputs
  for (int i = 0; i < ADDR_BUS_WIDTH; i++) {
    pinMode(A[i], OUTPUT);
  }

  delay(100);
  close_SDP();
  delay(100);
  
  Serial.println("Writing...");
  write_hex();
  Serial.println("Verifying...");
  verify();
  Serial.println("Enable SDP...");
  enable_SDP();
  Serial.println("Completed");

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
  if (cmd.startsWith("R"))
  {
    int addr = strtol(cmd.substring(first).c_str(),0,16);
    int data = readByte(addr);
    Serial.print("READ 0x");
    Serial.print(addr,HEX);
    Serial.print(" : 0x");
    Serial.println(data,HEX);
  }
  if (cmd.startsWith("W"))
  {

    int addr = strtol(cmd.substring(first, last).c_str(),0,16);
    int data =  strtol(cmd.substring(last).c_str(),0,16);
    writeByte(addr, data);
    int data_confirm = readByte(addr);
    if (data_confirm == data)
    {
      Serial.print("WRITE 0x");
      Serial.print(addr, HEX);
      Serial.print(" : 0x");
      Serial.println(data, HEX);
    }
    else
    {
      Serial.print("WRITE FAILED ADDR 0x");
      Serial.print(addr, HEX);
      Serial.print(" : 0x");
      Serial.print(data_confirm, HEX);
      Serial.print("(0x");
      Serial.print(data, HEX);
      Serial.println(" is the expected value)");
    }
  }
  if (cmd.startsWith("CSDP"))
  {
    Serial.println("close SDP");
    close_SDP();
  }
  if (cmd.startsWith("ESDP"))
  {
    Serial.println("enable SDP");
    enable_SDP();
  }
}



void write_hex() {
  for (int x = 0 ; x < hex_len; ++x)
  {
    if (x != 0 &&  x % 64 == 0)
    {
      delay(20);
    }
    pagestep(x, pgm_read_byte(hex_data+x));
  }
  delay(20);
}


void verify() {
  for (int x = 0 ; x < hex_len; ++x)
  {
    int data = readByte(x);
    if (data != pgm_read_byte(hex_data+x)) {
      Serial.println("addr " + String(x) + " data is " + String(data) + "(" + String(pgm_read_byte(hex_data + x)) + " is correct)");
      return;
    }
  }
}


void pagestep(int addr, int data) {
  for (int i = 0; i < 8; i++) {
    digitalWrite(I[i], (data & (1 << i)) > 0);
  }
  for (int i = 0; i < ADDR_BUS_WIDTH; i++) {
    digitalWrite(A[i], (addr & (1 << i)) > 0);
  }

  digitalWrite(WE, LOW);
  digitalWrite(CE, LOW);
  delayMicroseconds(1);
  digitalWrite(CE, HIGH);
  digitalWrite(WE, HIGH);
  delayMicroseconds(1);
}


void close_SDP() {
  digitalWrite(OE, HIGH);
  setDataBusMode(OUTPUT);
  pagestep(0x1555, 0xAA);
  pagestep(0x0AAA, 0x55);
  pagestep(0x1555, 0x80);
  pagestep(0x1555, 0xAA);
  pagestep(0x0AAA, 0x55);
  pagestep(0x1555, 0x20);
  delay(20);
}

void enable_SDP() {
  digitalWrite(OE, HIGH);
  setDataBusMode(OUTPUT);
  pagestep(0x1555, 0xAA);
  pagestep(0x0AAA, 0x55);
  pagestep(0x1555, 0xA0);
  delay(20);
}

// Set data bus to INPUT or OUTPUT
void setDataBusMode(int mode) {
  if (mode == INPUT || mode == OUTPUT) {
    for (int i = 0; i < 8; i++) {
      pinMode(I[i], mode);
    }
  }
}

// Write an address to the address bus
void setAddress(int addr) {
  for (int i = 0; i < ADDR_BUS_WIDTH; i++) {
    digitalWrite(A[i], (addr & (1 << i)) > 0  ? HIGH : LOW);
  }
}

void writeByte(int addr, byte val) {
  digitalWrite(OE, HIGH);
  setDataBusMode(OUTPUT);
  setAddress(addr);

  // Send data value to data bus
  for (int i = 0; i < 8; i++) {
    int a = (val & (1 << i)) > 0;
    digitalWrite(I[i], a);
  }

  // Commit data write
  digitalWrite(WE, LOW);
  digitalWrite(CE, LOW);
  delay(1);
  digitalWrite(CE, HIGH);
  digitalWrite(WE, HIGH);
  delay(10);
}


byte readByte(int addr) {
  byte data = 0;

  setDataBusMode(INPUT);

  // Write the addr
  for (int i = 0; i < ADDR_BUS_WIDTH; i++) {
    int a = (addr & (1 << i)) > 0;
    digitalWrite(A[i], a);
  }

  digitalWrite(CE, LOW);
  digitalWrite(OE, LOW);
  delayMicroseconds(10);

  // Read data bus
  for (int i = 0; i < 8; i++) {
    int d = digitalRead(I[i]);
    data += (d << i);
  }

  digitalWrite(OE, HIGH);
  digitalWrite(CE, HIGH);

  return data;
}