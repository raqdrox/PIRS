#include "api.h"


//----------------API and WIFI----------------
ESP8266WiFiMulti WiFiMulti;

const char* ssid = "Frost";
const char* password = "karan@123";

String token="Token cb6fd4778f21f2ac38b15423e445828bf029e7a6";
String fetch_patient_url = "http://192.168.1.12:8000/apis/mcu/fingerprints/getpatientfromfid/";
String fetch_available_fingerid_url = "http://192.168.1.12:8000/apis/mcu/fingerprints/getavailableid/";
String clear_unused_ids = "http://192.168.1.12:8000/apis/mcu/fingerprints/clearunused/";

//-------------------------------------------


bool initWifi(){
  Serial.println("Init Wifi");

  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);
  return true;
}

JSONVar fetchPatientData(int id){
  JSONVar payloadJson = JSON.parse("{}");
  if ((WiFiMulti.run() == WL_CONNECTED)) {
    WiFiClient client;
    HTTPClient http;
    
    if (http.begin(client, fetch_patient_url+id+"/")) {  
      http.addHeader("Authorization",token);

      int httpCode = http.GET();

      if (httpCode > 0) {
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          String payload = http.getString();
          payloadJson= JSON.parse(payload);
        }
      } else {
          payloadJson = JSON.parse("{\"Error\":\"Request Error\"}");
          
      }

      http.end();
    } else {
        payloadJson = JSON.parse("{\"Error\":\"Unable to Connect\"}");
    }
  
  }else{
    payloadJson = JSON.parse("{\"Error\":\"Wifi not connected\"}");
  }
  return payloadJson;
  
}

int fetchAvailableFingerID(){
  int id = -1;
  if ((WiFiMulti.run() == WL_CONNECTED)) {
    WiFiClient client;
    HTTPClient http;
    
    if (http.begin(client, fetch_available_fingerid_url)) {  
      http.addHeader("Authorization",token);

      int httpCode = http.GET();

      if (httpCode > 0) {
        Serial.printf("[HTTP] GET... code: %d\n", httpCode);
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          String payload = http.getString();

          id= JSON.parse(payload)["id"];
        }
      } else {
          id=-1;
          
      }

      http.end();
    } else {
        id=-2;
    }
  }else{id=-3;}
  return id;
}