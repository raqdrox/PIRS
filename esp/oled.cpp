#include "oled.h"

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

bool initDisplay(){
  Serial.println("Init Display");

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    return false;
  }
  display.display();
  delay(2000); // Pause for 2 seconds

  display.clearDisplay();

  return true;
}
void clearScreen(){
  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextColor(SSD1306_WHITE);
  display.cp437(true); 
  display.display();
}

void printTextToDisplay(String text,bool clear){  
  if(clear) clearScreen();

  display.println(text);

  display.display();

}



void printPatientData(struct Patient patient){
  clearScreen();

  display.setTextSize(1);      // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.setCursor(0, 0);     // Start at top-left corner
  display.cp437(true);         // Use full 256 char 'Code Page 437' font

  printTextToDisplay("Name: "+patient.name);
  
  printTextToDisplay("Age: "+patient.age);

  printTextToDisplay("Blood Group: "+patient.bloodgroup);

  printTextToDisplay("Diseases: "+patient.diseases);

  printTextToDisplay("Allergies: "+patient.allergies);

  printTextToDisplay("Cont. Name: "+patient.relativename);
  
  printTextToDisplay("Contact: "+patient.relativecontact);
}