import os
import time
import yaml

import logger as log
import registrar

from components import gpio
from components import mcp3008

# Component key constants
KEYS = {
    'soil_sensor': mcp3008.SoilSensor,
    'gpio_relay': gpio.GPIORelay
}

# YAML file loader
def load_yaml(config):
    with open(config) as file:
        config = yaml.safe_load(file)

    return config

# Initiate component registrar
reg = registrar.Registrar()

# Load config file
config = load_yaml('config.yaml')

# initiate logger
logger = log.Logger(config)

# Set default logging interval
log_interval = 300
log_time = time.time()

for c in config:
    print(c)
    if c in KEYS:
        print("Creating:", config[c])
        new = KEYS[c](config[c])
        reg.register(config[c]['key'], new)

    elif c == "log_interval":
        print("LOG INTERVAL SET")
        log_interval = config[c]
    
    else:
        print("[ERROR]: Invalid component key: ",c)
        
# Main loop
while 1:
    # Print current system status
    os.system('clear')
    print("==========")
    for n in reg.enum_keys():
        reg.get(n).update()

        print(reg.get(n).asdict())
        print("\n")

        # If log timer has expired then log the current component status
        if (time.time() - log_time) > log_interval:
            print("Log dump")
            logger.log(n, reg.get(n).asdict())

    print("log interval: ", log_interval )
    # Reset log timer
    if (time.time() - log_time) > log_interval:
        log_time = time.time()

    # Wait for refresh
    time.sleep(1)
