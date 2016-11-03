#include "rov.h" // Main header file
#include "mpu01.h" // MPU6050 header file
#include <Servo.h>
#include <Wire.h> //Gyroscope
Servo panServo;
Servo tiltServo;

// Create structures that hold sensor values and actuator positions
SENS sens;
ACT act;

void setup() {
  Serial.begin (115200); //9600 115200
  startPins();
  initialize();
}

void loop() {
  sens = readSensors(); // Read sensors values
  act = communicate(sens, act); // Send sensor values and receive actuator values if new
  moveActuator(act); // Update position of actuators
}
