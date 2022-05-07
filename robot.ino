/**********************************************************************
  Product     : Freenove 4WD Car for UNO
  Auther      : www.freenove.com
  Modification: 2019/08/03
**********************************************************************/
#define PIN_DIRECTION_RIGHT 3
#define PIN_DIRECTION_LEFT  4
#define PIN_MOTOR_PWM_RIGHT 5
#define PIN_MOTOR_PWM_LEFT  6

void setup() {
  Serial.begin(19200);
  Serial.flush();
  pinMode(PIN_DIRECTION_LEFT, OUTPUT);
  pinMode(PIN_MOTOR_PWM_LEFT, OUTPUT);
  pinMode(PIN_DIRECTION_RIGHT, OUTPUT);
  pinMode(PIN_MOTOR_PWM_RIGHT, OUTPUT);
}

boolean isRunning = true;

void motorRun(int speedl, int speedr) {
  int dirL = 0, dirR = 0;
  if (speedl > 0) {
    dirL = 0;
  }
  else {
    dirL = 1;
    speedl = -speedl;
  }
  if (speedr > 0) {
    dirR = 1;
  }
  else {
    dirR = 0;
    speedr = -speedr;
  }
  digitalWrite(PIN_DIRECTION_LEFT, dirL);
  digitalWrite(PIN_DIRECTION_RIGHT, dirR);
  analogWrite(PIN_MOTOR_PWM_LEFT, speedl);
  analogWrite(PIN_MOTOR_PWM_RIGHT, speedr);
}

void runRobot() {
    if(Serial.available() > 0) {
    //FRONT
      int val = Serial.read();
      if(val == '1') {
        motorRun(110, 110);
        Serial.flush();
      }
      // LEFT
      if(val == '2') {
        motorRun(-125, 125);
        Serial.flush();
      }
      //RIGHT
      if(val == '3') {
        motorRun(125, -125);
        Serial.flush();
      }
      //BACK
      if(val == '4') {
        motorRun(-125, -125);
        Serial.flush();
      }
      //STOP
      if(val == '5') {
        motorRun(0, 0);
        Serial.flush();
      }
      if(val == '9') {
        isRunning = false;
        Serial.flush();
      }
  }
}


void loop() {
  while(isRunning) {
    runRobot();
  }
}