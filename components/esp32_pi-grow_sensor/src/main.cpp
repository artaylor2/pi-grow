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

#include "esp32Node.h"

#define uS_TO_S     1000000

void setup() {
    // initialize serial monitor
    Serial.begin(115200);
    delay(1000);
    
    // Configure deep sleep timer wakeup
    esp_sleep_enable_timer_wakeup(8 * uS_TO_S);
    Serial.println("Setup complete");
}

void loop() {
    // Once awake, reconnect wifi and open UDP port
    startWifi();
    
    // Discover broker
    discoverBroker();
    // TODO - Get BME sensor data
    // TODO - Get ADC inputs 0-9

    // // Assemble message
    // String message = id + ',' + WiFi.RSSI() + '\n';

    // // Send message
    // Serial.println("Message = " + message);
    
    // // Broadcast message over UDP
    // client.beginPacket(address, SYSTEM_PORT);
    // client.printf(message.c_str());
    // client.endPacket();
    
    Serial.println("Discovery complete. Sleeping.");
    // Deep sleep
    esp_deep_sleep_start();
}