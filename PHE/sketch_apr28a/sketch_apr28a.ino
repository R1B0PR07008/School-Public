#include <Servo.h>

Servo myServo;

// int const potPin = A0;
// int potVal;
// int angle;

void setup() {
  // put your setup code here, to run once:

  myServo.attach(9);

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  // potVal = analogRead(potPin);
  // Serial.println("potVal: ");
  // Serial.print(potVal);

  // angle = map(potVal, 0, 1023, 0, 179);
  // Serial.print(", angle: ");
  // Serial.print(angle);

  // myServo.write(angle);
 

  myServo.write(90);
  delay(100);
    Serial.println(myServo.read());
  // myServo.write(45);
  // delay(100);
  // myServo.write(90);
  // delay(100);
  // myServo.write(135);
  // delay(100);
  myServo.write(180);
  //  delay(100);

  Serial.println(myServo.read());
}
