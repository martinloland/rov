void startPins() {
  pinMode(PAN_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void initialize() {
  panServo.attach(PAN_PIN);
  //panServo.attach(tiltPin);
  mpuSetup();
}
