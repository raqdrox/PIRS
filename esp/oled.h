#ifndef OLED_H
#define OLED_H
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "Patient.h"



bool initDisplay();
void printTextToDisplay(String text,bool clear=false);
void printPatientData(struct Patient patient);
void clearScreen();

#endif