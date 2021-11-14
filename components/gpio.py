"""
    GPIO
        This object represents a generic component
        connected using a GPIO pin

        self.gpio_in
            A DigitalInOut object representing the GPIO pin
        self.pin
            A string representing the GPIO pin's name
"""
from .component import Component

import board
import digitalio
import datetime
import time

class _GPIO(Component):
    def __init__(self, config):
        super().__init__(config)

        try:
            self.pin = config['pin']
            self.gpio_pin = digitalio.DigitalInOut(getattr(board, self.pin))
        except RuntimeError:
            print("[Runtime Error] Missing or invalid pin") 

    def status(self):
        return self.gpio_pin.value

    def asdict(self):
        dict = super().asdict()

        dict.update({
            "pin":self.pin,
            "state":self.gpio_pin.value
        })

        return dict

class GPIORelay(_GPIO):
    def __init__(self, config):
        super().__init__(config)

        # Set GPIO as output and default to off
        self.gpio_pin.switch_to_output()
        self.gpio_pin.value = True

        # If a maxtime key is set then use it
        if 'maxtime' in config:
            self.maxtime = config['maxtime']
        else:
            self.maxtime = 0

        # Set inital timestamp and current time
        self.timestamp = datetime.datetime.now()
        self.curtime = time.time()

        if 'invert' in config:
            self.invert = config['invert']
        else:
            self.invert = True

        # TODO: Figure out invert management logic
        self.state = not self.gpio_pin.value

        print('Initialized')

    # Toggle relay off
    def turn_off(self):
        self.gpio_pin.value = True
        self.timestamp = datetime.datetime.now()
        print('Toggle Off!')

    # Toggle relay on
    def turn_on(self):
        self.gpio_pin.value = False
        self.curtime = time.time()
        self.timestamp = datetime.datetime.now()
        print('Toggle On!')

    # Update object
    def update(self):
        # Update state
        # TODO: Update with invert logic
        self.state = not self.gpio_pin.value
        # Check for timeout
        if self.state and self.maxtime:
            if time.time() - self.curtime > self.maxtime:
                print('Timed Out')
                self.turn_off()

    # Dictionary conversion function
    def asdict(self):
        dict = super().asdict()
        dict.update({
            'invert':self.invert,
            'timeout':self.maxtime,
            'state':not self.gpio_pin.value
        })

        return dict
