#include <Arduino.h>
#include <Arduino_JSON.h>
#include "fingerprint.h"
#include "api.h"
#include "oled.h"
#include "Patient.h"



void setup(){
Serial.begin(9600);

while (!initDisplay())
;

while (!initFingerprint())
;

while(!initWifi())
;



}



void loop(){

}