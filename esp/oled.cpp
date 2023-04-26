#include "oled.h"

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

bool initDisplay(){
  Serial.begin(9600);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    return false;
  }
  display.setTextSize(1);             
  display.setTextColor(SSD1306_WHITE);      
  display.setCursor(0,0);  
  display.clearDisplay();
  
  return true;
}

void printTextToDisplay(String text,bool clear){
  if(clear) display.clearDisplay();

  display.println(text);

  display.display();

}


void printPatientData(struct Patient patient,bool clear){
  if(clear) display.clearDisplay();
  display.setTextSize(1);             
  display.setTextColor(SSD1306_WHITE);      
  display.setCursor(0,0);  
  printTextToDisplay("Name: "+patient.name);
  
  printTextToDisplay("Age: "+patient.age);

  printTextToDisplay("Blood Group: "+patient.bloodgroup);

  printTextToDisplay("Diseases: "+patient.diseases);

  printTextToDisplay("Allergies: "+patient.allergies);

  printTextToDisplay("Rel Name: "+patient.relativename);
  
  printTextToDisplay("Contact: "+patient.relativecontact);
}