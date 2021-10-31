from .component import Component

import adafruit_mcp3xxx.mcp3008 as MCP
import board
import busio
import digitalio

# Constants dictionary for MCP pin objects
PINS = {
    0: MCP.P0,
    1: MCP.P1,
    2: MCP.P2,
    3: MCP.P3,
    4: MCP.P4,
    5: MCP.P5,
    6: MCP.P6,
    7: MCP.P7
}

class _MCP3008(Component):
    def __init__(self,config):
        # Execute parent's constructor
        super().__init__(config)

        # Build SPI bus (default RPi SCK, MISO, MOSI pins)
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        # Build CS pin (default RPi CE0)
        cs = digitalio.DigitalInOut(board.D7)
        # Initialize MCP3008 object using SPI & CS
        self.mcp = MCP.MCP3008(spi, cs)

        try:
            self.pin = config['pin']
            self.pin in PINS
        except RuntimeError:
            print("[Runtime Error] Missing or invalid pin")

        self.state = 0

    def update(self):
        self.state = self.mcp.read(PINS[self.pin])
        return

    def asdict(self):
        dict = super().asdict()
        dict.update({
            'pin':self.pin,
            'state':self.state
        })

        return dict

class SoilSensor(_MCP3008):
    def __init__(self, config):
        super().__init__(config)

        if 'air_level' in config:
            self.air_level = config['air_level']
        else:
            self.air_level = 680

        if 'water_level' in config:
            self.water_level = config['water_level']
        else:
            self.water_level = 300

    def update(self):
        super().update()

        self.state = 100 - (((self.state - self.water_level) / (self.air_level - self.water_level)) * 100)

    def asdict(self):
        dict = super().asdict()
        dict['state'] = "{:.2f}".format(self.state) + '%'

        return dict
