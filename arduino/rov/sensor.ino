SENS readSensors(SENS temp) {
  temp.pressure = readPressure();
  temp.temp = readTemp();
  temp.volt = readVolt();
  temp.curr = readCurrent();
  temp = mpuLoop(temp); // read orientation

  return  temp;
}

float readPressure(){
	float reading = analogRead(PRESS_PIN);
  float atmPress = mapFloat(reading, 0.0, 1000.0, 160.0, 2467.0);
	return atmPress;
}

float readTemp(){
  if (tempSensor.available())
  {
    float temperature = tempSensor.readTemperature(address);
    tempSensor.request(address);
		return temperature;
  }
}

float readCurrent(){
	// Takes the average of 1000 readings
	float average = 0;
  int loops = 50;
  for(int i = 0; i < loops; i++) {
    average = average + (.044 * analogRead(CURR_PIN) -3.78) / loops;
  }
  return average;
}

float readVolt(){
	// Read one cell and multiply by three to get aprox whole battery
	float measure = analogRead(VOLT_PIN);
	float voltage = mapFloat(measure, 0.0, 1023.0, 0.0, 5.0);
	return voltage*3.0;
}

void sendSignal(SENS outgoing) {
  
  // Send actuator settings as string
  Serial.println(classToString(outgoing));
}

String classToString(SENS sens) {
  String str = "SENSORS,";
  str += "press:";
  str += sens.pressure;
  str += ",temp:";
  str += sens.temp;
  str += ",volt:";
  str += sens.volt;
  str += ",curr:";
  str += sens.curr;
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
