/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-serial-plotter
 */

void setup() {
  Serial.begin(9600); 
}

void loop() {
  int mic1 = analogRead(A0);
  int mic2 = analogRead(A1);
  int mic3 = analogRead(A2);
  int mic4 = analogRead(A3);
  int mic5 = analogRead(A4);
  int mic6 = analogRead(A5);

  Serial.print(String(mic1) + "\t" +
               String(mic2) + "\t" +
               String(mic3) + "\t" +
               String(mic4) + "\t" +
               String(mic5) + "\t" +
               String(mic6) + "\r\n");

  delay(3);
}
