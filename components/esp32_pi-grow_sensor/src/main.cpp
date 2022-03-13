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

#define uS_to_S 1000000

// router connection information
const char *ssid_Router     = "garden_test";
const char *password_Router = "177811aB+";

// unit identifier 
const String id = WiFi.macAddress();

/* User Functions */

/**
 * @brief Attempt to start a wifi connection
 * 
 * @param timeout Timeout of attempt, in milliseconds
 * @return true     Connection successful
 * @return false    Connection failed
 */
// TODO - Rework to work with non-const ssid + pwd

bool startWifi(int timeout = 8000) {
    // initialize wifi
    WiFi.begin(ssid_Router, password_Router);
    Serial.println(String("Connecting to ") + ssid_Router);

    // wait for connection verification or timeout
    while (WiFi.status() != WL_CONNECTED && timeout > 0)
    {
        delay(500);
        Serial.print('.');
        timeout -= 500;
    }

    if (WiFi.status() == WL_CONNECTED)
    {
        // report connection success
        Serial.println("\nConnected @ ");
        Serial.println(WiFi.localIP());
        Serial.println("Setup complete");

        return true;
    }
    else
    {
        // report connection failure
        Serial.println("Connection attempt timed out");
        return false;
    }
}

/* Main Functions */

void setup() {
    // initialize serial monitor
    Serial.begin(115200);
    delay(1000);
    Serial.println("Setup started");
    
    // Set sleep length (milliseconds)
    int sleepTimer = 5 * uS_to_S;

    // Configure esp32 timer wakeup
    esp_sleep_enable_timer_wakeup(sleepTimer);
}

void loop() {
 
    Serial.println("Wake Code " + esp_sleep_get_wakeup_cause());
    // Once awake, reconnect wifi
    startWifi();    
    // TODO - Get BME sensor data
    // TODO - Get ADC inputs 0-9

    // Assemble message
    String message = id + ',' + WiFi.RSSI() + '\n';

    // Send message
    // TODO - Configure to communicate over wifi
    Serial.println("Message = " + message);
    
    // Deep sleep
    esp_deep_sleep_start();
}