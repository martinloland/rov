void startPins() {
  if (mode == SENSOR) {
    pinMode(VOLT_PIN, INPUT);
    pinMode(TEMP_PIN, INPUT);
    pinMode(PRESS_PIN, INPUT);
    pinMode(CURR_PIN, INPUT);
  }

  else if (mode == ACTUATOR) {
    pinMode(PAN_PIN, OUTPUT);
    pinMode(TILT_PIN, OUTPUT);
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(LED_PIN, OUTPUT);

    pinMode(lf_a, OUTPUT);
    pinMode(lf_b, OUTPUT);
    pinMode(lb_a, OUTPUT);
    pinMode(lb_b, OUTPUT);
    pinMode(cb_a, OUTPUT);
    pinMode(cb_b, OUTPUT);
    pinMode(rb_a, OUTPUT);
    pinMode(rb_b, OUTPUT);

    pinMode(lf_enb, OUTPUT);
    pinMode(lb_enb, OUTPUT);
    pinMode(cb_enb, OUTPUT);
    pinMode(rb_enb, OUTPUT);
  }
}

void initialize() {
  panServo.attach(PAN_PIN);
  tiltServo.attach(TILT_PIN);
  mpuSetup();
	tempSensor.begin();
  tempSensor.request(address);
}
