#define FALSE 0
#define TRUE 1
#define NO 0
#define YES 1
#define OFF 0
#define ON 1
#define SENSOR 0
#define ACTUATOR 1

// ACTUATOR PINS
// Pin 2 is already used bu MPU
#define PAN_PIN 9
#define TILT_PIN 10
#define LED_PIN 13

#define lf_a A2 // Same rf_a
#define lf_b A3 // Same rf_b
#define lb_a 8
#define lb_b 7
#define cb_a 4
#define cb_b 2
#define rb_a A0
#define rb_b A1

#define lf_enb 3 // Same rf_enb
#define lb_enb 11 //stor
#define cb_enb 6
#define rb_enb 5 //stor

// SENSOR PINS
#define VOLT_PIN A7
#define TEMP_PIN A2
#define PRESS_PIN A1
#define CURR_PIN A0

// Pressure
byte address[8] = {0x28, 0xFF, 0x51, 0x70, 0x84, 0x16, 0x4, 0x63};
OneWire onewire(PRESS_PIN);
DS18B20 tempSensor(&onewire);

// Structures
typedef struct MOT{
	int lf = 0; // -255 ~ 255
	int rf = 0; // -255 ~ 255
	int lb = 0; // -255 ~ 255
	int cb = 0; // -255 ~ 255
	int rb = 0; // -255 ~ 255	
}MOT;

typedef struct GYR{
	float roll = 0; // +/- 180
	float yaw = 0; // +/- 180
	float pitch = 0; // +/- 180
	int ax = 0;
	int ay = 0;
	int az = 0;
	int compass = 0;
}GYR;

typedef struct ACT{
	int led = 0; // 0-1
	int pan = 90; // 0-179
	int tilt = 90; // 0-179
	MOT mot;
}ACT;

typedef struct SENS{
	float pressure = 0;
	float temp = 0;
	float volt = 0;
	float curr = 0;
	GYR gyr;
}SENS;
