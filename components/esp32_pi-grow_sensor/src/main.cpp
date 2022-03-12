/**
 * @file main.cpp
 * @author Taylor, Alixandra (artaylor2@students.nic.edu)
 * @brief An ESP32 sensor for the pi-grow logging and monitoring system
 * @version 0.1
 * @date 2022-03-04
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include <Arduino.h>
#include <WiFi.h>

# router connection information
const char *ssid_Router     "*****";
const char *password_Router "*****";

void setup() {
    // initialize serial monitor
    Serial.begin(115200);
    delay(2000);
    Serial.println("Setup started");
    
    // initialize wifi
    WiFi.begin(ssid_Router, password_Router);
    Serial.println(String("Connecting to ") + ssid_Router);

    // wait for connection verification
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print('.');
    }

    // report connection success
    Serial.println("\nConnected @ ");
    Serial.println(WiFi.localIP());
    Serial.println("Setup complete");
}

void loop() {
    // put your main code here, to run repeatedly:
    // Get ADC inputs 0-7

    // Assemble message

    // Send message

    // Deep sleep for 1 cycle



}