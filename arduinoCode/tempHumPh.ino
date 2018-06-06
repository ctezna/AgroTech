#include <TroykaDHT.h>
DHT dht(5, DHT21);
int dial = 1;
int sensor = 0;
int pwr = 2;
double phVal = 0.0;
double gndHumVal = 0.0;
double gndHum = 0.0;
double ph = 0.0;
double temp = 0.0;
double hum = 0.0;
int inbyte = 0;
void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(pwr,OUTPUT);
}

double norm(int val, double oldmax, double oldmin, double newmax, double newmin) {
  double oldrange = oldmax - oldmin;
  double newrange = newmax - newmin;
  double res = 0.0;
  res = (((val - oldmin) * newrange) / oldrange) + newmin;
  return res;
}


void loop() {
  digitalWrite(pwr,1);  
  dht.read();
  phVal = analogRead(dial);
  gndHumVal = analogRead(sensor);
  gndHum = 100.0 - norm(gndHumVal, 1023, 0, 100, 0);
  ph = norm(phVal, 1023, 0, 9, 4);
  if (Serial.available() > 0) {
    inbyte = Serial.read();
  }
  if (inbyte == 0) {
    switch (dht.getState()) {
      case DHT_OK:
        temp = dht.getTemperatureC();
        hum = dht.getHumidity();
        Serial.print("T=");
        if(temp < 10 and temp >= 0){
          Serial.print(0);
        }
        Serial.print(temp);
        Serial.print("H=");
        if(hum < 100){
          Serial.print(0);
        }
        if(hum < 10){
          Serial.print(0);
        }
        Serial.print(hum);
        Serial.print("P=");
        Serial.print(ph);
        Serial.print("G=");
        if(gndHum < 100){
          Serial.print(0);
        }
        if(gndHum < 10){
          Serial.print(0);
        }
        Serial.print(gndHum);
        break;
      case DHT_ERROR_CHECKSUM:
        Serial.print("ER-CS");
        break;
      case DHT_ERROR_TIMEOUT:
        Serial.print("ER-TO");
        break;
      case DHT_ERROR_NO_REPLY:
        Serial.print("ER-SNC");
        break;
    }
    inbyte = 0;
  }
  delay(2000);
}
