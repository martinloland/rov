SENS readSensors() {
  SENS temp;

  temp.pressure = 3024;
  temp.temp = 18.3;
  temp.volt = 10.8;
  temp.gyr.ax = 0;
  temp.gyr.ay = 0;
  temp.gyr.az = 0;
  temp.gyr.compass = 0;

  temp = mpuLoop(temp); // read orientation

  return  temp;
}

ACT communicate(SENS sens) {
  ACT temp;
  if (Serial.available() > 0) {
    //Receive data
    String incoming = Serial.readString();

    // Send data back
    String sending = createString(sens);
    Serial.println(sending);
  }

  return  temp;
}

ACT communicateProto(SENS sens) {
  ACT temp;
  if (Serial.available() > 0) {
    //Receive data
    String incoming = Serial.readString();
  }

  // Send data back
  String sendString = createString(sens);
  Serial.println(sendString);

  return  temp;
}

String createString(SENS sens) {
  String str = "SENSORS,";
  str += "press:";
  str += sens.pressure;
  str += ",temp:";
  str += sens.temp;
  str += ",volt:";
  str += sens.volt;
  str += ",roll:";
  str += sens.gyr.roll;
  str += ",yaw:";
  str += sens.gyr.yaw;
  str += ",pitch:";
  str += sens.gyr.pitch;
  str += ",ax:";
  str += sens.gyr.ax;
  str += ",ay:";
  str += sens.gyr.ay;
  str += ",az:";
  str += sens.gyr.az;
  str += ",compass:";
  str += sens.gyr.compass;

  return str;
}

void moveActuator(ACT act) {

}
