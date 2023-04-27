#ifndef FINGERPRINT_H
#define FINGERPRINT_H
#include <Adafruit_Fingerprint.h>

bool initFingerprint();

uint8_t getFingerprintEnroll(uint8_t id);
int getFingerprintID();
void deleteAll();
#endif