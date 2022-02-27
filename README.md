# pi-grow
---
## Summary:
The purpose of Pi-Grow is to provide a flexible framework for building an automated home gardening system.

Individual components inheret from specific types of interfaces and are configured using a YAML formatted configuration file.

The system is being designed with Raspberry Pi in mind, but it built off of CircuitPython libraries with an eye towards support other single-board computers as well.

This is primarily a learning-oriented project so it is likely to evolve and shift over time as interest and areas of study shift as well. 

## Features:
- Simple proof-of-concept with an analog soil moisture sensor running on MCP3008 and a 3.3v relay
- Flexible configuation file system to allow for component configuration

## To-Do:
- ~~Simple proof-of-concept with an analog soil moisture sensor running on MCP3008 and a 3.3v relay~~
- ~~Flexible configuation file system to allow for component configuration~~
- Logging system for monitoring and tracking system components
- Onboard GPIO device support for Raspberry Pi
  - Relay
  - OLED Display
- Oboard MCP3008 ADC device support for Raspberry Pi
  - Soil moisture sensor
- ESP32 Support
  - ADC soil moisture sensor
  - Climate sensor
  - Communication over serial
  - Solar-power functionality
    - Battery tracking
  - Deep sleep system
  - YAML-based configurability
- Water reservoir monitoring
- Climate monitoring

- User-friendly GUI for configuring systems
- RPC interface for remote systems management
- Web front-end for monitoring systems on a local network
