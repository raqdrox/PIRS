#include <Arduino.h>
#include <Arduino_JSON.h>
#include "fingerprint.h"
#include "api.h"
#include "oled.h"
#include "Patient.h"



void setup(){
Serial.begin(9600);
Serial.println("Start");
while (!initDisplay())
{Serial.print(".");}

while (!initFingerprint())
{Serial.print(".");}

while(!initWifi())
{Serial.print(".");}



}



Patient mapJSONVarToPatient(JSONVar patientData){
    struct Patient patient;
    patient.name = (const char*)patientData["name"];
    patient.age = (const char*)patientData["age"];
    patient.bloodgroup = (const char*)patientData["medical_data"]["blood_group"];
    patient.diseases = (const char*)patientData["medical_data"]["diseases"];
    patient.allergies = (const char*)patientData["medical_data"]["allergies"];
    patient.relativename = (const char*)patientData["emergency_contact"]["name"];
    patient.relativecontact = (const char*)patientData["emergency_contact"]["phone"];
    return patient;
}

bool enrollFingerprint(){
    //Enroll

    //Get available finger id
    int fingerID = fetchAvailableFingerID()+1;
    if(fingerID == 0){
        Serial.println("Error fetching finger id");
        return false;
    }
    Serial.print("Finger ID: ");
    Serial.println(fingerID);

    //Enroll
    printTextToDisplay("Place Finger",true);
    delay(100);
    while (!getFingerprintEnroll(fingerID))
    ;
    printTextToDisplay("Enrolled ID : "+fingerID,true);

    delay(10000);
    return true;
}

bool RetrievePatient(){
    
    printTextToDisplay("Place Finger",true);
    int fingerID = -1;
    while (fingerID==-1){
      fingerID=getFingerprintID();
      delay(100);
      }

    if(fingerID==-2){
      printTextToDisplay("No Match Found",true);
      delay(2000);
      return false;
}
    printTextToDisplay("Fetching Patient Data",true);

    JSONVar patientData = fetchPatientData(fingerID);
    if(patientData.hasOwnProperty("Error")){

        Serial.println(patientData["Error"]);
        return false;
    }    

    struct Patient patient = mapJSONVarToPatient(patientData);
    printPatientData(patient);
    delay(10000);
    return true;
}



void loop(){

Serial.println("Enter 1 to enroll, 2 to retrieve, 3 to delete database");
printTextToDisplay("      Patient\n\n      Information\n\n      Retrieval\n\n      System",true);

while(!Serial.available());
int choice = Serial.parseInt();

bool result =false;
switch (choice)
{
case 1:
    result = enrollFingerprint();
    if(result){
        Serial.println("Enrolled Successfully");
    }
    else{
        Serial.println("Error Enrolling");
    }
    break;
case 2:
    result=RetrievePatient();
    if(result){
        Serial.println("Retrieved Successfully");
    }
    else{
        Serial.println("Error Retrieving");
    }
    break;
case 3:
    deleteAll();
    break;
default:
    break;
}


}