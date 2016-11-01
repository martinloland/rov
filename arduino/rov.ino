#include "arduinoRov.h"
#include "mpu01.h" // MPU6050 header file
#include <Servo.h>
#include <Wire.h> //Gyroscope
Servo panServo;
Servo tiltServo;

int temp;

// Create structures that hold sensor values and actuator positions
SENS sens;
ACT act;

void setup(){
	Serial.begin (115200); //9600 115200
	startPins();
	initialize();
}

void loop(){
	sens = readSensors(); // Read sensors values
	act = communicateProto(sens); // Send sensor values and receive actuator values
	moveActuator(act); // Update position of actuators
}
