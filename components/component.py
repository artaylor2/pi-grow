"""
    Component Object
        Represents a generalized component for
        purposes of inheritence.
"""

class Component:
    def __init__(self, config):
        self.type = type(self).__name__

        # All objects require a key, otherwise
        # otherwise throw an error
        try:
            self.key = config['key']
        except RuntimeError:
            print("[Runtime Error] Missing or invalid key") 

        # If name is empty use key instead
        if config['name']:
            self.name = config['name']
        else:
            self.name = self.key

    # Dictionary conversion function
    def asdict(self):
        dict = {
            'type': self.type,
            'key': self.key,
            'name': self.name
        }

        return dict

    # Tab for status function
    def status(self):
        return

    # Tab for update function
    def update(self):
        return
