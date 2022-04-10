#include "esp32Node.h"

#define SYSTEM_PORT     40555

// Message tag constants
#define MESS_DISCO  "1"  // Message is a discovery query
#define ACK_DISCO   "2"  // Discovery query acknowledgement
#define MESS_DATA   "3"  // Message contains data
#define ACK_DATA    "4"  // Data receipt acknowledgement (Unused)
#define MAGIC       "425"
// router and socket connection information
// const char *ssid_Router     = "garden_test";
// const char *password_Router = "177811aB+";

const char *ssid_Router     = "The Kathouse 2.4";
const char *password_Router = "PASSWORDallLowercase";

const String magic = "4235";
const String ack_disco = "2";
// const char *address         = "192.168.4.255";
const char *address         = "192.168.1.255";

// Unique unit identifier
const String id = WiFi.macAddress();

// Deep-sleep-proofed variable for previously contacted broker's address
// Initialized as a null address
RTC_DATA_ATTR IPAddress prevBroker(IPADDR_ANY);

/**
 * @brief Send a discovery broadcast to pi-grow brokers on the network and return the address
 * 
 * @return IPAddress Address of first discovered broker
 */
IPAddress discoverBroker() {
    // Create dummy address and message buffer
    IPAddress brokerAddress(IPADDR_ANY);
    char packetBuffer[64];
    int packetLen = 0;

    // If Wifi is connected or can be successfully connected
    if (WiFi.status() == WL_CONNECTED || startWifi()) {
        // Start UDP client and message packet
        WiFiUDP client;
        client.begin(SYSTEM_PORT);
        client.beginPacket(IPADDR_BROADCAST, SYSTEM_PORT);

        // Send a discovery message to the network's broadcast address
        String message = magic + id;
        Serial.println("Transmitting: " + message); 
        client.print(message);
        client.endPacket();
        
        // Wait for acknowledgement
        for(int i = 0; i < 10; i++) {
            if(client.parsePacket())
            {
                packetLen = client.read(packetBuffer, 64);
                if (packetLen > 0) {
                    packetBuffer[packetLen] = 0;
                }
                
                Serial.println("Received Message:");
                Serial.println(packetBuffer);

                if(strcmp(packetBuffer, (magic + ack_disco).c_str()) == 0) {
                    brokerAddress = IPAddress(client.remoteIP());
                    Serial.print("Confirmation received. Host @ ");
                    Serial.println(brokerAddress);
                    break;
                }
            }
            delay(100);
        }
    }

    // Return the broker address
    return brokerAddress;
}

bool getSensors() {
    return false;
}

bool startWifi(int timeout) {
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
        Serial.println("[ERROR][WIFI] Connection attempt timed out");
        return false;
    }
}

bool transmitMessage(String message, IPAddress target) {
    return false;
}