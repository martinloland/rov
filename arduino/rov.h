#define FALSE 0
#define TRUE 1
#define NO 0
#define YES 1
#define OFF 0
#define ON 1

// Pins
// Pin 2 is already used bu MPU
#define PAN_PIN 9

// Structures
typedef struct MOT{
	int lf; // 0-255
	int rf; // 0-255
	int lb; // 0-255
	int rb; // 0-255	
}MOT;

typedef struct GYR{
	float roll; // +/- 180
	float yaw; // +/- 180
	float pitch; // +/- 180
	int ax;
	int ay;
	int az;
	int compass;
}GYR;

typedef struct ACT{
	int led; // 0-1
	int pan; // 0-179
	int tilt; // 0-179
	MOT mot;
}ACT;

typedef struct SENS{
	float pressure;
	float temp;
	float volt;
	float curr;
	GYR gyr;
}SENS;
