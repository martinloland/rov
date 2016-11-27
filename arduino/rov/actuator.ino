void moveActuator(ACT act) {
  led(act);
  panTilt(act);
  motors(act.mot);
}

void led(ACT act) {
  if (act.led == ON) {
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(LED_PIN, LOW);
  }
}

void panTilt(ACT act) {
  panServo.write(act.pan);
  tiltServo.write(act.tilt);
}

void motors(MOT mot){
  turnMotor(mot.lf, lf_a, lf_b, lf_enb);
  turnMotor(mot.lb, lb_a, lb_b, lb_enb);
  turnMotor(mot.cb, cb_a, cb_b, cb_enb);
  turnMotor(mot.rb, rb_a, rb_b, rb_enb);
}

void turnMotor(int speed, int Apin, int Bpin, int enablePin){
  int forward = true;
  if(speed <= 0){
    forward = false;
  }
  if (forward){
    digitalWrite(Apin, HIGH);
    digitalWrite(Bpin, LOW);
  } else {
    digitalWrite(Apin, LOW);
    digitalWrite(Bpin, HIGH);   
  }
  analogWrite(enablePin, abs(speed));
}

ACT recvSignal(ACT temp) {
  //Incoming: 'ACT,led:1,pan:120,tilt:43,lf:0,rf:0,lb:100,cb:45,rb:110'
  if (Serial.available() > 0) {
    delay(5); // Let the whole string arrive to buffer
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
    // Update actuator class
    temp = stringToClass(inData, temp);
  }

  return temp;
}

ACT stringToClass(char *inData, ACT temp) {
  char *curr;
  char *next;
  char *att;
  int value;

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
    } else if (strcmp(att, "cb") == 0) {
      temp.mot.cb = value;
    } else if (strcmp(att, "rb") == 0) {
      temp.mot.rb = value;
    }
  }

  return temp;
}
