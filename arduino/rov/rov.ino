#include <OneWire.h>
#include <DS18B20.h>
#include <Servo.h>
#include <Wire.h> //Gyroscope
#include "rov.h" // Main header file
#include "mpu01.h" // MPU6050 header file
Servo panServo;
Servo tiltServo;

int mode = SENSOR; // Change depending on which arduino
// Create structures that hold sensor values and actuator positions
SENS sens;
ACT act;

void setup() {
  Serial.begin (115200); //9600 115200
  startPins();
  initialize();
}

void loop() {
  if (mode == SENSOR) {
    // read sensor values
    sens = readSensors(sens);

    // send sensor values
    sendSignal(sens);

  } else if (mode == ACTUATOR) {
    // receive actuator settings
    act = recvSignal(act);
    // move actuators
    moveActuator(act);
  }
}

float mapFloat(float x, float lowIn, float highIn, float lowOut, float highOut) {
  return (x - lowIn) * (highOut - lowOut) / (highIn - lowIn) + lowOut;
}
