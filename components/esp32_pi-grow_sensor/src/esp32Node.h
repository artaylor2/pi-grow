/**
 * @file esp32Node.h
 * @author Taylor, Alixandra (artaylor2@students.nic.edu)
 * @brief ESP32 sensor node declarations
 * @version 0.1
 * @date 2022-03-14
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifndef ESP32NODE
#define ESP32NODE

#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <string>

// Function declarations
IPAddress discoverBroker();
bool startWifi(int timeout = 8000);
bool transmitMessage(String message, IPAddress target);
bool getSensors();

#endif