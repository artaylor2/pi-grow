import yaml
import time

import os

import logger as log
import registrar

from components import gpio
from components import mcp3008

KEYS = {
    'soil_sensor': mcp3008.SoilSensor,
    'gpio_relay': gpio.GPIORelay
}

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

for c in config:
    if c in KEYS:
        print("Creating:", config[c])
        new = KEYS[c](config[c])
        
        reg.register(config[c]['key'], new)

    else:
        print("[ERROR]: Invalid component key: ",c)

while 1:

    #print('{:.2f}'.format(reg.get("soil_sensor_1").state) + "%")
    os.system('clear')
    print("==========")
    for n in reg.enum_keys():
        reg.get(n).update()

        print(reg.get(n).asdict())
        print("\n")
        
        logger.log(n, reg.get(n).asdict())

    time.sleep(3)

#sensor1 = mcp3008.SoilSensor(0)
#relay1 = gpio.GPIORelay("D22", 5)

#while 1:
#    print('{:.2f}'.format(sensor1.state) + "%")

#    if sensor1.state > 40 and not relay1.state:
#        relay1.turn_on()
#    elif sensor1.state <= 40 and relay1.state:
#        relay1.turn_off()

#    sensor1.update()
#    relay1.update()
