#ifndef API_H
#define API_H
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Arduino_JSON.h>

bool initWifi();
JSONVar fetchPatientData(int id,WiFiClient client,String url,String token);
int FetchAvailableFingerID(WiFiClient client,String url,String token);

#endif