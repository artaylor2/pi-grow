class Registrar:
    def __init__(self):
        self._registry = {}

    def register(self, key, value):
        if key not in self._registry:
            self._registry.update({key:value})

    def enum_all(self):
        return self._registry()

    def enum_keys(self):
        return self._registry.keys()

    def enum_items(self):
        return self._registry.items()

    def get(self, key):
        return self._registry[key]

    def exists(self, key):
        return key in self._registry

    @property
    def length(self):
        return len(self.all())
