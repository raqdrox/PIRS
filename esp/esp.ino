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

bool enrollFingerprint(){
    //Enroll

    //Get available finger id
    int fingerID = fetchAvailableFingerID()+1;
    if(fingerID == 0){
        Serial.println("Error fetching finger id");
        break;
    }
    Serial.print("Finger ID: ");
    Serial.println(fingerID);

    //Enroll
    printTextToDisplay("Place Finger on sensor",true);
    while (!getFingerprintEnroll(fingerID))
    ;
    
    printTextToDisplay("Enrolled Successfully",true);
    delay(2000);
    return true
}

bool RetrievePatient(){
    //Retrieve
    printTextToDisplay("Place Finger on sensor",true);
    int fingerID = -1;
    while (fingerID == -1) {
        fingerID = getFingerprintID();
    }

    printTextToDisplay("Fetching Patient Data",true);

    JSONVar patientData = fetchPatientData(fingerID);
    if(patientData["Error"] != NULL){
        Serial.println(patientData["Error"]);
        break;
    }
    Patient patient(patientData);
    printTextToDisplay(patient.name,true);
    delay(2000);
    return true;
}
void loop(){

//Ask user for choice 
//1. Enroll
//2. Retrieve

Serial.println("Enter 1 to enroll, 2 to retrieve");
while(!Serial.available());
int choice = Serial.parseInt();

printTextToDisplay("Patient Information Retrieval System",true);

switch (choice)
{
case 1:
    bool result = enrollFingerprint();
    if(result){
        Serial.println("Enrolled Successfully");
    }
    else{
        Serial.println("Error Enrolling");
    }
    break;
case 2:
    bool result=RetrievePatient();
    if(result){
        Serial.println("Retrieved Successfully");
    }
    else{
        Serial.println("Error Retrieving");
    }
    break;
default:
    break;
}


}