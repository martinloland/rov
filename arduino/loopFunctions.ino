SENS readSensors() {
  SENS temp;

  // These are temporary values, but needs to be changed to actual sensor readings
  temp.pressure = 3024;
  temp.temp = 18.3;
  temp.volt = 10.8;
  temp.curr = 2.12;
  temp.gyr.ax = 0;
  temp.gyr.ay = 0;
  temp.gyr.az = 0;
  temp.gyr.compass = 0;
  temp = mpuLoop(temp); // read orientation

  return  temp;
}

ACT communicate(SENS sens, ACT temp) {
  // Serial will come in the format: 'ACT,led:1,pan:120,tilt:43,lf:0,rf:0,lb:100,rb:110'
  if (Serial.available() > 0) {
    char inData[100]; // Allocate some space for the string
    char inChar; // Where to store the character read
    byte index = 0; // Index into array; where to store the character
    // Read in a whole string
    while (Serial.available() > 0) {
      inChar = Serial.read(); // Read a character
      inData[index] = inChar; // Store it
      index++; // Increment where to write next
      inData[index] = '\0'; // Null terminate the string
    }
    // Update sensors
    temp = stringToClass(inData);
  }

  // Send actuator settings as string
  Serial.println(classToString(sens));

  return temp;
}

ACT stringToClass(char *inData) {
  char *curr;
  char *next;
  char *att;
  int value;
  ACT temp;

  next = strstr(inData, ",") + 1;

  while (next - 1 != NULL) {
    curr = next;
    // Prepare next iteration
    next = strstr(next, ",") + 1;
    // Insert NULL character at delim
    strcpy(next - 1, "\0");
    // Update the corrosponding attribute
    att = strtok(curr, ":");
    value = atol(strtok(NULL, ":"));
    if (strcmp(att, "led") == 0) {
      temp.led = value;
    } else if (strcmp(att, "pan") == 0) {
      temp.pan = value;
    } else if (strcmp(att, "tilt") == 0) {
      temp.tilt = value;
    } else if (strcmp(att, "lf") == 0) {
      temp.mot.lf = value;
    } else if (strcmp(att, "rf") == 0) {
      temp.mot.rf = value;
    } else if (strcmp(att, "lb") == 0) {
      temp.mot.lb = value;
    } else if (strcmp(att, "rb") == 0) {
      temp.mot.rb = value;
    }
  }

  return temp;
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

void moveActuator(ACT act) {
  led(act);
  panTilt(act);
}

void panTilt(ACT act) {
  panServo.write(act.pan);
  //tiltServo.write(act.tilt);
}

void led(ACT act) {
  if (act.led == 1) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
